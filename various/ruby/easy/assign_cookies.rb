# https://leetcode.com/problems/assign-cookies/description/
# @param {Integer[]} g
# @param {Integer[]} s
# @return {Integer}
def find_content_children(g, s)
  # Stop using god damn single-letter variables !
  children = g.sort
  cookies = s.sort

  cookie_index = 0
  child_index = 0

  while cookie_index < cookies.size && child_index < children.size
    child_index += 1 if children[child_index] <= cookies[cookie_index]
    cookie_index += 1
  end

  child_index
end

p find_content_children([1,2,3], [1,1])
p find_content_children([1,2], [1,2,3])
