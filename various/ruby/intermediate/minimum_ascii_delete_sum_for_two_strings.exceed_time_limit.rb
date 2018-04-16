# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/
# @param {String} s1
# @param {String} s2
# @return {Integer}
def minimum_delete_sum(s1, s2)
  @s1 = s1
  @s2 = s2
  @res = 100000
  @sum = 0
  gen(0, 0, [], [])
  @res
end

def gen(i, j, word1, word2)
  if word1.join("") == word2.join("")
    @res = [@res, get_removed_ascii_sum(@s1, word1) + get_removed_ascii_sum(@s2, word2)].min
  else
    return
  end

  if i == @s1.size && j == @s2.size
  else
    for m in i..@s1.size-1
      word1 << @s1[m]
      gen(m+1, j, word1, word2)

      for n in j..@s2.size-1
        word2 << @s2[n]
        gen(m+1, n+1, word1, word2)
        word2.pop
      end

      word1.pop
    end
  end
end

def get_removed_ascii_sum(s, word)
  map = {}
  map.default = 0
  s.each_char { |c| map[c] += 1 }
  word.each { |c| map[c] -= 1 }

  sum = 0
  map.each {|k, v| sum += k.ord * v}

  sum
end

p minimum_delete_sum(
"igijekdtywibepwonjbwykkqmrgmtybwhwjiqudxmnniskqjfbkpcxukrablqmwjndlhblxflgehddrvwfacarwkcpmcfqnajqfxyqwiugztocqzuikamtvmbjrypfqvzqiwooewpzcpwhdejmuahqtukistxgfafrymoaodtluaexucnndlnpeszdfsvfofdylcicrrevjggasrgdhwdgjwcchyanodmzmuqeupnpnsmdkcfszznklqjhjqaboikughrnxxggbfyjriuvdsusvmhiaszicfa", 
"ikhuivqorirphlzqgcruwirpewbjgrjtugwpnkbrdfufjsmgzzjespzdcdjcoioaqybciofdzbdieegetnogoibbwfielwungehetanktjqjrddkrnsxvdmehaeyrpzxrxkhlepdgpwhgpnaatkzbxbnopecfkxoekcdntjyrmmvppcxcgquhomcsltiqzqzmkloomvfayxhawlyqxnsbyskjtzxiyrsaobbnjpgzmetpqvscyycutdkpjpzfokvi")
