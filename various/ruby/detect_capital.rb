# https://leetcode.com/problems/detect-capital/description/
# @param {String} word
# @return {Boolean}
def detect_capital_use(word)
  if word.upcase == word || word.downcase == word
    return true
  elsif word[1..-1].downcase == word[1..-1]
    return true
  else
    return false
  end
end

p detect_capital_use("USA")
p detect_capital_use("UsA")
p detect_capital_use("usa")
p detect_capital_use("Usa")
