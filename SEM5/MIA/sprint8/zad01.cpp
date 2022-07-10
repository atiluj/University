#include <iostream>

using namespace std;
int main(){
    int t, n, x, y;
    cin>>t;
    for(int i=0; i<t; i++){
        cin>>n>>x>>y;

        if(n == 2){
            cout<<x<<" "<<y<<endl;
        }
        else{
            int r, out;
            int dif = y - x;
            for(int j=1; j<n; j++){
                if(dif % (n-j) == 0){
                    r = dif/(n-j);
                    out = j-1;
                    break;
                }
            }

            int min = x;
            while(out != 0 && min-r > 0){
                min -= r;
                out--;
            }
            int max = min + r*n - r;
            
            for(int j=min; j<=max; j += r){
                cout<<j<<" ";
            }
            cout<<endl;
        }
    }

    return 0;
}
