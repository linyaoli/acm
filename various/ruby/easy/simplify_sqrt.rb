def simplify_sqrt(num)
  factors = {}

  (num/2).downto(1) do |n|
    t_n = n * n
    next if t_n > num
    if num % t_n == 0
      num /= t_n
      factors[n] = factors[n].nil? ? 1 : factors[n] + 1 
    end
  end

  return factors, num
end

puts simplify_sqrt(3000)
