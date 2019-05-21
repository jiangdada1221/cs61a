; Lab 13: Final Review

; Q3
(define (compose-all funcs)
(define (helper funcs argu)
(if (null? funcs) argu
(helper (cdr funcs) ((car funcs) argu))
)
)
(lambda (x) (helper funcs x))
)
