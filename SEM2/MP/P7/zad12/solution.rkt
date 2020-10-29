#lang racket
;;--- zadanie 12 --- Zmienne wolne i związane

(provide (struct-out pos) (struct-out const) (struct-out binop) (struct-out var-expr) (struct-out let-expr) (struct-out environ) (struct-out var-free) (struct-out var-bound) expr-annot? annotate-expression)
;; ---------------
;; Jezyk wejsciowy
;; ---------------

(struct pos (file line col)     #:transparent)
(struct const    (val)          #:transparent)
(struct binop    (op l r)       #:transparent)
(struct var-expr (id)           #:transparent)
(struct let-expr (loc id e1 e2) #:transparent)

(define (expr? e)
  (match e
    [(const n)      (number? n)]
    [(binop op l r) (and (symbol? op) (expr? l) (expr? r))]
    [(var-expr x)   (symbol? x)]
    [(let-expr loc x e1 e2)
     (and (pos? loc) (symbol? x) (expr? e1) (expr? e2))]
    [_ false]))

(define (make-pos s)
  (pos (syntax-source s)
       (syntax-line   s)
       (syntax-column s)))

(define (parse e)
  (let ([r (syntax-e e)])
    (cond
      [(number? r) (const r)]
      [(symbol? r) (var-expr r)]
      [(and (list? r) (= 3 (length r)))
       (match (syntax-e (car r))
         ['let (let* ([e-def (syntax-e (second r))]
                      [x     (syntax-e (first e-def))])
                 (let-expr (make-pos (first e-def))
                           (if (symbol? x) x (error "parse error!"))
                           (parse (second e-def))
                           (parse (third r))))]
         [op   (binop op (parse (second r)) (parse (third r)))])]
      [else (error "parse error!")])))



; ---------- ;
; Srodowiska ; <-------- dopisane
; ---------- ;

(struct environ (xs) #:transparent)

(define env-empty (environ null))
                
(define (env-add para env)
  (environ (cons para (environ-xs env))))
  
(define (env-lookup id env)
  (define (assoc-lookup xs)
    (cond [(null? xs) #f] ;;"free var"
          [(eq? (caar xs) id) (cdar xs)]
          [else (assoc-lookup (cdr xs))]))
  (assoc-lookup (environ-xs env)))

;; ---------------
;; Jezyk wyjsciowy
;; ---------------

(struct var-free  (id)     #:transparent)
(struct var-bound (pos id) #:transparent)

(define (expr-annot? e) 
  (match e
    [(const n)         (number? n)]
    [(binop op l r)    (and (symbol? op) (expr-annot? l) (expr-annot? r))]
    [(var-free x)      (symbol? x)]
    [(var-bound loc x) (and (pos? loc) (symbol? x))]
    [(let-expr loc x e1 e2)
     (and (pos? loc) (symbol? x) (expr-annot? e1) (expr-annot? e2))]
    [_ false]))

(define (annotate-expression formula) ;;<----------------------- zad12 
  (define (aux formula env)
    (match formula
      [(const n) (const n)]
      [(binop op l r)
       (binop op (aux l env) (aux r env))]
      [(let-expr pos id e1 e2)
       (let-expr  pos
                  id
                  (aux e1 env)
                  (aux e2 (env-add (cons id pos) env)))]
      [(var-expr val)
       (let ([find-pos (env-lookup val env)])
         (if find-pos
         (var-bound find-pos val)
         (var-free val)))]
      [_ (error "error")]))
  (aux formula env-empty))
