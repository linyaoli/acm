# https://leetcode.com/problems/arithmetic-slices/description/
# @param {Integer[]} a
# @return {Integer}
def number_of_arithmetic_slices(a)
  res = 0
  dp = []

  for i in 0..a.size-1
    tmp = [0] * a.size
    tmp[i] = 1
    tmp[i+1] = 1 if i + 1 < a.size
    dp << tmp[0..-1]
  end

  # dp.each {|d| p d}

  for i in 0..a.size-3
    for j in i+2..a.size-1
      if dp[i][j-1] == 1
        if a[j] - a[j-1] == a[j-1] - a[j-2]
          dp[i][j] = 1
          res += 1
        end
      end
    end
  end


  # dp.each {|d| p d}

  res
end

def is_arithmetic(arr)
  d = arr[1] - arr[0]
  for i in 2..arr.size-1
    if arr[i] - arr[i-1] != d
      return false
    end
  end

  true
end

p number_of_arithmetic_slices([1,2,3,4, 5])
p number_of_arithmetic_slices([1, 1, 2, 5, 7])
