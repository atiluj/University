#include <stdio.h>  // lista 2 zad. 1
#include "decimalio.h"

typedef unsigned char bool;

static bool is_digit(const char c){  //zwraca prawde jeœli c jest z przedzia³u 1-9, wpp. fa³sz
    return '0' <= c && c <= '9';
}

static bool is_space_or_newline(const char c){   //zwraca prawde jeœli c jest spacj¹ lub znakiem nowej linii, wpp fa³sz
    return c == ' ' || c == '\n';
}

int read_decimal(){   //czyta znak
    int d = 0;
    char c;
    do //pobiera znak (omija spacje i znaki nowej linii)
        c = getchar();
    while( is_space_or_newline(c) );
    do {//pobiera pierwsza liczbe do spacji i zapisuje w d
        d *= 10;
        d += c - '0'; //chcem aby d by³o int. '0'-48 '1'-49 ... '9'-57, wiêc przyk³adowo 57-48=9 i mamy int.
        c = getchar();
    }while( is_digit(c) );

    ungetc(c, stdin);
    return d;
}

int trace_decimal(const int d){ //œcie¿ka
    int b = 1;
    while(b * 10 <= d)
        b *= 10;
    while(b > 0){
        putchar( (d/b)%10 + '0' );//zamiana na char
        b /= 10;
    }
    putchar('\n'); // dzia³a tak samo jak putc(c, stdout)
    return d;
}

