(define (list-change total denoms)
  ; BEGIN PROBLEM 18
  (cond ((= total 0) '(()))
        ((null? (cdr denoms)) (list (repeat total (car denoms))))
        ((< total (car denoms)) (list-change total (cdr denoms)))
        (else (append (cons-all (car denoms) (list-change (- total (car denoms)) denoms))
                      (list-change total (cdr denoms)))    )            )
  )
  ; END PROBLEM 18
(define (repeat n x)
(if (= n 0) nil (cons x (repeat (- n 1) x))))

; the base is that : 2 branches : with first, without first
; with_first then total减去first 继续recursion
; without——first 继续recursion 最后将两者append
; 算法基础在于1可以组成任何数 and withfirst后迭代的部分 从大化小 到最后要么为0 要么demons中只剩下了1  1组成最后的数 
