# https://leetcode.com/problems/custom-sort-string/description/
# @param {String} s
# @param {String} t
# @return {String}
def custom_sort_string(s, t)
  order_map = {}
  s.split("").each_with_index do |c, i|
    order_map[c] = i
  end

  target_map = {}
  t.split("").each_with_index do |c, i|
    if order_map.keys.include? c
      target_map[order_map[c]] = c
    else
      target_map[-1] = target_map[-1].to_s + c 
    end
  end

  result = Array.new(s.size){Array.new(0)}
  t.each_char do |c|
    result[order_map[c]] << c unless order_map[c].nil?
  end

  result.join + target_map[-1].to_s
end

p custom_sort_string("kqep", "pekeq")
