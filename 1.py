from itertools import combinations
l,k,ans=[1,2,3,4,5],[],0
for i in range(0,5): k.extend(combinations(l,i))
for i in k: 
    if sum(i)==9 : ans += 1 
print(ans)



    
