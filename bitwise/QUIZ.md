### set a bit at nth position in the number

```c
num |= (1 << n)
```

the left shift `<<` and right shift `>>` should not be used for negative numbers.

### clear a bit at nth position

```c
num &= (~(1 << n))
```

### toggle a bit at nth position
Use xor.
```c
num ^= 1 << n
```

### Check if a bit is set
```c
num & (1 << n)
```

### invert every bit/ 1's complement
be careful with `~`, inverting a small number can result in a big one.
```c
~num
```

### 2's complement: 1's complement + 1
```c
~num + 1

```

### remove the lowest set bit
```c
num = num & (num - 1)
```

### get the lowest set bit
```c
num & (~num + 1)
```

### check if a number if odd
```c
num & 1
```
