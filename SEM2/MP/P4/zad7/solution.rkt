#lang racket
;;lista 4 zad 8   Sortowanie przez kopcowanie (heapsort)

(require "leftist.rkt")
(provide heapsort)

;;procedura sortujaca kopiec lewicowy
(define (heapsort lista)
  (define (list-to-heap heap lista) ;;z elemntów listy budujemy kopiec
    (if (null? lista)
        heap
        (list-to-heap (heap-insert (car lista) heap) (cdr lista))))
  (define (heap-to-list heap)
    (if (heap-empty? heap)  ;;z kopca robimy posortowana liste
        null
        (cons (heap-min heap) (heap-to-list (heap-pop heap)))))
  (heap-to-list (list-to-heap empty-heap lista)))


;;testy:                                 oczekiwany rezultat:
;;(heapsort (list))                            '()               
;;(heapsort (list 2 7 2 -1 0 2))               '(-1 0 2 2 2 7)
;;(heapsort (list 1/2 -0.33 74/13 8))          '(-0.33 1/2 74/13 8)
