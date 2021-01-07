t= int(input())
while t:
         t=t-1
         n,m=input().split()
         l1=list(map(int,input().split()))
         l2=list(map(int,input().split()))
         i=0
         flag=True
         while sum(l1)<=sum(l2):
                  l1.sort()
                  l2.sort()
                  if l1[0]<l2[-1]:
                   temp=l2[-1]
                   l2[-1]=l1[0]
                   l1[0]=temp
                   i+=1
                  else:
                   flag=False
                   print(-1)
                   break
         if flag==True:
               print(i)
                          
