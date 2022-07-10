// Julita Osman 314323
#include <iostream>
#include <arpa/inet.h>
#include <chrono>

#include "error.h"
#include "icmp_send.h"
#include "icmp_receive.h"

using namespace std;

struct sockaddr_in ip;
int internet_socket;
chrono::time_point<chrono::high_resolution_clock> sending_time;
struct in_addr destination_ips[3];
int destination_milliseconds[3];
int destination_replies;

int main(int argc, char* argv[]) {
    if (argc == 1) {
        error("Podaj IP!");
    }
    if (argc > 2 || argc < 1) {
        error("Niepoprawne polecenie!");
    }

    ip.sin_family = AF_INET;
    ip.sin_addr.s_addr = inet_addr(argv[1]);
    if (ip.sin_addr.s_addr == (in_addr_t)-1) {
        error("Niepoprawny adres IP!");
    }

    internet_socket = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
    if (internet_socket == -1) {
        error("Nie udało się otworzyć gniazda!");
    }

    for (int i = 1; i <= 30; i++) {
        sending_time = chrono::high_resolution_clock::now();
        for (int j = 1; j <= 3; j++) {
            icmp_send(internet_socket, ip, i, j);
        }

        struct timeval timeout;
        timeout.tv_sec = 1;
        timeout.tv_usec = 0;
        destination_replies = 0;
        while (destination_replies < 3) {
            fd_set set;
            FD_ZERO(&set);
            FD_SET(internet_socket, &set);
            int result = select(internet_socket + 1, &set, NULL, NULL, &timeout);

            if (result == -1) {
                error("Nie udało się czekać na wynik!");
            }
            if (result > 0) {
                in_addr_t destination_ip = icmp_receive(internet_socket, i);
                if (destination_ip != (in_addr_t)-1) {
                    destination_ips[destination_replies].s_addr = destination_ip;
                    destination_milliseconds[destination_replies] = chrono::duration_cast<chrono::milliseconds>(chrono::high_resolution_clock::now() - sending_time).count();
                    destination_replies++;
                }
            }
            if (result == 0) {
                // czas minął
                break;
            }
        }

        cout << i << ". ";
        if (destination_replies == 0) {
            cout << "*" << endl;
            continue;
        }

        cout << inet_ntoa(destination_ips[0]) << " ";
        
        if (destination_replies >= 2 && destination_ips[0].s_addr != destination_ips[1].s_addr) {
            cout << inet_ntoa(destination_ips[1]) << " ";
        }
        if (destination_replies >= 3 && destination_ips[0].s_addr != destination_ips[2].s_addr && destination_ips[1].s_addr != destination_ips[2].s_addr) {
            cout << inet_ntoa(destination_ips[2]) << " ";
        }

        if (destination_replies == 3) {
            int average = (destination_milliseconds[0] + destination_milliseconds[1] + destination_milliseconds[2]) / 3;
            cout << average << "ms" << endl;
        } else {
            cout << "???" << endl;
        }

        if (destination_ips[0].s_addr == ip.sin_addr.s_addr) break;
    }

    return 0;
}