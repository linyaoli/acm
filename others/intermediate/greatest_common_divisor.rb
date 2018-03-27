def gcd(m, n)
  m, n = n, m if m < n
  while n != 0
    m, n = n, m % n
  end

  m
end

puts gcd(10, 5)
puts gcd(10, 4)
puts gcd(11, 5)
puts gcd(14, 5)
puts gcd(21, 14)

# least common multiple
def lcm(m, n) 
  g = gcd(m, n)

  m / g * n / g * g
end

puts lcm(10, 5)
puts lcm(10, 4)
puts lcm(11, 5)
puts lcm(14, 5)
puts lcm(21, 14)
