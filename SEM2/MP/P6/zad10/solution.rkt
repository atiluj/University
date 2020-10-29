#lang racket
;;Interpreter wyrazen z liczbami zespolonymi

;;instrukcje do momentu pojawienia sie dlugiego ciągu znak ';' pochodzą ze wzoru na zadanie 10
(provide (struct-out complex) parse eval)

(struct complex (re im) #:transparent)
(struct variable ()     #:transparent)

(define value?
  complex?)

(struct const (val)    #:transparent)
(struct binop (op l r) #:transparent)

(define (op->proc op)
  (match op ['+ +] ['- -] ['* *] ['/ /]))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(define (eval e)
  (match e
    [(const n)  n]
    [(complex re im) (complex re im)]
    [(binop op l r)  (let* ([re-l (complex-re (eval l))]
                            [re-r (complex-re (eval r))]
                            [im-l (complex-im (eval l))]
                            [im-r (complex-im (eval r))])
                       (match e
                         [(binop '+ l r) (complex (+ re-l  re-r)
                                                  (+ im-l im-r))]
                         [(binop '- l r) (eval (binop '+ l (complex (- re-r)
                                                                    (- im-r))))]
                         [(binop '* l r) (complex (+ (* re-l re-r)
                                                           (* im-l im-r -1))
                                                  (+ (* re-l im-r)
                                                            (* re-r im-l)))]
                         [(binop '/ l r) (let* (  [comp-r (eval r)];; (a + bi)/(c + di) = [(a + bi)*(c - di)] / [(c + di)*(c - di)]
                                                  [comp-l (eval l)]
                                                  [neg-im-comp-r (complex (complex-re comp-r) (* -1 (complex-im comp-r)))]
                                                  [pom (eval (binop '* comp-l  neg-im-comp-r))] ;;licznik
                                                  ;;(c + di)*(c - di) wynik tego działania da nam liczbe rzeczywista
                                                  [dzielnik (complex-re (eval (binop '* neg-im-comp-r comp-r)))]) ;;mianownik
                                              (if (= dzielnik 0)
                                                  #f
                                                  (let ([new-l (/ (complex-re pom) dzielnik)]
                                                        [new-r (/ (complex-im pom) dzielnik)])
                                                  (complex new-l new-r))))]))]))
                                 

(define (parse q)
  (cond [(number? q) (complex q 0)]
        [(eq? q 'i) (complex 0 1)]
        [(and (list? q)
              (eq? (length q) 3)
              (symbol? (first q)))
         (binop (first q) (parse (second q)) (parse (third q)))]))

