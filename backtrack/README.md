thoughts about the permutations and subsets problems in backtrack solutions.


permutations:

```python
  for j in xrange(i,n):
    swap(a[i],a[j])
    helper(i+1)
    swap(a[i],a[j])
```

subsets/powersets:


```python
  for j in xrange(i,n):
     push(a[j])
     helper(j+1)
     pop()
```
