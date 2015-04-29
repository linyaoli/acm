class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        num=list(num)
        n=len(num)
        temp=[]
        if n==1: #when we only have one number
            temp.append(num)
            return temp
        else:
            for i in range(n):
                not_perm= num[0:i]+num[i+1:] # take out i from the list since i is fixed
                for j in self.permute(not_perm):  #use recursion here
                    temp.append(num[i:i+1]+ j) #here num[i:i+1] is fixed, j is all the permutations
            return temp
