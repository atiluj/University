#lang racket
;; zadanie zostało wykonane na podstawie programu sqrt z wykładu
;; miejsca które zostały zmienione zostały oznaczone ';;*'

(provide cube-root) ;;*

(define (cube-root x) ;;*
  ;; lokalne definicje
  ;; poprawianie przybliżenia
  (define (square x) (* x x))
  (define (cube x) (* x x x))
  (define (dist x y) (abs (- x y)))
  (define (improve guess)
    (/ (+ (/ x (square guess)) (* 2 guess) ) 3))    ;;*
  ;; sprawdzanie czy przybliżenie jest wystarczająco dobre
  (define (good-enough? g)
    (< (dist x (cube g))   ;;*
       0.0001))
  ;; procedura iterująca poprawianie przybliżenia aż
  ;; osiągniemy wystarczająco dobre przybliżenie
  (define (iter guess)
    (if (good-enough? guess)
        guess
        (iter (improve guess))))
  
  (iter 1.0))

;; przykłady testowe    czego powinniśmy oczekiwać
(cube-root 27)          ;; 3
(cube-root 24)          ;; mniej niż 3
(cube-root 1)           ;; 1
(cube-root 64)          ;; 4

;;program 
