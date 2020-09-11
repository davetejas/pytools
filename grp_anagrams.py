
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Assume lowercase letters at this time.

# Dup letter possible


# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat", “atte”, “teat”]
# Output: [
# ["bat"],
# ["nat","tan"],
# ["ate","eat","tea"],
# [“atte”, “teat”]
# ]

# Example 2:
# Input: strs = ["a"]
# Output: [["a"]]


'''
Approach

1st : group all words of same size togather -> wordBuckets
2nd : create a string key size 26 (for all small char) with position of letter in alphabet as index
3rd : iterate through all words can create above key add to cmap (character map)
4th : any anagram would create same key, add those words to list in value of map
5th : compile and return the list
''' 

class Solve:
    def __init__(self):
        self.input = {}
        self.output = []
        
    # builds buckets for words with same len
    def wordBuckets(self, book: list) -> list:
        for w in book:
            if len(w) in self.input.keys():
                self.input[len(w)].append(w)
            else:
                self.input[len(w)] = [w]
                
    def groupAnagram(self, words, sz):
        self.wmap = {}
        for w in words:
            cmap = '0' * 26 # 26 char of lower case
            for idx in range(sz):
                index = ord(w[idx]) - ord('a')
                cmap = cmap[:index] + '1' + cmap[index+1:]
                                
            if cmap in self.wmap.keys():
                self.wmap[cmap].append(w)
            else:
                self.wmap[cmap] = [w]
        
        #print(self.wmap)
        result = []
        for k in self.wmap.keys():
            result.append(self.wmap[k])
            
        # print(result)
        return result
    
    def outcome(self, s):
        self.wordBuckets(s)
        for length in self.input.keys():
            res = self.groupAnagram(self.input[length], length)
            self.output.append(res)
            
        print(self.output)
    
strs = ["eat","tea","tan","ate","nat","bat", "teal", "tale"]
r = Solve()

r.outcome(strs)
                
