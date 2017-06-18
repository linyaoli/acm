=begin
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
=end

# @param {String} s
# @return {String}
def reverse_words(s)
  res = []
  words = s.split(" ")
  words.each do |w|
    res << reverse_word(w)
  end
  res.join(" ")
end

def reverse_word(s)
  new_word = ""
  n = s.size
  for i in 0..n-1
    new_word += s[n - i - 1]
  end
  new_word
end
