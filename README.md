
```python
%timeit sum(set_.stream)
2.7 ms ± 127 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
 
%timeit set_.Sum()
2.67 ms ± 137 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# 
%timeit sum(set_.stream)
# 2.5 ms ± 67.3 µs per loop (mean ± std. dev. of 7 runs, 100 loops each) 
%timeit set_.Sum()
2.55 ms ± 49.1 µs per loop (mean ± std. dev. of 7 runs, 100 loops each) 
```