# @param {Integer} num
# @return {Boolean}
=begin
def check_perfect_number(num)
  res = divisors(num)
  p res
  if res.inject(0){|sum, x| sum + x} == num
    return true
  end

  false
end

def divisors(num)
  i = 1
  res = []
  while i <= num/2
    res << i if num % i == 0
    i += 1
  end
  res
end
=end
def check_perfect_number(num)
  sum = 0
  i = 1
  while(i <= Math.sqrt(num))
    if num % i == 0
      sum += i + num / i
    end
    i += 1
  end
  (sum - num) == num
end
