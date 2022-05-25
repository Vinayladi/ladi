n = int(input())
ans = ''
s = list(map(int,list(input())))
lis = [[' ','0'],[',','@'],['A','B',"C",'a','b','c','2'],['D',"E",'F','d','e','f','3'],['G','H','I','g','h','i','4'],['J','K','L','j','k','l','5'],['M','N','O','m','n','o','6'],['P','Q','R','S','p','q','r','s','7'],['T','U','V','t','u','v','8'],['W','X','Y','Z','w','x','y','z','9']]
i,c = 1,1
p = s[0]
while i<len(s):
    if s[i]==p:
        c += 1
    else:
        ans += lis[p][c-1]
        p = s[i]
        c = 1
    i += 1
ans += lis[p][c-1]
print(ans)