#lang racket
;; poniższy kod pochodzi z polecenia zadania
;; zmienione i dodane fragmenty zostały ozanczone symbolem ;;<-------- ZAD16

(provide lcons lnull lnull? lcar lcdr proc normal lnth from lfilter prime? primes)

(define (lcons x f) (mcons x f))
(define lnull null)
(define lnull? null?)
(define (lcar xs) (mcar xs));->wyjsciowe n
(define (lcdr xs) ((mcdr xs))) ;-> (lcons wart1 (lcons wart2 ... (lcons wartk ogon)...))

(define (proc xs) ;;<-------- ZAD16
  (if (procedure? (mcdr xs))
      xs
      (proc (mcdr xs))))

(define (normal xs) ;;<-------- ZAD16
  (if (procedure? xs)
      (cons xs null)
      (cons (mcar xs) (normal (mcdr xs)))))

(define(lnth n xs) ; (lcons 2 (lcons 3 (lcons 5 proc)))
  (define normal-list (normal xs))
  (cond[(= n 0) (lcar xs)]
       [(< n (length normal-list)) ;;<-------- ZAD16
        (list-ref normal-list (- n 1))] ;;
       [else (let ([proc-pair (proc xs)]) ;;
               (begin (set-mcdr! proc-pair (lcdr proc-pair)) ;;
                      (lnth n xs)))])) ;;
  
(define (from n)
  (lcons n (lambda () (from (+ n 1)))))

(define (lfilter p xs)
  (cond [(lnull? xs) lnull]
        [(p (lcar xs))
         (lcons (lcar xs) (lambda () (lfilter p (lcdr xs))))]
        [else (lfilter p (lcdr xs))]))

(define (prime? n) ; definicja umyslnie malo wydajna
  (define (factors i)
    (cond [(>= i n) (list n)]
          [(= (modulo n i) 0) (cons i (factors (+ i 1)))]
          [else (factors (+ i 1))]))
  (= (length (factors 1)) 2))

;lista wszystkich liczb pierwszych
(define primes (lfilter prime? (from 2)))

;;testy
#|
(time (lnth 1000 primes))
(time (lnth 1001 primes))
(time (lnth 1002 primes))
|#
