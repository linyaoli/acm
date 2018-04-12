# https://leetcode.com/problems/my-calendar-ii/description/
class MyCalendarTwo
  def initialize()
    @intersection = {}
    @intersection.default = 0
    @keys = [0]
  end

=begin
    :type start: Integer
    :type end: Integer
    :rtype: Boolean
=end
  def book(start, endy)
    @intersection[start] += 1
    @intersection[endy] -= 1

    insert(start)
    insert(endy)

    sum = 0
    @keys.each do |k|
      sum += @intersection[k]
      if sum >= 3
        @intersection[start] -= 1
        @intersection[endy] += 1
        return false
      end
    end

    true
  end

  def insert(val)
    if val > @keys[-1]
      @keys << val
    elsif val < @keys[0]
      @keys.insert(0, val)
    else
      for i in 0..@keys.size-1
        if @keys[i] < val && @keys[i+1] > val
          @keys.insert(i+1, val)
          break
        elsif @keys[i] == val
          break
        end
      end
    end
  end
end
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo.new()
# param_1 = obj.book(start, end)
#
my = MyCalendarTwo.new
runs = [[24,40],[43,50],[27,43],[5,21],[30,40],[14,29],[3,19],[3,14],[25,39],[6,19]]
runs.each do |arr|
  p my.book(arr[0], arr[1])
end
