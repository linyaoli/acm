# https://leetcode.com/problems/jewels-and-stones/description/
#

# @param {String} j
# @param {String} s
# @return {Integer}
def num_jewels_in_stones(j, s)
  jewel_list = {} 
  j.each_char do |c|
    jewel_list[c] = 1
  end

  count = 0
  s.each_char do |c|
    if !jewel_list[c].nil?
      count += 1
    end
  end

  count
end

puts num_jewels_in_stones("aA", "zzz")
