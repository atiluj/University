#lang racket
;; --- zad 14 --- Dodanie do języka apply

(provide parse eval)

;;Zmodyfikowany program fun.rkt
;;zmodyfikowane oraz dodane fragmenty kody zostały oznaczone
;; <--------- ZAD14

; Do list.rkt dodajemy procedury
;
; Miejsca, ktore sie zmienily oznaczone sa przez !!!

; --------- ;
; Wyrazenia ;
; --------- ;

(struct const      (val)      #:transparent)
(struct binop      (op l r)   #:transparent)
(struct var-expr   (id)       #:transparent)
(struct let-expr   (id e1 e2) #:transparent)
(struct if-expr    (eb et ef) #:transparent)
(struct cons-expr  (e1 e2)    #:transparent)
(struct car-expr   (e)        #:transparent)
(struct cdr-expr   (e)        #:transparent)
(struct null-expr  ()         #:transparent)
(struct null?-expr (e)        #:transparent)
(struct app        (f e)      #:transparent) ; <------------------ !!!
(struct lam        (id e)     #:transparent) ; <------------------ !!!
(struct apply-expr (f lis)    #:transparent) ;; <--------- ZAD14

(define (list->pair lis)
  (cond [(null? lis) (null-expr) ]
       [(cons-expr (parse (car lis)) (list->pair (cdr lis)))]))

(define (how-much-lmd lambd)
    (match lambd 
        [(lam id e) (+ 1 (how-much-lmd e))]
        [_ 0]
    ))

(define (how-much-list x)
    (match x
        [(cons-expr e1 e2) (+ 1 (how-much-list e2))]
        [_ 0]
    )
)

(define (expr? e)
  (match e
    [(const n) (or (number? n) (boolean? n))]
    [(binop op l r) (and (symbol? op) (expr? l) (expr? r))]
    [(apply-expr f lis) (and (expr? f) (expr? lis))];; <--------- ZAD14
    [(var-expr x) (symbol? x)]
    [(let-expr x e1 e2)
     (and (symbol? x) (expr? e1) (expr? e2))]
    [(if-expr eb et ef)
     (and (expr? eb) (expr? et) (expr? ef))]
    [(cons-expr e1 e2) (and (expr? e1) (expr? e2))]
    [(car-expr e) (expr? e)]
    [(cdr-expr e) (expr? e)]
    [(null-expr) true]
    [(null?-expr e) (expr? e)]
    [(app f e) (and (expr? f) (expr? e))] ; <--------------------- !!!
    [(lam id e) (and (symbol? id) (expr? e))] ; <----------------- !!!
    [_ false]))

(define (parse q)
  (cond
    [(and (list? q) (eq? (first q) 'list))
    (list->pair (cdr q))]      
    [(number? q) (const q)]
    [(and (list? q) (eq? (length q) 3) (eq? (first q) 'apply))  ;; <--------- ZAD14
     (let ([check-app (apply-expr (parse (second q)) (parse (third q)))])  ;; <--------- ZAD14
                                                                 (if (expr? check-app)
                                                                     check-app
                                                                     (error "error")))]
    [(eq? q 'true)  (const true)]
    [(eq? q 'false) (const false)]
    [(eq? q 'null)  (null-expr)]
    [(symbol? q) (var-expr q)]
    [(and (list? q) (eq? (length q) 2) (eq? (first q) 'null?))
     (null?-expr (parse (second q)))]
    [(and (list? q) (eq? (length q) 3) (eq? (first q) 'cons))
     (cons-expr (parse (second q))
                (parse (third q)))]
    [(and (list? q) (eq? (length q) 2) (eq? (first q) 'car))
     (car-expr (parse (second q)))]
    [(and (list? q) (eq? (length q) 2) (eq? (first q) 'cdr))
     (cdr-expr (parse (second q)))]
    [(and (list? q) (eq? (length q) 3) (eq? (first q) 'let))
     (let-expr (first (second q))
               (parse (second (second q)))
               (parse (third q)))]
    [(and (list? q) (eq? (length q) 4) (eq? (first q) 'if))
     (if-expr (parse (second q))
              (parse (third q))
              (parse (fourth q)))]
    [(and (list? q) (eq? (length q) 3) (eq? (first q) 'lambda)) ; <!!!
     (parse-lam (second q) (third q))]
    [(and (list? q) (pair? q) (not (op->proc (car q)))) ; <------- !!!
     (parse-app q)]
    [(and (list? q) (eq? (length q) 3) (symbol? (first q)))
     (binop (first q)
            (parse (second q))
            (parse (third q)))]))

(define (parse-app q) ; <----------------------------------------- !!!
  (define (parse-app-accum q acc)
    (cond [(= 1 (length q)) (app acc (parse (car q)))]
          [else (parse-app-accum (cdr q) (app acc (parse (car q))))]))
  (parse-app-accum (cdr q) (parse (car q))))

(define (parse-lam pat e) ; <------------------------------------- !!!
  (cond [(= 1 (length pat))
         (lam (car pat) (parse e))]
        [else
         (lam (car pat) (parse-lam (cdr pat) e))]))

; ---------- ;
; Srodowiska ;
; ---------- ;

(struct environ (xs) #:transparent)

(define env-empty (environ null))
(define (env-add x v env)
  (environ (cons (cons x v) (environ-xs env))))
(define (env-lookup x env)
  (define (assoc-lookup xs)
    (cond [(null? xs) (error "Unknown identifier" x)]
          [(eq? x (car (car xs))) (cdr (car xs))]
          [else (assoc-lookup (cdr xs))]))
  (assoc-lookup (environ-xs env)))

; --------- ;
; Ewaluacja ;
; --------- ;

(struct clo (id e env)) ; <------------------------- !!!

(define (value? v)
  (or (number? v)
      (boolean? v)
      (and (pair? v) (value? (car v)) (value? (cdr v)))
      (null? v)
      (clo? v))) ; <---------------------------------------------- !!!

(define (new-apply func lis) ;; <--------- ZAD14
  (define (aux func lis)
    (if (null? lis)
            func
            (app (aux func (cdr lis)) (const (car lis)))))
    (if (> (how-much-lmd func) (length lis))
        (error "ERROR")
        (aux func lis)))
        

#|
(define (rev-lis lis new-lis)  ;; <--------- ZAD14
  (match lis
    [(cons-expr e1 e2) (rev-lis (cons-expr-e2 lis) (cons-expr (cons-expr-e1 lis) new-lis))]
    [(null-expr) new-lis]
    ))|#

(define (op->proc op)
  (match op ['+ +] ['- -] ['* *] ['/ /] ['% modulo]
    ['= =] ['> >] ['>= >=] ['< <] ['<= <=]
    ['and (lambda (x y) (and x y))]
    ['or  (lambda (x y) (or  x y))]
    [_ false])) ; <--------------------------------------- !!!

(define (eval-env e env)
  (match e
    [(const n) n]
    [(binop op l r) ((op->proc op) (eval-env l env)
                                   (eval-env r env))]
    [(apply-expr f lis) (eval-env (new-apply (eval-env f env) (reverse (eval-env lis env))) env)] ;; <--------- ZAD14
    [(let-expr x e1 e2)
     (eval-env e2 (env-add x (eval-env e1 env) env))]
    [(var-expr x) (env-lookup x env)]
    [(if-expr eb et ef) (if (eval-env eb env)
                            (eval-env et env)
                            (eval-env ef env))]
    [(cons-expr e1 e2) (cons (eval-env e1 env)
                             (eval-env e2 env))]
    [(car-expr e) (car (eval-env e env))]
    [(cdr-expr e) (cdr (eval-env e env))]
    [(null-expr) null]
    [(null?-expr e) (null? (eval-env e env))]
    [(lam x e) (clo x e env)] ; <--------------------------------- !!!
    [(app f e) ; <------------------------------------------------ !!!
     (let ([vf (match f
                 [(clo x body fun-env) f]
                 [_ (eval-env f env)])]
           [ve (eval-env e env)])
       (match vf [(clo x body fun-env)
                  (eval-env body (env-add x ve fun-env))]))]))

(define (eval e) (eval-env e env-empty))

#|
(eval (parse '(apply (lambda (x) x) (list 1))))
(eval (parse '(apply (lambda (x y) (lambda (z) (+ x (+ y z )))) (list 1 2 3))))

(eval (parse
'(apply (lambda (x y z) (+ x (+ y z)))
(list 1 2))))



(eval (parse '(apply (lambda (x y) (+ x y)) (cons 1 (cons 2 null)))))
(eval (parse '(apply (lambda (x y z) (+ x y)) (if false (list 1 2 3) (list 5 6 7))))) 
(eval (parse '(apply (if true (lambda (x y) (+ x y)) 4) (list 1 2)))) 
(eval (parse '(let [y 4] (let [y 2] (apply (lambda (x) x) (list y))))))
|#
