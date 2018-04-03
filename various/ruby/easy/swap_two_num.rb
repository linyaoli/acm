def swap(a, b)
  a = a^b
  b = b^a
  a = a^b

  return a, b
end

p swap(11, 22)
