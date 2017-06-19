# @param {String} pattern
# @param {String} str
# @return {Boolean}
def word_pattern(pattern, str)
  indexer_p2w = {}
  indexer_w2p = {}
  words = str.split
  return false if pattern.length != words.size
  words.each_with_index do |word, i|
    if indexer_p2w[pattern[i]].nil?
      indexer_p2w[pattern[i]] = word
    else
      if indexer_p2w[pattern[i]] != word
        return false
      end
    end

    if indexer_w2p[word].nil?
      indexer_w2p[word] = pattern[i]
    else
      if indexer_w2p[word] != pattern[i]
        return false
      end
    end
  end
  p indexer_p2w
  p indexer_w2p

  return true
end

puts word_pattern("abbaa", "dog cat cat dog dog")
