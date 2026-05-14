class WordCount:

    def isAnagram(self, s: str, t: str) :
        words1 = {}
        words2 = {}
        self.s=s
        self.t=t
        for index in self.s:
            # print(index.lower())
            val_exist = words1.get(index.lower())
            if val_exist==None:
                words1[index.lower()]=1
            else:
                words1[index.lower()]+=1
        for index in self.t:
            # print(index.lower())
            val_exist = words2.get(index.lower())
            if val_exist==None:
                words2[index.lower()]=1
            else:
                words2[index.lower()]+=1

        if words1==words2:
            return True
        else:
            return False

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
anagram_check = WordCount()
anagram_check.isAnagram("root","toor")
print(anagram_check.isAnagram2("root","toor"))