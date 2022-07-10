#include <iostream>

using namespace std;

int main(){
    int n, k;
    cin>>n>>k;

    long long ans = 1, p = n-k+1;

    for(int i = 0; i < k-1; i++) ans = ans * k % 1000000007;
    for(int i = 1; i < p; i++) ans = ans * (p-1) % 1000000007;

    cout<<ans<<endl;
    return 0;
}