class NumArray

=begin
    :type nums: Integer[]
=end
    def initialize(nums)
        @nums = nums
        (1..@nums.size-1).each do |x|
            @nums[x] += @nums[x-1]
        end
    end


=begin
    :type i: Integer
    :type j: Integer
    :rtype: Integer
=end
    def sum_range(i, j)
        return @nums[j] if i == 0
        @nums[j] - @nums[i - 1] 
    end


end

# Your NumArray object will be instantiated and called as such:
# obj = NumArray.new(nums)
# param_1 = obj.sum_range(i, j)
