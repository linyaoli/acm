#
# Complete the group_strings function below.
#
def group_strings(strings)
    #
    # Write your code here.
    #
  group = {}

  strings.each do |str|
    if str.size >= 2
      if group[str[0..1]].nil?
        group[str[0..1]] = [str[2..-1]]
      else
        group[str[0..1]] << str[2..-1]
      end
    end
  end

  res = []

  group.each do |k, v|
    res << k + "[" + v.join(",") + "]" if v.size > 1
  end

  res
end

p group_strings(['abc', 'abcd', 'cd', 'cd', 'bcd'])
