(define-macro (list-of map-expr for var in lst if filter-expr)
(list 'filter (list 'lambda (list var) filter-expr)  lst)
)
