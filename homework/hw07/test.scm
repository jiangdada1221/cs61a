(define (contains? s v)
    (if (empty? s) #f
    (if (= v (car s))
      #t
      (contains? (cdr s) v)
    )
    )
    )
(define (empty? s) (null? s))
