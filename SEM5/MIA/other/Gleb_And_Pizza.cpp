#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int r,d,n,x,y,z, ans=0;
    cin>>r>>d>>n;

    for(int i=0; i<n; i++){
        cin>>x>>y>>z;
        double k  = sqrt(x*x+y*y);
        int h = r-d;
        if(k <= r && k >= h && (k+z) <= r && (k-z) >= h) ans++;   
    }

    cout<<ans<<endl;

    return 0;
}