# https://leetcode.com/problems/ransom-note/description/
# @param {String} ransom_note
# @param {String} magazine
# @return {Boolean}
def can_construct(ransom_note, magazine)
  base = {}
  base.default = 0

  magazine.each_char do |c|
    base[c] += 1
  end

  ransom_note.each_char do |c|
    return false if base[c] == 0
    base[c] -= 1
  end

  true
end

p can_construct("abb", "aab")
