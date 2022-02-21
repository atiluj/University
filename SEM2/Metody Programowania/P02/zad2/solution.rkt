#lang racket 
;; lista 2 zad. 10 UŁAMKI ŁAŃCUCHOWE 

(provide cont-frac)  

(define (cont-frac num den n) ;; bierze dwie funkcje jednoargumntowe ;;n - dokładaność (do ilu miejsc po przecinku)
    (define (precision i) ;;funckja zwraca (0.1)^i (i to n), dokładność 
      (if (> i 0) 
        (* 0.1 (precision (- i 1))) 
        1)) 

  (define (step An_1 Bn_1 An_2 Bn_2 i) ;;Funkcja step zapamiętuje poprzednią i wylicza aktualną wartość. Następnie jeżeli ich różnica jest mniejsza od zadanej dokładności, zwraca wynik. 
     (define An (+ (* (den i) An_1) (* (num i) An_2))) ;Wzór na nowe An 
     (define Bn (+ (* (den i) Bn_1) (* (num i) Bn_2))) ;Wzór na nowe Bn 
     (if (> i 500) (/ An Bn) ;; czasem nie da się osiągnąć takiej dokładności jaka chce użytkownik i funkcja się zapętla 
     (if (< (abs (- (/ An_1 Bn_1) (/ An Bn))) (precision n)) 
         (/ An Bn) 
         (step An Bn An_1 Bn_1 (+ i 1))))) 
  (step 0 1 1 0 1)) 


;; do testow
(define (square x) (* x x))

;; przykłady testowe                                                             czego powinniśmy oczekiwać
(+ 1 (cont-frac (lambda (i) 1.0) (lambda (i) 1.0) 10))                           ;;>1.618033988738303 
(+ 3 (cont-frac (lambda (i) (square (- (* 2 i) 1)))  (lambda (i) 6.0) 6))        ;;>3.1415931417757212
