#lang racket
--- zad 22 ----
;; na podstawie szablonu
;; miejsca zmienione lub dopisane zostały oznaczone symbolem
;;<----------------- ZAD22

(require racklog)
(provide solve)

;; transpozycja tablicy zakodowanej jako lista list
(define (transpose xss)
  (cond [(null? xss) xss]
        ((null? (car xss)) (transpose (cdr xss)))
        [else (cons (map car xss)
                    (transpose (map cdr xss)))]))

;; procedura pomocnicza
;; tworzy listę n-elementową zawierającą wyniki n-krotnego
;; wywołania procedury f
(define (repeat-fn n f)
  (if (eq? 0 n) null
      (cons (f) (repeat-fn (- n 1) f))))

;; tworzy tablicę n na m elementów, zawierającą świeże
;; zmienne logiczne
(define (make-rect n m)
  (repeat-fn m (lambda () (repeat-fn n _))))

;;procedura sprawdzajaca czy dana lista ys sklada sie z samych podkreślników, lub jest pusta
(define %is-plain ;;<----------------- ZAD22
  (%rel (y ys)
        [(null)]
        [((cons y ys))
         (%is y '_)
         (%is-plain ys)]))

;; predykat binarny ;;<----------------- ZAD22
(define %row-ok
  (%rel (xs ys)
  [(xs ys) (%row-ok-2 xs ys 0)]))

;;funkcja pomocnicza
(define %row-ok-2 ;;<----------------- ZAD22
  (%rel (x xs y ys s) ;;s-mówi o tym jaki znak było ostatnio (1* 0_)
        [('() '() s)]
        [('() ys s) (%is-plain ys)]
        [('(1) (cons '* ys) s) (%is-plain ys)]
        [((cons x xs) (cons '_ ys) s)
         (%= s 0)
         (%row-ok-2 (cons x xs) ys s)]
        [((cons 0 xs) (cons '_ ys) s)
         (%row-ok-2 xs ys 0)]
        [((cons x xs) (cons '* ys) s)
         (%is y (- x 1))
         (%row-ok-2 (cons y xs) ys 1)]
        ))

;;sprawdza czy rzędy się zgadzają
(define %rows-ok ;;<----------------- ZAD22
  (%rel (x y xs ys)
        [(null null)]
        [((cons x xs) (cons y ys))
         (%row-ok x y)
         (%rows-ok xs ys)]))

;;test do rows-ok
#|(%which () (%rows-ok '((2) (1) (1))
        '((* *)
          (_ *)
          (* _))))|#

;; funkcja rozwiązująca zagadkę
(define (solve rows cols)
  (define board (make-rect (length cols) (length rows)))
  (define tboard (transpose board))
  (define ret (%which (xss yss) 
                      (%= xss board)
;; TODO  <------------------------------------------ ZAD22
                      (%rows-ok rows xss)
                      (%= yss tboard)
                      (%rows-ok cols yss)))
                      
  (and ret (cdar ret)))

;; testy
;;(solve '((2) (1) (1)) '((1 1) (2)))
;;(solve '((2) (2 1) (1 1) (2)) '((2) (2 1) (1 1) (2)))
;;(solve '((4) (6) (2 2) (2 2) (6) (4) (2) (2) (2))
               ;;'((9) (9) (2 2) (2 2) (4) (4)))
#|
(equal? (solve '((2) (1) (1)) '((1 1) (2)))
        '((* *)
          (_ *)
          (* _)))

(equal? (solve '((2) (2 1) (1 1) (2)) '((2) (2 1) (1 1) (2)))
        '((_ * * _)
          (* * _ *)
          (* _ _ *)
          (_ * * _)))

(equal? (solve '((4) (6) (2 2) (2 2) (6) (4) (2) (2) (2))
               '((9) (9) (2 2) (2 2) (4) (4)))
        '((* * * * _ _)
          (* * * * * *)
          (* * _ _ * *)
          (* * _ _ * *)
          (* * * * * *)
          (* * * * _ _)
          (* * _ _ _ _)
          (* * _ _ _ _)
          (* * _ _ _ _)))

;; Moje testy

(equal? (solve '((1) (1) (1) (1) (1))
               '((1) (1) (1) (1) (1)))
        '((* _ _ _ _)
          (_ * _ _ _)
          (_ _ * _ _)
          (_ _ _ * _)
          (_ _ _ _ *)))

(equal? (solve '((2 2) (5) (1 1 1) (1 1))
               '((4) (2) (2) (2) (4)))
        '((* * _ * *)
          (* * * * *)
          (* _ * _ *)
          (* _ _ _ *)))

(equal? (solve '((4) (1 1) (1 1) (4))
               '((4) (1 1) (1 1) (4)))
        '((* * * *)
          (* _ _ *)
          (* _ _ *)
          (* * * *)))

(equal? (solve '((4) (1) (1) (1 1) (4))
               '((1 2) (1 1) (1 1) (5)))
        '((* * * *)
          (_ _ _ *)
          (_ _ _ *)
          (* _ _ *)
          (* * * *)))

(equal? (solve '((4) (1 1) (4) (1 1) (1 1))
               '((1) (1 1) (1 1) (5))) ;; drugie (1 1) jest źle
        '((* * * *)
          (* _ _ *)
          (* * * *)
          (* _ * _)
          (* _ _ *)))

(equal? (solve '((4) (1 1) (3) (1 1) (1 1)) ;;3 jeste źle
               '((1) (1 1) (1 1) (5)))
        '((* * * *)
          (* _ _ *)
          (* * * *)
          (* _ * _)
          (* _ _ *)))
|#

