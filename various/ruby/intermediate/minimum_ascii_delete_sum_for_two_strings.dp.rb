# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/
# @param {String} s1
# @param {String} s2
# @return {Integer}
def minimum_delete_sum(s1, s2)
  dp = Array.new(s1.size + 1) { Array.new(s2.size + 1, 0) }
  (0..s1.size-1).reverse_each do |i|
    dp[i][s2.size] = dp[i+1][s2.size] + s1[i].ord
  end

  (0..s2.size-1).reverse_each do |i|
    dp[s1.size][i] = dp[s1.size][i+1] + s2[i].ord
  end

  (0..s1.size-1).reverse_each do |i|
    (0..s2.size-1).reverse_each do |j|
      if s1[i] == s2[j]
        dp[i][j] = dp[i+1][j+1]
      else
        dp[i][j] = [dp[i+1][j] + s1[i].ord, dp[i][j+1] + s2[j].ord].min
      end
    end
  end

  dp[0][0]
end

p minimum_delete_sum(
"igijekdtywibepwonjbwykkqmrgmtybwhwjiqudxmnniskqjfbkpcxukrablqmwjndlhblxflgehddrvwfacarwkcpmcfqnajqfxyqwiugztocqzuikamtvmbjrypfqvzqiwooewpzcpwhdejmuahqtukistxgfafrymoaodtluaexucnndlnpeszdfsvfofdylcicrrevjggasrgdhwdgjwcchyanodmzmuqeupnpnsmdkcfszznklqjhjqaboikughrnxxggbfyjriuvdsusvmhiaszicfa", 
"ikhuivqorirphlzqgcruwirpewbjgrjtugwpnkbrdfufjsmgzzjespzdcdjcoioaqybciofdzbdieegetnogoibbwfielwungehetanktjqjrddkrnsxvdmehaeyrpzxrxkhlepdgpwhgpnaatkzbxbnopecfkxoekcdntjyrmmvppcxcgquhomcsltiqzqzmkloomvfayxhawlyqxnsbyskjtzxiyrsaobbnjpgzmetpqvscyycutdkpjpzfokvi")

=begin
explaination:

Let dp[i][j] be the answer to the problem for the strings s1[i:], s2[j:].

When one of the input strings is empty, the answer is the ASCII-sum of the other string. We can calculate this cumulatively using code like dp[i][s2.length()] = dp[i+1][s2.length()] + s1.codePointAt(i).

When s1[i] == s2[j], we have dp[i][j] = dp[i+1][j+1] as we can ignore these two characters.

When s1[i] != s2[j], we will have to delete at least one of them. We'll have dp[i][j] as the minimum of the answers after both deletion options.

The solutions presented will use bottom-up dynamic programming.

=end
