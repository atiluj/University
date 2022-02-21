;; ---- zad 21 ------ Prosty typechecker
;; na podstawie kodu z listy 13 zad 5 z zajęć Pana Tomasz Draba
;; zmieniony/dodany kod został oznaczony symbolem  ;;<------------- ZAD 21

#lang typed/racket
(provide parse typecheck)
; --------- ;
; Wyrazenia ;
; --------- ;

(struct const    ([val : Number])      #:transparent)
(struct const-bool ([val : Symbol]) #:transparent)                             ;;<---- ZAD 21
(struct binop    ([op : Symbol] [l : Expr] [r : Expr])   #:transparent)
(struct binop-cmp ([op : Symbol] [l : Expr] [r : Expr]) #:transparent)         ;;<---- ZAD 21
(struct binop-log ([op : Symbol] [l : Expr] [r : Expr]) #:transparent)         ;;<---- ZAD 21
(struct not-log ([op : Symbol] [x : Expr]) #:transparent)                      ;;<---- ZAD 21
(struct var-expr ([id : Symbol])       #:transparent)
(struct let-expr ([id : Symbol] [e1 : Expr] [e2 : Expr]) #:transparent)
(struct if-expr ([expr : Expr] [e1 : Expr] [e2 : Expr]) #:transparent)         ;;<---- ZAD 21
(define-type  EType (U 'real 'boolean))

(define-type Expr (U const const-bool if-expr binop-cmp binop binop-log not-log var-expr let-expr))
(define-type (LetConcr X) (List 'let (List Symbol X) X))
(define-type (BinConcr X) (List (U '+ '* '- '/ '%) X X))
(define-type (SymbolLogConcr X) (List (U '&& '|| '^ 'and 'or 'xor) X X))    ;;<---- ZAD 21
(define-type (SymbolNotConcr X) (List (U '! 'not '¬) X))                    ;;<---- ZAD 21
(define-type (SymbolCmpConcr X) (List (U '< '> '<= '>= '= '== '!= '<>) X X))   ;;<---- ZAD 21
(define-type (IfConcr X) (List 'if X X X))     ;;<------ ZAD 21
(define-type Concr (U                          ;;<------ ZAD 21
                    Number
                    Real
                    Symbol
                    Boolean
                    (LetConcr Concr)
                    (BinConcr Concr)
                    (SymbolCmpConcr Concr)   
                    (SymbolNotConcr Concr)   
                    (SymbolLogConcr Concr)
                    (IfConcr Concr)
                    ))

; Środowisko
(struct environ ([xs : (Listof (Pairof Symbol EType))]) #:transparent) ;;<---- ZAD 21
;;(: env-empty environ)                                                ;;<---- ZAD 21
(define env-empty (environ null))
(: env-add (-> Symbol EType environ environ))                          ;;<---- ZAD 21
(define (env-add x v env)
  (environ (cons (cons x v) (environ-xs env))))
(: env-lookup (-> Symbol environ EType))                               ;;<---- ZAD 21
(define (env-lookup x env)
  (: assoc-lookup (-> (Listof (Pairof Symbol EType)) EType))           ;;<---- ZAD 21
  (define (assoc-lookup xs)
    (cond [(null? xs) (error "Unknown identifier" x)]
          [(eq? x (car (car xs))) (cdr (car xs))]
          [else (assoc-lookup (cdr xs))]))
  (assoc-lookup (environ-xs env)))


; Typecheck   <------------------------------------------------- ZAD 21
(: typecheck (-> Expr (U EType #f)))
(define (typecheck q)
  (: typecheck-env (-> Expr environ (U EType #f)))
  (define (typecheck-env q env)
    (match q
      [(let-expr id e1 e2) (let ((te1 (typecheck-env e1 env)))
                             (if (eq? #f te1)
                                 #f
                                 (typecheck-env e2 (env-add id te1 env))))]
      [(binop op l r)(if (and
                          (eq? (typecheck-env l env) 'real)
                          (eq? (typecheck-env r env) 'real)) 'real #f)]
      [(var-expr id) (cond
                       [(eq? 'real (env-lookup id env)) 'real]
                       [(eq? 'boolean (env-lookup id env)) 'boolean]
                       [else #f])]
      [(const val) 'real]
      [(not-log op q) 'boolean]
      [(const-bool val) 'boolean]
      [(if-expr eb et ef) (if (eq? (typecheck-env eb env) 'boolean)
                              (if (eq? (typecheck-env et env) (typecheck-env ef env)) (typecheck-env et env) #f)
                              #f)]      
      [(binop-cmp op l r) (if (and (eq? 'real (typecheck-env l env)) (eq? 'real (typecheck-env r env))) 'boolean #f)]
      [(binop-log op l r) (if (and (eq? 'boolean (typecheck-env l env)) (eq? 'boolean (typecheck-env r env))) 'boolean #f)]
      [_ #f]
      ))
  (typecheck-env q env-empty))

; Parser
(: parse (-> Concr Expr))
(define (parse q)
  (cond
    [(number? q) (const q)]
    [(member q (list 'true 'false))                          ;;<---- ZAD 21
     (const-bool q)]                                         ;;<---- ZAD 21
    [(symbol? q) (var-expr q)]
    [(and (list? q) (eq? (length q) 4) (eq? (first q) 'if))  ;;<---- ZAD 21
     (if-expr (parse (second q))                             ;;<---- ZAD 21
              (parse (third q))                              ;;<---- ZAD 21
              (parse (fourth q)))]                           ;;<---- ZAD 21
    [(and (list? q) (eq? (length q) 3) (eq? (first q) 'let)) ;;<---- ZAD 21
     (let-expr (first (second q))
               (parse (second (second q)))
               (parse (third q)))]
    [(and (list? q) (eq? (length q) 3) (symbol? (first q)) (member (first q) (list '& '&& '|| '^ 'and 'or 'xor))) ;;<---- ZAD 21
     (binop-log (first q)
                (parse (second q))
                (parse (third q)))]
    [(and (list? q) (eq? (length q) 3) (symbol? (first q)) (member (first q) (list '< '> '<= '>= '= '== '!= '<>))) ;;<---- ZAD 21
     (binop-cmp (first q)
                (parse (second q)) 
                (parse (third q)))]
    [(and (list? q) (eq? (length q) 2) (symbol? (first q)) (member (first q) (list 'not '¬ '!))) ;;<---- ZAD 21
     (not-log (first q)
                (parse (second q)))]
    [(and (list? q) (eq? (length q) 3) (symbol? (first q)) (member (first q) (list '+ '- '/ '* '%))) ;;<---- ZAD 21
     (binop (first q)
            (parse (second q))
            (parse (third q)))]
    [else (error "error")]))
