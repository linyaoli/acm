# The is_bad_version API is already defined for you.
# @param {Integer} version
# @return {boolean} whether the version is bad
# def is_bad_version(version):
# https://leetcode.com/problems/first-bad-version/description/

# @param {Integer} n
# @return {Integer}
def first_bad_version(n)
  start = 1
  final = n

  while start <= final
    mid = (final - start) / 2 + start
    if is_bad_version(mid)
      final = mid - 1
    else
      start = mid + 1
    end
    return mid if is_bad_version(mid) && !is_bad_version(mid - 1)
  end

  -1
end
