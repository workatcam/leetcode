def counts(string):
    counter = {}
    for i in string:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    return counter

class Solution:
    def isAnagram(s1,s2):
        if counts(s1) == counts(s2): #what is the time complexity
            return True
        else:
            return False
