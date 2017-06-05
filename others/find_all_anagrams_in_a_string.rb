# @param {String} s
# @param {String} p
# @return {Integer[]}
def find_anagrams(s, p)
  result = []
  idx = indexer(p)
  _idx = indexer(s[0..p.size-1])
  e = s.size - p.size
  (0..e).each do |i|
    result << i if idx == _idx
    _idx = shifter(_idx, s[i], s[i+p.size])
  end

  result
end

def indexer(p)
  idx = {}
  p.each_char do |c|
    if idx[c].nil?
      idx[c] = 1
    else
      idx[c] += 1
    end
  end

  return idx
end

def shifter(idx, out, inn)
  idx[out] -= 1
  idx.delete(out) if idx[out] == 0

  if idx[inn].nil?
    idx[inn] = 1
  else
    idx[inn] += 1
  end
  idx
end

p find_anagrams("abab", "ab")
