"""
648. Replace Words

In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"

"""

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        new_sentence = ""
        hash_map = dict()

        for word in sentence.split():
            non_derivative = True
            for root in dictionary:
                if word.startswith(root):
                    non_derivative = False
                    if word in hash_map:
                        if len(hash_map[word]) > len(root):
                            hash_map[word] = root
                    else:
                        hash_map[word] = root
            if non_derivative:
                if not new_sentence:
                    new_sentence = word
                else:
                    new_sentence = "%s %s" % (new_sentence, word)
            else:
                if not new_sentence:
                    new_sentence = hash_map[word]
                else:
                    new_sentence = "%s %s" % (new_sentence, hash_map[word])
        return new_sentence


# test case 1
# -----------
# sentence = "the cattle was rattled by the battery"
# dictionary = ["cat","bat","rat"]

# test case 2
# ----------
# sentence = "the cattle was rattled by the battery"
# dictionary = ["catt", "cat","bat","rat"]

# test case 3
# -----------
# sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
# dictionary = ["a", "aa", "aaa", "aaaa"]
