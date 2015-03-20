"""
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
"""
# An elegant version of Finite automata machine, so so elegant.
# not from my knowledge.
class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        in_type = [
            0, #invalid
            1, #space
            2, #sign +, -
            3, #number
            4, #dot
            5, #'e', 'E'
        ]
        trans_table = [
        #0INVA,1SPA,2SIG,3DI,4DO,5E
            [-1,  0,  3,  1,  2, -1], #0 intialization without input or only space
            [-1,  8, -1,  1,  4,  5], #1 after numbers being input
            [-1, -1, -1,  4, -1, -1], #2 only dot being input, no num before
            [-1, -1, -1,  1,  2, -1], #3 + or - has been input
            [-1,  8, -1,  4, -1,  5], #4 has both num and dot before
            [-1, -1,  6,  7, -1, -1], #5 after 'e' or 'E' being input
            [-1, -1, -1,  7, -1, -1], #6 input sign after a 'e'
            [-1,  8, -1,  7, -1, -1], #7 input num after 'e'
            [-1,  8, -1, -1, -1, -1], #8 input space with a valid num before
        ]
        state = 0
        for c in s:
            input = 0 #invalid
            if c.isspace():
                input = 1
            elif c == '+' or c == '-':
                input = 2
            elif c.isdigit():
                input = 3
            elif c == '.':
                input = 4
            elif c == 'e' or c == 'E':
                input = 5
            state = trans_table[state][input]
            if state == -1:
                return False
        return state == 1 or state == 4 or state == 7 or state == 8


sol = Solution()
print sol.isNumber(".1")
print sol.isNumber("3. ")
print sol.isNumber(". 1")
print sol.isNumber("1 4")
print sol.isNumber("1 ")
print sol.isNumber(" .")
