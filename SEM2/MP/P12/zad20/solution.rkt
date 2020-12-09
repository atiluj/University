#lang racket
;;---zad 20 --- Komponenty i quickchech
;; na  podstawie kodu z pliku stack-and-fifo.rkt
;; kod został dopisany w wyzanczonych i wskazanych do tego miejscach

(require "graph.rkt")
(provide bag-stack@ bag-fifo@)

;; struktura danych - stos
(define-unit bag-stack@
  (import)
  (export bag^)
  (define (bag? d) 
    (and (list? d)
         (eq? (length d) 2)
         (list? (cdr d))
         (eq? (car d) 'bag-stack)))

  (define (bag-stack d) (cadr d))
  
  (define (bag-cons l) (list 'bag-stack l))
  
  (define (bag-empty? d)
    (eq? (bag-stack d) '()))

  (define empty-bag (bag-cons '()))

  (define (bag-peek l)
    (car (bag-stack l)))

  (define (bag-remove l)
    (bag-cons (cdr (bag-stack l))))

  (define (bag-insert l x)       
    (if (bag-empty? l)
        (bag-cons (list x))
        (bag-cons (cons x (bag-stack l)))))
  )

;; struktura danych - kolejka FIFO
(define-unit bag-fifo@
  (import)
  (export bag^)

  (define (bag? d)
    (and (list? (caadr d))
         (list? (cddr d))
         (= (length d) 2)
         (= (length (cadr d)) 2);
         (eq? (car d) 'bag-fifo)))

  (define (bag-fifo d) (cadr d)) ;;zwróci pare list
  
  (define (bag-cons l) (list 'bag-fifo l))
  
  (define (bag-empty? d)
    (equal? (bag-fifo d) '(() ()) ))

  (define empty-bag (bag-cons '(() ()) ))

  (define (bag-peek l)                   
    (if (eq? (car (bag-fifo l)) '() )
        (car (reverse (cadr (bag-fifo l))))
        (car (car (bag-fifo l)))))

  (define (bag-remove l)
    (if (eq? (car (bag-fifo l)) '())
        (bag-cons (list (cdr (reverse (cadr (bag-fifo l)))) '()))
        (bag-cons (list (cdr (car (bag-fifo l))) (cadr (bag-fifo l))))))

  (define (bag-insert l x)       ;; (1 2 3) (x 1 2 3)
    (bag-cons (list (car (bag-fifo l)) (cons x (cadr (bag-fifo l)))))))

;; otwarcie komponentów stosu i kolejki

(define-values/invoke-unit bag-stack@
  (import)
  (export (prefix stack: bag^)))

(define-values/invoke-unit bag-fifo@
  (import)
  (export (prefix fifo: bag^)))


#| testy
(define-unit empty@
  (import bag^)
  (export)

  (define a empty-bag)
  (display a)
  (display (bag-insert (bag-insert a 3) 4))
  )

(define-unit empty2@
  (import bag^)
  (export)

  (define b empty-bag)
  (display b)
  (display (bag-remove (bag-insert (bag-insert b 3) 4))))  


(invoke-unit empty@ (import (prefix stack: bag^)))
(invoke-unit empty2@ (import (prefix fifo: bag^)))|#


;; testy w Quickchecku
(require quickcheck)

;; testy kolejek i stosów
(define-unit bag-tests@
  (import bag^)
  (export)
  
  ;; test przykładowy: jeśli do pustej struktury dodamy element
  ;; i od razu go usuniemy, wynikowa struktura jest pusta
  (quickcheck
   (property ([s arbitrary-symbol])
             (bag-empty? (bag-remove (bag-insert empty-bag s)))))
  
  ;; TODO: napisz inne własności do sprawdzenia!
  (quickcheck
   (property ([s arbitrary-symbol])
             (eq? s (bag-peek (bag-insert empty-bag s)))))

  (quickcheck
   (property ([s arbitrary-symbol])
             (not (bag-empty? (bag-remove (bag-insert (bag-insert empty-bag s) s))))))

  (quickcheck
   (property ([s arbitrary-symbol])
             (not (bag-empty? (bag-insert empty-bag s))))))


;;O00000000000000000000000000LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

;; uruchomienie testów dla obu struktur danych
(display "------STOS&FIFO------\n")
(invoke-unit bag-tests@ (import (prefix stack: bag^)))
(invoke-unit bag-tests@ (import (prefix fifo: bag^)))
(display "--------STOS-------\n")
;; TODO: napisz też testy własności, które zachodzą tylko dla jednej
;;STOS;; testy stosów
(define-unit bag-tests-stack@
  (import bag^)
  (export)

  (quickcheck
   (property ([s arbitrary-symbol])
             (eq? s (bag-peek (bag-insert empty-bag s)))))

  (quickcheck
   (property ([s arbitrary-symbol]
              [p arbitrary-symbol])
             (eq? p (bag-peek (bag-insert (bag-insert empty-bag s) p)))))
  
  (quickcheck
   (property ([s arbitrary-symbol]
              [p arbitrary-symbol])
             (eq? s (bag-peek (bag-remove (bag-insert (bag-insert empty-bag s) p)))))))


(invoke-unit bag-tests-stack@ (import (prefix stack: bag^)))
(display "--------FIFO-------\n")
;;KOLEJKA
;; testy kolejek
(define-unit bag-tests-fifo@  
  (import bag^)
  (export)

  (quickcheck
   (property ([s arbitrary-symbol]
              [p arbitrary-symbol])
             (eq? (bag-peek (bag-insert empty-bag s)) (bag-peek (bag-insert (bag-insert empty-bag s) p)))))

  (quickcheck
   (property ([s arbitrary-symbol]
              [p arbitrary-symbol])
             (eq? s (bag-peek (bag-insert (bag-insert empty-bag s) p)))))

  (quickcheck
   (property ([s arbitrary-symbol]
              [p arbitrary-symbol])
             (eq? p (bag-peek (bag-remove (bag-insert (bag-insert empty-bag s) p)))))))

(invoke-unit bag-tests-fifo@ (import (prefix fifo: bag^)))
;; z dwóch zaimplementowanych struktur danych

;; otwarcie komponentu grafu
(define-values/invoke-unit/infer simple-graph@)

;; otwarcie komponentów przeszukiwania 
;; w głąb i wszerz
(define-values/invoke-unit graph-search@
  (import graph^ (prefix stack: bag^))
  (export (prefix dfs: graph-search^)))

(define-values/invoke-unit graph-search@
  (import graph^ (prefix fifo: bag^))
  (export (prefix bfs: graph-search^)))

;; graf testowy
(define test-graph
  (graph
   (list 1 2 3 4)
   (list (edge 1 3)
         (edge 1 2)
         (edge 2 4))))
;; TODO: napisz inne testowe grafy
(define test-graph-2
  (graph
   (list 1 2)
   (list (edge 1 2)
         (edge 2 1))))

(define test-graph-3
  (graph
   (list)
   (list)))

(define test-graph-4
  (graph
   (list 1 2)
   (list (edge 1 1))))

(define test-graph-5
  (graph
   (list 1 2 3 4 5)
   (list (edge 1 2)
          (edge 2 3)
           (edge 3 4)
            (edge 4 5)
             (edge 5 1)
              (edge 2 4)
              )))

(define test-graph-6
  (graph
   (list 1 2 3)
   (list (edge 2 3))))

;; uruchomienie przeszukiwania na przykładowym grafie
(bfs:search test-graph 1)
(dfs:search test-graph 1)
;; TODO: uruchom przeszukiwanie na swoich przykładowych grafach

(bfs:search test-graph-2 1)
(dfs:search test-graph-2 1)

(bfs:search test-graph-3 1)
(dfs:search test-graph-3 1)

(bfs:search test-graph-4 1)
(dfs:search test-graph-4 1)

(bfs:search test-graph-5 1)
(dfs:search test-graph-5 1)

(bfs:search test-graph-6 1)
(dfs:search test-graph-6 1)
