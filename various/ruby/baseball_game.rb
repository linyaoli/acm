# You're now a baseball game point recorder.
# 
# Given a list of strings, each string can be one of the 4 following types:
# 
# Integer (one round's score): Directly represents the number of points you get in this round.
# "+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
# "D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
# "C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
# Each round's operation is permanent and could have an impact on the round before and the round after.
# 
# You need to return the sum of the points you could get in all the rounds.
# https://leetcode.com/problems/baseball-game/description/ 

# @param {String[]} ops
# @return {Integer}
def cal_points(ops)
  total = 0
  pre = []
  # Remove all invalid ones
  after_ops = []
  while ops.size > 0
    val = ops.shift
    if val == "C"
      after_ops.pop
    else
      after_ops << val
    end
  end

  after_ops.each do |op|
    case op
    when "D"
      pre << pre[-1].to_i * 2
    when "+"
      pre <<  pre[-1].to_i + pre[-2].to_i
    else
      pre << op.to_i
    end
  end

  pre.sum 
end
p cal_points(["5","2","C","D","+"])
p cal_points(["5","-2","4","C","D","9","+","+"])
