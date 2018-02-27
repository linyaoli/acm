# @param {Integer[]} candies
# @return {Integer}
# @param {Integer[]} candies
# @return {Integer}
# https://leetcode.com/problems/distribute-candies/#/description
def distribute_candies(candies)
  sister_bag = {}
  (0..candies.size-1).each do |c|
    if sister_bag[candies[c]].nil?
      sister_bag[candies[c]] = 1 
    else
      sister_bag[candies[c]] += 1
    end
  end

  [sister_bag.size, candies.size/2].min
end}
