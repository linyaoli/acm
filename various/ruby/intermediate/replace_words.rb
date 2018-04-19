# https://leetcode.com/problems/replace-words/description/
# @param {String[]} dict
# @param {String} sentence
# @return {String}

def replace_words(dict, sentence)
  sorted_dict = dict.sort_by(&:length)
  words = sentence.split(" ")
  res = []

  # words that has been replaced.
  dp = Array.new(words.size, false)

  words.each_with_index do |word, i|
    sorted_dict.each do |dw|
      break if dp[i] == true

      n = dw.length
      if n < word.length && word[0..n-1] == dw && dp[i] == false
        dp[i] = true
        res << dw
      end
    end

    res << word if dp[i] == false
  end

  res.join(" ")
end

# another solution if Trie tree.

p replace_words(["cat", "bat", "rat"], "the cattle was rattled by the battery")
