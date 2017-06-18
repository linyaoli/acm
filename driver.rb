def driver(gaps, start, endy)
  return 0 if start >= endy || start < 0 || endy > 100
  res = 0
  gaps.each do |gap|
    if start < gap[1] && start > gap[0]
      res += ([gap[1], endy].min - start) * 1.0 / gap[2]
    elsif start <= gap[0] && endy >= gap[1]
      res += (gap[1] - gap[0]) * 1.0 / gap[2]
    elsif endy > gap[0] && endy < gap[1]
      res += (endy - gap[0]) * 1.0 / gap[2]
      break
    end
  end
  res
end

gaps = [
  [0, 30, 10], #3
  [30, 40, 20], #0.5
  [40, 80, 20], #2
  [80, 100, 5], #4
]

puts sprintf('%.2f', driver(gaps, 41, 42))
puts sprintf('%.2f', driver(gaps, 40, 80))
puts sprintf('%.2f', driver(gaps, 35, 60))
puts sprintf('%.2f', driver(gaps, 0, 100))
puts sprintf('%.2f', driver(gaps, 0, 0))
puts sprintf('%.2f', driver(gaps, 100, 100))
puts sprintf('%.2f', driver(gaps, 20, 60))

# Time complexity O(n)
# Space complexity O(1)
