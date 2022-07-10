#include <iostream>
#include <cmath>

using namespace std;

long long gcd(long long a,long long b){
    if(b == 0){
        return a;
    }
    return gcd(b,a%b);
}
 
int main(){
    long long x, a, b;
    cin>>x;

    long long i=sqrt(x);

    while(i){
        if(x%i==0 && gcd(i,x/i)==1){
            cout<<i<<" ";
            cout<<x/i<<endl;
            break;
        }
        i--;
    } 

    return 0;
}