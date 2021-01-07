#include<bits/stdc++.h>
#include<sstream>
using namespace std;
int hex(int n)
{ 
     
    int num = n;
    int dec_value = 0;
 
    // Initializing base value to 1, i.e 2^0
    int base = 1;
 
    int temp = num;
    while (temp) {
        int last_digit = temp % 10;
        temp = temp / 10;
 
        dec_value += last_digit * base;
 
        base = base * 2;
    }
 
    return dec_value;

}
int main(){
         int t;cin>>t;
         while(t--)
         {  string arr= "abcdefghijklmnop";
           vector<char>v ;
                  int n=0;
                  cin>>n;
                  string s;
                  cin>>s;
                  for(int i=0;i<n/4;i++)
                  {          
                           string t;
                           int m=(i+1)*4;
                           t.append(s.begin()+i*4,s.begin()+m);
                           stringstream geek(t);   
                           int p=0;
                           geek>>p;
                    
                           
                           v.push_back(arr[hex(p)]);
                 
                  }        
                  
                  for(auto m:v)
                  {
                           cout<<m;
                  }
                  cout<<endl;
                  v.clear();
                  
         }
}
