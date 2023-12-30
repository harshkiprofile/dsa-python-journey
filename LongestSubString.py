def lengthOfLongestSubstring( s: str) -> int:
        sub = []
        if len(sub) > 2:
            for i in range(len(s)):
                for j in range(i+1, len(s)):
                    if s[i] ==  s[j]:
                        sub.append(s[i:j])
                        break
        
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        if len(s) == 2:
            if s[0] != s[1]:
                return type(2)
        return len(max(sub))

print(lengthOfLongestSubstring("au"))
