# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

def groupAnagrams(strs):
        output_dict = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))

            if sorted_string not in output_dict:
                output_dict[sorted_string] = []
            
            output_dict[sorted_string].append(string)

        return list(output_dict.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

def findWords(words):
    
        set1 = {'q','w','e','r','t','y','u','i','o','p'}
        set2 = {'a','s','d','f','g','h','j','k','l'}
        set3 = {'z','x','c','v','b','n','m'}
        
        res = []
        for i in words:
            wordset = set(i.lower())
            if wordset.issubset(set1) or wordset.issubset(set2) or wordset.issubset(set3):
                res.append(i)
        return res

print(findWords(["Hello","Alaska","Dad","Peace"]))