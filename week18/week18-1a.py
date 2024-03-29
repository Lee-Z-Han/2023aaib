class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s) # 字串的長度
        a = s[:n//2] # 前半段
        b = s[n//2:] # 後半段
        motherA = 0 # a的母音有幾個
        motherB = 0 # a的母音有幾個
        for c in a: # 在a裡面的每一個字母 c 逐一檢查
            if c=='a' or c=='e' or c=='i' or c=='o' or c=='u': # 小寫的母音
                motherA += 1
            if c=='A' or c=='E' or c=='I' or c=='O' or c=='U': # 大寫的母音
                motherA += 1
        for c in b: # 在b裡面的每一個字母 c 逐一檢查
            if c=='a' or c=='e' or c=='i' or c=='o' or c=='u': # 小寫的母音
                motherB += 1
            if c=='A' or c=='E' or c=='I' or c=='O' or c=='U': # 大寫的母音
                motherB += 1
        if motherA == motherB: return True
        else: return False