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

### least significant bit (LSB)
the bit that determines whether the number is even or odd. Sometimes it also refers to the right-most bit.


### clear all bits from LSB to nth bit
```c
m = ~((1 << n+1) - 1)
x &= m

e.g.
x = 29 -> 00011101

1 << 4 -> 00010000
16 - 1 -> 00001111
~15    -> 11110000
x & m  -> 00010000
```

### most significant bit (MSB)
the left-most bit.

### clear all bits from MSB to nth bit
```c
m = (1 << n) - 1
x &= m
```

### count set bits in number
```c
while x > 0
  x &= x - 1
  n += 1
end
```

### find log base 2 of 32 bit number
```c
while x > 1
  x = x >> 1
  res += 1
end
```

### check if given 32 bit number if power of 2
```c
x & (x & x-1)

e.g.
32  -> 00100000
x-1 -> 00011111
x & x-1 -> 00000000 
```

### swap two numbers
```c
a ^= b
b ^= a
a ^= b
```
