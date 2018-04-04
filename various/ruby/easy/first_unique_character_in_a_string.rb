# https://leetcode.com/problems/first-unique-character-in-a-string/description/
# @param {String} s
# @return {Integer}
def first_uniq_char(s)
  map = Hash.new 
  map.default = 0
  s.each_char do |c|
    map[c] += 1
  end

  s.split("").each_with_index do |c, i|
    return i if map[c] == 1
  end

  return -1
end

p first_uniq_char("ready")
p first_uniq_char("readyoready")
