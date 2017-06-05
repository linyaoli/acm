=begin
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
=end

class NumArray
  BUCKET_SIZE = 100
  def initialize(nums)
    @data = nums.flatten
    init_buckets
  end

  def update(i, val)
    if valid_range?(i)
      @buckets[i/BUCKET_SIZE] += val - @data[i]
      @data[i] = val
    end
  end

  def sum_range(i, j)
    return 0 if !valid_range?(i) || !valid_range?(j) || i > j
    b1 = i / BUCKET_SIZE
    b2 = j / BUCKET_SIZE
    result = 0
    if b1 - b2 > 1
      result = sum(@buckets[b1+1..b2-1]) + sum(@data[i..(b1+1)*BUCKET_SIZE-1]) + sum(@data[b2*BUCKET_SIZE..j])
    else
      result = sum(@data[i..j])
    end

    result
  end

  private

  def valid_range?(i)
    return false if i < 0 && i >= data.size
    return true
  end

  def init_buckets
    @buckets = []
    @data.each_slice(BUCKET_SIZE) do |slice|
      @buckets << sum(slice)
    end
  end

  def sum(nums)
    nums.inject(0){|sum, x| sum + x}
  end
end

na = NumArray.new([[0, 9, 5,7,3]])
puts na.sum_range(4, 4)
#na.update(2,4)
#na.sum_range(3,3)
