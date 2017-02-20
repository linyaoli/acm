# Given an integer, write a function to determine if it is a power of two.
# @param {Integer} n
# @return {Boolean}
def is_power_of_two(n)
   while n > 1
        if [2, 4, 6, 8].include?(n % 10)
            n /= 2
        else
            return false
        end
   end
   return false if n != 1
   return true
end
