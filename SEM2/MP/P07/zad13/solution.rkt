#lang racket
;;--- zad 13 ---  Zmienne żywe i martwe

(provide (struct-out const) (struct-out binop) (struct-out var-expr) (struct-out var-dead) (struct-out let-expr) find-dead-vars)   
; --------- ;
; Wyrazenia ;
; --------- ;
 
(struct const    (val)      #:transparent)
(struct binop    (op l r)   #:transparent)
(struct var-expr (id)       #:transparent)
(struct var-dead (id)       #:transparent)
(struct let-expr (id e1 e2) #:transparent)

(define (expr? e)
  (match e
    [(const n) (number? n)]
    [(binop op l r) (and (symbol? op) (expr? l) (expr? r))]
    [(var-expr x) (symbol? x)]
    [(var-dead x) (symbol? x)]
    [(let-expr x e1 e2) (and (symbol? x) (expr? e1) (expr? e2))]
    [_ false]))

(define (parse q)
  (cond
    [(number? q) (const q)]
    [(symbol? q) (var-expr q)]
    [(and (list? q) (eq? (length q) 3) (eq? (first q) 'let))
     (let-expr (first (second q))
               (parse (second (second q)))
               (parse (third q)))]
    [(and (list? q) (eq? (length q) 3) (symbol? (first q)))
     (binop (first q)
            (parse (second q))
            (parse (third q)))]))

; ---------------------------------- ;
; Wyszukaj ostatnie uzycie zmiennych ;
; ---------------------------------- ;
(define (val-count formula result) ;; liczy wystąpienia zmiennych w formule i zwraca liste par (zmienna . liczba wystąpień) 
    (match formula 
        [(const formula) result]
        [(let-expr id e1 e2) 
            (val-count e2 (append (list(cons id 0)) (val-count e1 result)))] ;;;!!!
        [(binop op l r)
            (val-count r (val-count l result))]
        [(var-expr v) 
            (add-occur '() result v)]))


(define (add-occur start result v) ;;dodaje jedno wystapienie zmiennej v do listy par (zmienna . liczba wystąpień) 
    (if (null? result)
        #f
        (if (eq? (caar result) v)
            (append start 
                    (list (cons v (+ (cdar result) 1)))
                    (cdr result))
            (add-occur (append start (list(car result))) (cdr result) v))))

(define (sub-occur result v) ;;odejmuje jedno wytąpieni zmiennej v (gdy dojdzie do 0 wiemy że jest to var-dead) 
  (define (sub start result v)
      (cond
        [(null? result) #f]
        [(eq? (caar result) v) (let ([n (- (cdar result) 1)])
                                 (if (= n 0)
                                     (append start (cdr result))
                                     (append start 
                                             (list (cons v (- (cdar result) 1)))
                                             (cdr result))))]
        [else (sub (append start (list(car result))) (cdr result) v)]))
    (sub '() result v))

(define (find-dead-vars wyr) ;;funkcja docelowa
  (define global (val-count wyr '()))
    (define (find e)
    (match e
        [(const e) (const e)]
        [(let-expr id e1 e2)
         (let-expr id 
         (find e1)
         (find e2))]
        [(binop op l r)
            (binop op (find l)
                      (find r))]
        [(var-expr v) 
            (let* ([n (length global)]
                   [new-result (sub-occur global v)])
              (set! global new-result)
              (if (= (length new-result) n)
                     (var-expr v)
                     (var-dead v)
                     ))]))
  (find wyr))
