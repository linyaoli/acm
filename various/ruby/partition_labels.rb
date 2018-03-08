# https://leetcode.com/problems/partition-labels/description/:w
# @param {String} s
# @return {Integer[]}
def partition_labels(s)
  char_table  = []
  index_table = []
  result = []
  counter = 0
  s.split("").each_with_index do |c, i|
    index_table << counter
    if !char_table.include? c
      counter += 1
    else
      i = char_table.find_index c
      for j in i..char_table.size
        index_table[j] = index_table[i] 
      end
    end
    char_table << c
  end

  index_table[0..-1].uniq.each do |c|
    result << index_table[0..-1].count(c)
  end

  result
end

s = "ababcbacadefegdehijhklij"
p partition_labels(s)
s = "dccccbaabe"
p partition_labels(s)
