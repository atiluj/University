#include <iostream>

using namespace std;

int main(){
    int n,m,x,min=1000000000,ans = 0;
    cin>>n>>m;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin>>x;
            if(x<min){
                min = x;
            }
        }
        if(min>ans){
            ans = min;
        }

        min=1000000000;
    }

    cout<<ans<<endl;


    return 0;
}