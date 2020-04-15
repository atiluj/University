#lang racket
;; lista 3 zadanie 9 Sortowanie szybkie (quicksort)

(provide partition quicksort)

(define (partition n xs) ;; n-piwot  ;;xs-lista
  (define (aux1 temp iter) ;; temp-list elementów mniejsza od pivot
    (if (= iter (length xs))
        temp
        (if (<= (list-ref xs iter) n) ;;lis-ref <lista> <id>  - zwraca <id> element <lista>
             (aux1 (append temp (list (list-ref xs iter))) (+ 1 iter)) ;;gdy element listy jest mniejszy od pivota dodajemy go do temp
            (aux1 temp (+ 1 iter))))) ;;jeśli nie to idziemy dalej
  (define (aux2 temp iter)
    (if (= iter (length xs))
        temp
        (if (> (list-ref xs iter) n)
            (aux2 (append temp (list (list-ref xs iter))) (+ 1 iter)) ;;gdy element listy jest większy od pivota dodajemy go do temp
            (aux2 temp (+ 1 iter))))) ;;jeśi nie to idziemy dalej
  (cons (aux1 `() 0) (aux2 `() 0))) ;;`() to (list)  ;; wywołanie

(define (quicksort lista) ;;funkcja quicksort, która za argument przyjmuje liste
  (if (< (length lista) 2) ;; jeśli lista ma mniej niz 2 alementy to wypisz liste
      lista
      (append (quicksort (car (partition (car lista) (cdr lista)))) ;;zwróci (aux1 `() 0)
              (list (car lista)) ;;pivot ;;car(lista)-pierwszy element
              (quicksort (cdr (partition (car lista) (cdr lista))))))) ;;zwórci (aux2 `() 0)


;;testy
"test procedury (partition n xs) rodzielajacej liste xs na dwie listy (elementy listy xs <= pivot)(elementy listy xs > pivot(n))"
(partition 3 (list 1 2 -0.89 1/13 69 9 0 4.5 0.19))
"-------------------------------------------"
"testy procedury (quicksort xs)"    ;;powinniśmy spodziewać sie posortowanych rosnąco ciągów liczb
(quicksort (list))
(quicksort (list 9 7 6.5 4/3 0 -7 -7.6))
(quicksort (list 1 5 3 8 4 7 6))
(quicksort (list 6 8 0 3 4 3 1))
(quicksort (list 1 2 -0.89 1/13 69 9 0 1 1 4.5 0.19))
(quicksort (list -1 2 3 4 5 5.5 12/2))

