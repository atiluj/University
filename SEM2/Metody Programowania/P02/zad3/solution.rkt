#lang racket
;;zad. 11 Pierwiastki dowolnych stopni przez tłumienie z uśrednianiem  lista 2

(provide nth-root)

(define eps 0.0001)   ;;zdefiniowanie odległości

(define (close-to? a b)  ;;badanie odległosci
  (< (abs(- a b)) eps))

(define (average a b) ;;średnia
  (/ (+ a b) 2))
  
;;procedury z ćwiczeń:
(define (compose f g)
  (lambda (x) (f (g x))))

(define (identity f) f)

(define (repeated f n)
  (if(= n 0)
     identity
     (compose f (repeated f (- n 1)))))

(define (nth-pow x n)  ;;funkcja zwraca x^n
    (if(= n 0)
       1
       (* (nth-pow x (- n 1)) x)))

;;procedury z wykładu:
(define (fixed-point f guess1)
  (define (try guess)
    (let ([imp (f guess)])
      (if (close-to? guess imp)
          imp
          (try imp))))
  (try guess1))

(define (average-damp f)
  (lambda (x) (average x (f x))))

;;procedury do rozwiązania zadania:
(define (nth-power x n)
  (if (= n 0)
      1
      (* x (nth-power x (- n 1)))))

(define (nth-root x n)
  (if (= n 1)
      x
     (fixed-point ((aprox (floor(-(log x 2)1)))
                   (lambda (y)(/ x (nth-pow y (- n 1)))))
                  1.0)))
  
;;procedury do testowania ilości wymaganych tłumień:
(define (aprox k)
  (repeated average-damp k))  ;;k-krotne tłumienie
  
(define (test-k x n k) ;;x-wartość ;;n-stopien pierwiastka ;;k-ilość tłumie
  (if (= n 1)
      x
     (fixed-point ((aprox k)
                   (lambda (y) (/ x (nth-pow y (- n 1)))))
                  1.0)))

;;testy:
"dla pierwiastkow stopnia 1"
(test-k 13 1 1)

"sprawdzamy optymalna ilosc wytlumien:  x=64 n=3"
"dla k=2"(test-k 64 3 2)
"dla k=5"(test-k 64 3 5)
"dla k=6"(test-k 64 3 6)
"dla k=7"(test-k 64 3 7)
;;optymalny wynik uzyskujemy dla k=5
"sprawdzamy optymalna ilosc wytlumien:  x=625 n=4"
"dla k=8"(test-k 625 4 8)
"dla k=9"(test-k 625 4 9)
"dla k=10"(test-k 625 4 10)
;;optymalny wynik uzyskujemy dla k=8
"sprawdzamy optymalna ilosc wytlumien:  x=35937 n=3"
"dla k=13"(test-k 35937 3 13)
"dla k=14"(test-k 35937 3 14)
;;optymalny wynik uzyskujemy dla k=13

;;mozemy zauważyć, że 5 = log2(64)-1 oraz 8 < log2(625)-1 oraz 13 = log2(35937)-1
;;zatem przyjmujemy, że stosowna ilosc wytlumien wyraza sie poprzez (floor(-(log n 2)1))

"testujemy procedure nth-root dla paru przykladowych wartosci:"
"dla x=625 n=9"(nth-root 625 9)
"dla x=512 n=3"(nth-root 512 3)
"dla x=8192 n=13"(nth-root 8192 13)
"dla x=35920 n=3"(nth-root 35920 3) ;;33*33*33=35937

