;; Extra Scheme Questions ;;

(define (empty? s) (null? s))
; Q5
(define lst
  'YOUR-CODE-HERE
)

; Q6
(define (composed f g)
  (lambda (x) (f (g x)))
)

; Q7
(define (remove item lst)
   (define (equal? x) (= x item))
  (if (empty? lst)
        nil
        (filter equal? lst)
  )
)
(define (equal? item x)
  (= item x)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (no-repeats s)
      (if (empty? s)
      nil
      (if (not (isin? (car s) (cdr s)))
      (cons (car s) (no-repeats (cdr s)))
      (no-repeats (cdr s))
      )
      )
)
(define (isin? x lst)
    (if (empty? lst)
      #f
      (if (= (car lst) x)
        #t
        (isin? x (cdr lst))
      )
    )
)
; Q9
(define (substitute s old new)
  (if (empty? s) nil
  (if (pair? (car s))
  (append '(substitute (car s) old new) '(substitute (cdr s) old new))
  (if (equal? (car s) old)
     (append '(new) '(substitute (cdr s) old new))
     (append '(car s)  '(substitute (cdr s) old new))
  )
  )
)
)

; Q10
(define (sub-all s olds news)
  'YOUR-CODE-HERE
)
