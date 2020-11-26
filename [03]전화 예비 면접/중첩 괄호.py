#괄호가 제대로 중첩되었는지 판단

s="(())"
s1="()()"
s2="(()()"
s3=")("
flag=True
def solution(s):
    #flag=True
    cnt=0
    for i in range(len(s)):
        if s[i]=="(":
            cnt+=1
        else:
            cnt-=1
        if cnt<0:
            return False
    if cnt==0:
        return True
    return False

print(solution(s3))
