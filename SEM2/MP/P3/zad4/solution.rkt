#lang racket
;; lista 3 zadanie 8 Sortowanie przez scalanie (mergesort)

(provide mergesort merge split)

(define (merge left right) 
  (define (merge-rek left right res) ;;funkcja pomocnicza które rozpatruje przypadki 
    (cond  [(null? left) (append res right)] ;;gdy jedna lista jest pusta
           [(null? right) (append res left)] ;;gdy jedna lista jest pusta
           [(if (< (car left) (car right)) ;;porównanie elementów
                     (merge-rek (cdr left) right (append res (list(car left))))
                     (merge-rek left (cdr right) (append res (list(car right)))))]))
  (merge-rek left right '()))

(define (split lista) ;;funckja split która jako argument przyjmuje liste 
  (define mid (floor(/(length lista)2))) ;;mid to środek - dlugość funkcji / 2
  (define (part1 lista res) ;;
    (if (> (length lista) mid)
        (part1 (cdr lista) (append res (list(car lista))))
        (cons res lista)))
  (part1 lista '())) ;;wywołanie part1

(define (mergesort lista) ;;głowna funkcja która za argument przyjmuje liste
  (if (< (length lista) 2) ;;sprawdza czy lista jest jednoelementowa
      lista ;;jeśli tak to wypisz tą liste jednoelementową
      (merge (mergesort(car (split lista))) (mergesort(cdr (split lista))))));; jeśli nie to wywołaj merge

;;testy
(mergesort (list 1 4 5 2 9 7))                  ;;powinniśmy spodziewać się rosnących ciągów liczb
(mergesort (list 1.2 -4 5 -2 9/3 7))
(mergesort (list 1 4 5 2 2 5 3/4))
(mergesort (list 1 -4.234 5.123 2 123.9 7))

