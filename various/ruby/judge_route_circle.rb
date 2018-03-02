# https://leetcode.com/problems/judge-route-circle/description/
#

# @param {String} moves
# @return {Boolean}
def judge_circle(moves)
  horizontal = 0
  vertical = 0
  moves.each_char do |c|
    case c
    when "U"
      vertical += 1
    when "D"
      vertical -= 1
    when "L"
      horizontal += 1
    when "R"
      horizontal -= 1
    else
      break
    end
  end

  return true if horizontal == 0 && vertical == 0
  false
end

puts judge_circle("LL")
