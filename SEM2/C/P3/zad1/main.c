#include "decimalio.h" //lista 2 zad. 1

int main()
{
    int x, power;
    x = read_decimal();
    for(int i = 0; i < x; i++){
        power = i * i;
        trace_decimal(power);
    }
    return 0;
}
