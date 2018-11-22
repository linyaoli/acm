# 0 -> [0]
# 1 -> [4, 2]
# 2 -> [7, 3]
# ...
#
# Find unions.

@f = [
  [0],
  [4,2],
  [7,3],
  [8],
  [8],
  [3],
  [6],
  [6,8],
  [8],
  [8,6]
]

@parents = [nil] * 10

def find(i, origin)
  if @parents[i].nil?
    @parents[i] = origin

    @f[i].each do |friend|
      if friend != i
        @parents[i] = find(friend, origin) || @parents[i]
      end
    end
    return nil
  else
    return @parents[i]
  end
end

(0..9).each do |i|
  find(i, i)
end

p @parents

res = {}
@parents.each_with_index do |i, j|
  if res[i]
    res[i] += @f[j] << j
  else
    res[i] = @f[j] << j
  end

  res[i].uniq!
end

p res
