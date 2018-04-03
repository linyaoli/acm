# https://leetcode.com/problems/rotate-string/description/
# @param {String} a
# @param {String} b
# @return {Boolean}
def rotate_string(a, b)
  return true if a == b
  b.split("").each_with_index do |c, i|
    if b[i+1..-1] + b[0..i] == a
      return true
    end
  end

  false
end

p rotate_string('abcde', 'cdeab')
p rotate_string('abcde', 'abced')
p rotate_string('abcde', 'abcde')
p rotate_string('', '')
