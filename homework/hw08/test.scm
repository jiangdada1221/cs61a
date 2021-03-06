
(define (longest-increasing-subsequence lst)
        (define (helper lst prev)
                (cond ((null? lst) nil)
                      ((<= (car lst) prev) (helper (cdr lst) prev))
                      (else (define with-first (append (list (car lst)) (helper (cdr lst) (car lst))))
                            (define without-first (helper (cdr lst) prev))
                            (if (> (length with-first) (length without-first)) with-first without-first)
                      )
                )
        )
        (helper lst 0)
)
