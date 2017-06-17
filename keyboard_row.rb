# @param {String[]} words
# @return {String[]}
# https://leetcode.com/problems/keyboard-row/#/description
def find_words(words)
  row1 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
  row2 = ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
  row3 = ["Z", "X", "C", "V", "B", "N", "M"]
  rdict1 = rdict2 = rdict3 = {}
  row1.each{|l| rdict1[l] = 1}
  row2.each{|l| rdict2[l] = 2}
  row3.each{|l| rdict3[l] = 3}

  result_set = []
  words.each do |word|
    last_row_idx = -1
    word.each_char do |c|
      c.upcase!
      cur_row_idx = rdict1[c] || rdict2[c] || rdict3[c]
      if last_row_idx < 0
        last_row_idx = cur_row_idx
      else
        if last_row_idx != cur_row_idx
          last_row_idx = 0
          break
        end
      end
    end

    result_set << word if last_row_idx != 0
  end

  result_set 
end}}
