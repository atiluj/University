traceroute: main.o error.o icmp_receive.o icmp_send.o
	g++ -o traceroute main.o error.o icmp_receive.o icmp_send.o
main.o: main.cpp
	g++ -c -Wall -Wextra main.cpp
error.o: error.cpp
	g++ -c -Wall -Wextra error.cpp
icmp_receive.o: icmp_receive.cpp
	g++ -c -Wall -Wextra icmp_receive.cpp
icmp_send.o: icmp_send.cpp
	g++ -c -Wall -Wextra icmp_send.cpp
clean:
	rm main.o error.o icmp_receive.o icmp_send.o
distclean: clean
	rm traceroute
