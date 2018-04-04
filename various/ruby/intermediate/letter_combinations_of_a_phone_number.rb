def letter_combinations(digits)
  result = []
  generator(0, digits.split(""), [], result)
  result
end

def generator(i, digits, solution, result)
  if solution.size == digits.size
    result << solution.join
  else
    for j in i..digits.size-1
      letters = keyboard(digits[j]).split("")
      letters.each do |letter|
        solution << letter
        generator(j+1, digits, solution, result)
        solution.pop
      end
    end
  end
end

def keyboard(n)
  {
    "1" => "",
    "2" => "abc",
    "3" => "def",
    "4" => "ghi",
    "5" => "jkl",
    "6" => "mno",
    "7" => "pqrs",
    "8" => "tuv",
    "9" => "wxyz",
    "0" =>  " "
  }[n]
end

p letter_combinations("23")
