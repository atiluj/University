#include <netinet/in.h>
#include <netinet/ip_icmp.h>
#include <unistd.h>

#include "error.h"

bool icmp_reply_verify(struct icmp *icmp_packet, int i) {
    return icmp_packet->icmp_type == ICMP_ECHOREPLY && icmp_packet->icmp_id == getpid() && icmp_packet->icmp_seq / 3 == i;
}

bool icmp_time_exceeded_verify(struct icmp *icmp_packet, int i) {
    if (icmp_packet->icmp_type == ICMP_TIME_EXCEEDED) {
        struct ip *inner_ip = (struct ip *)&icmp_packet->icmp_data;
        struct icmp *inner_icmp = (struct icmp *)((char *)inner_ip + 4 * inner_ip->ip_hl);
        return inner_icmp->icmp_id == getpid() && inner_icmp->icmp_seq / 3 == i;
    }
    return false;
}

in_addr_t icmp_receive(int internet_socket, int i) {
    char data[1024];
    struct sockaddr_in destination_ip;
    socklen_t size = sizeof(struct sockaddr_in);
    int result = recvfrom(internet_socket, &data, 1024, 0, (struct sockaddr *)&destination_ip, &size);
    if (result == -1) {
        error("Błąd przy odbieraniu danych!");
    }
    if (size != sizeof(struct sockaddr_in)) {
        error("System zwrócił adres innego rozmiaru!");
    }

    struct ip *ip_packet = (struct ip *)&data;
    struct icmp *icmp_packet = (struct icmp *)((char *)ip_packet + 4 * ip_packet->ip_hl);
    if (icmp_reply_verify(icmp_packet, i) || icmp_time_exceeded_verify(icmp_packet, i)) {
        return destination_ip.sin_addr.s_addr;
    } else {
        return -1;
    }
}