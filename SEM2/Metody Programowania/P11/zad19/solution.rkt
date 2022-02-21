#lang racket
;; --- zad 19 --- Kontrakty parametryczne
;; procedura foldr-map to zmodyfikowany kod z zajęć Pana Draba 

(require racket/contract)

(provide (contract-out
          [with-labels with-labels/c]
          [foldr-map foldr-map/c]
          [pair-from pair-from/c]))
(provide with-labels/c foldr-map/c pair-from/c)

;; podpunkt 1
(define with-labels/c
  (parametric->/c [a b] (->
                         (-> a b) (listof a)
                         (listof (list/c b a)))))

(define (with-labels f lis)
  (if (null? lis)
      lis
      (cons (list (f (car lis)) (car lis)) (with-labels f (cdr lis)))))

;(with-labels number->string (list 1 2 3 4))

;;; podpunkt 2
;; na podstawie zadania 5 z ćwiczeń
(define foldr-map/c (parametric->/c [e a i] (->
                                             (-> e a (cons/c i a)) a (listof e)
                                             (cons/c (listof i) a)
                                             )))

(define (foldr-map f a xs)
  (define (it a xs ys)
    (if (null? xs)
        (cons ys a)
        (let [(p (f (car xs) a))]
          (it (cdr p)
              (cdr xs)
              (cons (car p) ys)))))
  (it a (reverse xs) null))

;;(foldl-map (λ (x a) (cons a (+ a x))) 0 '(1 2 3 4 5))
;; ((0 1 3 6 10) . 15)
;;(foldr-map (λ (x a) (cons a (+ a x))) 0 '(1 2 3 4 5))
;;((0 5 9 12 14) . 15)

;; podpunkt 3
(define pair-from/c
  (parametric->/c [a b c] (->
                           (-> a b) (-> a c)
                           (-> a (cons/c b c)))))

(define (pair-from f g)
  (lambda (x) (cons (f x) (g x))))

;((pair-from (lambda (x y) (+ x y)) (lambda (x) (* x 2))) 2)
;((pair-from ((lambda (x) (+ x 1)) 3) (lambda (x) (* x 2))) 2)
;((pair-from (lambda (x) 'a) (lambda (x) (* x 2))) 2)            ;;(a . 4)
;((pair-from 5 (lambda (x) (* x 2))) 2)
;((pair-from "what did you did you?" (lambda (x) (* x 2))) 2)

