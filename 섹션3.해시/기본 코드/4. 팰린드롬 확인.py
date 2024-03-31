from collections import Counter

def solution(s):
    answer = False
    frequency = Counter(s)
    odd = 0

    for key in frequency:
        if frequency[key] % 2 != 0: # 홀수
            odd += 1

    if odd >= 2: return False
    else: return True
                      
print(solution("abacbaa"))
print(solution("abaaceeffkckbaa"))
print(solution("abcabbcc"))
print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
print(solution("aabcefagcefbcabbcc"))
'''
True
True
False
True
False
'''
'''
a가 짝수인가?
b가 짝수인가? ...
회문의 조건: 홀수인 키가 2 이상이면 False, 아니면 True 반환
'''