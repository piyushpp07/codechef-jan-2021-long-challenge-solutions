for i in range(int(input())):
         N,K,x,y=map(int,input().split())
         if x==y:
               print(N,N)
         else :
              arr=[]
              if x<y:
                  arr=[[x+N-y,N],[N,N-y+x],[y-x,0],[0,y-x]]
              else:
                  arr=[[N,y+N-x],[y+N-x,N],[0,x-y],[x-y,0]]
              i=arr[(K-1)%4]
              print(i[0],i[1])
