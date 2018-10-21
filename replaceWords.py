"""
Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
"""

def find_word(word, d):
        for i in range(1, min(len(word), 100)):
            if word[:i] in d: return word[:i]
        return word
        
def replaceWords(d, sentence):
    d, words = set(d),  sentence.split()
    return " ".join([find_word(word, d) for word in words])


dict = ["cat", "bat", "rat"]     
sentence = "the cattle was rattled by the battery"
print(replaceWords(dict,sentence))