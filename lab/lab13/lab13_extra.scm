; Lab 13: Final Review - Optional Questions

; Q6
(define (nodots s)
(cond
((null? s) nil)
((number? s) (list s))    ; number 一定是cdr s 中获得到的
((pair? (car s)) (cons (nodots (car s)) (nodots (cdr s))))
(else (cons (car s) (nodots (cdr s))))
)
)

; Q7
(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond ((null? curr) #f)
          ((contains? seen-so-far curr) #t)
          (else (pair-tracker (cons curr seen-so-far) (cdr-stream curr))))
    )
  (pair-tracker nil s)
)

(define (contains? lst s)
  (if (null? lst)
  #f
  (if (eq? (car lst) s))
  #t
  (contains? (cdr lst) s)
  )
  )
  ; lst contains s?

; Q8   i hate macro !!!
(define-macro (switch expr cases)
              (let ((val (eval expr)))
                   (cons 'cond
                         (map (lambda (case)
                                      (cons (eq? val (car case)) (cdr case))
                              )
                              cases
                         )
                   )
              )
)
(define-macro (switch2 cases)
(car cases)
)
