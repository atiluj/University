#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n, t, counter=0; 
    string s, res ="";

    cin>>n>>t>>s;

    for(int i=0; i<n-1; i++){ 
        if(s.substr(0,i+1) == s.substr(n-i-1)){
            counter=i+1;
        }
    } 

    res += s;

    for(int i=1; i<t; i++){
        res += s.substr(counter);
    } 
    cout<<res<<endl;
}
