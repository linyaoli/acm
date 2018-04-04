# @param {Integer} n
# @return {Integer}
def num_squares(n)
  @dp = Array.new(n+1, 10000)
  @dp[0] = 0
  for i in 0..n
    j = 1
    while i + j * j <= n
      @dp[i+j*j] = [@dp[i+j*j], @dp[i]+1].min
      j += 1
    end
  end

  @dp[n]
end

=begin math/fast way, no shit.
require 'prime'

def num_squares(n)
  n /= 4 while n % 4 == 0
    return 4 if n % 8 == 7
      return 3 if n.prime_division.any? { |p, e| p % 4 == 3 && e.odd? }
        (n**0.5).to_i**2 == n ? 1 : 2
        end
=end
