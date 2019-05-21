(define-macro (list-of map-expr for var in lst if filter-expr)
(define filtered (list 'filter (list 'lambda (list var) filter-expr)  lst))
(list 'map (list 'lambda (list var) map-expr) filtered)
)
