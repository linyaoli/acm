# https://leetcode.com/problems/queue-reconstruction-by-height/description/
#
# @param {Integer[][]} people
# @return {Integer[][]}
def reconstruct_queue(people)
  map = {}
  height = []

  people.each_with_index do |p, i|
    if map[p[0]].nil?
      map[p[0]] = [[p[1], i]]
      height << p[0]
    else
      map[p[0]] << [p[1], i]
    end
  end

  height.sort!

  res = []
  height.reverse.each do |h|
    map[h].sort!
    map[h].each do |p|
      res.insert(p[0], people[p[1]])
    end
  end

  res.compact
end

p reconstruct_queue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
