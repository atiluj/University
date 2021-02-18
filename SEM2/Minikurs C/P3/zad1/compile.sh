#!/bin/bash
gcc -Wall -c decimalio.c -o decimalio.o
gcc -Wall -c main.c -o main.o
gcc -lm decimalio.o main.o -o program
