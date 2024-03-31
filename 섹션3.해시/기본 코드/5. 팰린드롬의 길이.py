from collections import Counter

def solution(s):
    freq = Counter(s)
    odd = 0
    length = 0

    for key in freq:
        if freq[key] % 2 != 0:
            odd += 1 # 검사용
            length += freq[key] - 1
        else: 
            length += freq[key]

    if odd >= 1:
        length += 1 # 중간에 놓을 문자

    return length
    
                   
print(solution("abcbbbccaaeee"), end=" ")
print(solution("aabbccddee"), end=" ")
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"), end=" ")
print(solution("aabcefagcefbcabbcc"), end=" ")
print(solution("abcbbbccaa"))
'''
11 10 41 17 9
'''