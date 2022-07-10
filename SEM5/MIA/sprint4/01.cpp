#include <iostream>
#include <math.h>

using namespace std;

int main(){
    long long n;
    cin>>n;

    if(n%2 == 1){
        cout<<0<<endl;
    }
    else{
        long long p = pow(2,n/2);
        cout<<p<<endl;
    }





    return 0;
}