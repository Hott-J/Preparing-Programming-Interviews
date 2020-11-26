#라이브러리 없이 구현

s="안녕하세요"
a=""
for i in range(len(s)-1,-1,-1):
    a+=s[i]
print(a)

#효율적인가?

s = 'abcde'
print(s[::-1])  # 'edcba'

s = 'abcde'
print(s[3:0:-1])  # dcb

s = 'abcde'
print(s[3::-1])  # dcba

#리스트나 튜플에도 적용

l = ['a', 'b', 'c', 'd', 'e']
print(l[::-1])  # ['e', 'd', 'c', 'b', 'a']

t = ('a', 'b', 'c', 'd', 'e')
print(t[::-1])  # ('e', 'd', 'c', 'b', 'a')