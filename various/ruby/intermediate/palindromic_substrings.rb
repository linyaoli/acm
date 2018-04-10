# https://leetcode.com/problems/palindromic-substrings/description/
# @param {String} s
# @return {Integer}
# so the following method would just exceed time limit, thats why
# DP is needed.
# def count_substrings(s)
#   res = 0
# 
#   for i in 0..s.size-1
#     for j in i..s.size-1
#       if is_palindromic(s[i..j])
#         res += 1
#       end
#     end
#   end
# 
#   res
# end
def count_substrings_extend(s)
  res = 0
  oned = [0] * s.size
  dp = []

  for i in 1..s.size
    tmp = oned[0..-1]
    tmp[i-1] = 1
    dp << tmp
  end

  for i in 0..s.size-1
    for j in i..s.size-1
      if i == j
        res += 1
      else
        if s[i] == s[j]
          if (dp[i+1][j-1] == 1 && i+1 < j-1)
            res += 1
            dp[i][j] = 1
          else
            if is_palindromic(s[i..j])
              res += 1
              dp[i][j] = 1
            end
          end
        end
      end
    end
  end

  # dp.each {|d| p d}

  res
end

def is_palindromic(str)
  chars = str.split("")
  for i in 0..chars.size/2 - 1
    if chars[i] != chars[chars.size - i - 1]
      return false
    end
  end
  
  return true
end

def count_substrings(s)
  res = 0
  oned = [0] * s.size
  dp = []

  for i in 1..s.size
    res += 1
    tmp = oned[0..-1]
    tmp[i-1] = 1
    dp << tmp
  end

  for i in 0..s.size-2
    if s[i] == s[i+1]
      dp[i][i+1] = 1
      res += 1
    end
  end

  for i in 2..s.size-1
    for j in 0..s.size-i-1
      m = i + j
      if dp[j+1][m-1] == 1 && s[j] == s[m]
        dp[j][m] = 1
        res += 1
      end
    end
  end

  res
end

p count_substrings("aaaaa")
