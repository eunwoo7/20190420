# 1부터 100까지의 합을 구하는 도중에 최초로 100을 넘는 i와 그 합을 출력합니다

s=0
i=0

while i<=100:
    s+=i
    if(s>=1000):
        break
    i+=1

print("최초로 합이 1000을 넘는 i의 값과 그 합은",i,s)     

    
