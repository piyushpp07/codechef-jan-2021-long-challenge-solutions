#include<bits/stdc++.h>
using namespace std;
int main()
{
         int t; 
         cin>>t;
         while(t--)
         {
                  int n=0,k=0,d=0,sum=0,z=0;
                  cin>>n>>k>>d;
                  for(int i=0;i<n;i++){
                           cin>>z;
                           sum+=z;
                  }

                  int q=sum/k;
                  if(q>=d)
                  cout<<d<<endl;
                  else cout<<q<<endl;
         }
         return 0;
}
