#lang racket
;;---  zadanie 11  --- Kompilacja RPN do Arith

(provide (struct-out const) (struct-out binop) rpn->arith)

(struct const (val)    #:transparent)
(struct binop (op l r) #:transparent)

(define (delete-nth list n) ;;funkcja usuwający i-ty element w liscie
    (if (= n 0)
        (cdr list)
        (cons (car list) (delete-nth (cdr list) (- n 1)))))

(define (rpn->arith e)
  (define (mk-const x)
  (if (number? x)
      (const x)
      x))
  (define (converse-rpn w iter) ;;wywolanie od iter=0, nim przechodzimy po liście w poszukiwaniu operatora 
    (if (and (< iter (length w)) (member (list-ref w iter) '(+ - * /)))
        (if (< iter 2)
            (error "niepoprawne wyrazenie w RPN")
            (let* ([l (list-ref w (- iter 2))]
                   [r (list-ref w (- iter 1))]
                   ;; wykonanie i zapisanie działania na dwóch liczbach przed operatorem
                   [w-update (list-set w (- iter 2) (binop (list-ref w iter) (mk-const l) (mk-const r)))])
                 ;;usuniecie dwoch juz niepotrzebnych elementow i ponowne wywolanie funkcji
                (converse-rpn (delete-nth (delete-nth w-update (- iter 1)) (- iter 1)) (- iter 1))))
        (if (= iter (length w))
           (first w)
            (converse-rpn w (+ iter 1)))))
  (converse-rpn e 0))
