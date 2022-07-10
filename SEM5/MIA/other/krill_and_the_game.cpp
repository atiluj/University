#include <iostream>

using namespace std;

int main(){
    long long l, r, x, y, k, a, b;
    cin>>l>>r>>x>>y>>k;

    string ans="NO";

    for(b = x; b <= y; b++){
        // a/b = k
        // a = k * b;
        a = k * b;
        if(a>=l && a<=r){
            ans = "YES";
        }
    }
    
    cout<<ans<<endl;


    return 0;
}