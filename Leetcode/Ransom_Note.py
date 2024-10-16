def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(0, len(magazine)-len(ransomNote)):
            if ransomNote == magazine[i:len(ransomNote)]:
                return True
        if magazine.sort() == ransomNote.sort() or ransomNote.sort() in magazine.sort():
             return True
        return False
canConstruct("aabbccc", "aabb")