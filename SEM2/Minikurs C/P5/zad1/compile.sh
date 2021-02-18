#!/bin/bash   // Julita Osman 314323 lista 4 zadanie 1
gcc -Wall -c bst.c -o bst.o
gcc -Wall -c main.c -o main.o
gcc -lm bst.o main.o -o program
