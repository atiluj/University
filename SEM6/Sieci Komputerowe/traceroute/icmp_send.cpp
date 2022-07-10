#include <netinet/in.h>
#include <netinet/ip_icmp.h>
#include <assert.h>
#include <unistd.h>
#include <memory.h>

#include "error.h"

u_int16_t compute_icmp_checksum (const u_int16_t *buff, int length)
{
	u_int32_t sum;
	const u_int16_t* ptr = buff;
	assert (length % 2 == 0);
	for (sum = 0; length > 0; length -= 2)
		sum += *ptr++;
	sum = (sum >> 16) + (sum & 0xffff);
	return (u_int16_t)(~(sum + (sum >> 16)));
}

void icmp_send(int internet_socket, struct sockaddr_in ip, int i, int j) {
    struct icmp data;
    memset(&data, 0, sizeof(struct icmp));
    data.icmp_type = ICMP_ECHO;
    data.icmp_id = getpid();
    data.icmp_seq = i * 3 + j - 1;
    data.icmp_cksum = compute_icmp_checksum((u_int16_t *)&data, sizeof(struct icmp));
    int result = setsockopt(internet_socket, IPPROTO_IP, IP_TTL, &i, sizeof(int));
    if (result == -1) {
        error("Nie udało się skonfigurować gniazda!");
    }
    result = sendto(internet_socket, &data, sizeof(struct icmp), 0, (struct sockaddr *)&ip, sizeof(struct sockaddr_in));
    if (result == -1) {
        error("Nie udało się wysłać!");
    }
}