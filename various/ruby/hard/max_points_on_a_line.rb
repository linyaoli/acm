# https://leetcode.com/problems/max-points-on-a-line/
# Definition for a point.
class Point
    attr_accessor :x, :y
    def initialize(x=0, y=0)
        @x = x
        @y = y
    end
end

# @param {Point[]} points
# @return {Integer}
def max_points(points)
  res = 0
  points.each do |p1|
    dup = 1
    gradient_map = {}
    gradient_map.default = 0

    points.each do |p2|
      gradient = 0
      next if p1 == p2
      if p1.x == p2.x && p1.y == p2.y
        dup += 1
        next
      elsif p1.x == p2.x
        gradient = 999.0
      else
        gradient = (p2.y - p1.y) * 1.0 / (p2.x - p1.x)
      end

      gradient_map[gradient] += 1
    end

    gradient_map.each do |k, v|
      res = [res, v + dup].max
    end
  end

  res
end

pts = []
pts << Point.new(84, 250)
pts << Point.new(0, 0)
pts << Point.new(1, 0)
pts << Point.new(0, -70)
pts << Point.new(0, -70)
pts << Point.new(1, -1)
pts << Point.new(21, 10)
pts << Point.new(42, 90)
pts << Point.new(-42, -230)

p max_points(pts)
