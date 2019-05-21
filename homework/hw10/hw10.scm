(define (accumulate combiner start n term)
  (if (= n 0)
  start
  (accumulate combiner (combiner start (term n)) (- n 1) term)
  )
)

; this one fails, but this is a tail-recursion isn't it?
; if you look at this and figure out what 's wrong, please contact me by jiangdada12344321@163.com
(define (accumulate-tail combiner start n term)
(if (= n 0)
start
(accumulate combiner (combiner start (term n)) (- n 1) term)
)
)

(define (partial-sums stream)
  (define (helper record stream)
  (if (null? stream)
  nil
  (cons-stream (+ record (car stream)) (helper (+ record (car stream)) (cdr-stream stream))))
  )
  (helper 0 stream)
)

(define (rle s)
  (define (helper number count s)
  (if (null? s)
  (list count s)
  (if (not (= number (car s)))
  (list count s)
    (helper number (+ 1 count) (cdr-stream s)))   ))
  (if (null? s)
  nil
  (
  cons-stream (list (car s) (car (helper (car s) 0 s))) (rle (car(cdr (helper (car s) 0 s)))) ))
  )
; in fact helper function can return the result by its own
