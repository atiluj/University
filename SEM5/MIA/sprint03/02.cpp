#include <iostream>

using namespace std;

bool works(long long mid, long long k, long long m,long long n){
    long long pillows, left, right, diff;
    //cout<<"mid = "<<mid<<"    k-1 = "<<k-1<<"   n-k = "<<n-k<<endl;
    if(k-1 > mid-1){
        diff = k-1 - (mid-1);
        left = (1+mid-1)*(mid-1)/2 + diff;
    }
    else if(k==1)
        left = 0;
    else if(k == 2)
        left = mid - 1;
    else left = (mid-1+(mid-(k-1)))*(k-1)/2;


    if(n-k > mid-1){
        diff = n-k - (mid-1);
        right = (1+mid-1)*(mid-1)/2 + diff;
    }
    else if(k + 1 == n)
        right = mid - 1;
    else if(k == n)
        right = 0;
    else right = (mid-1 + (mid-(n-k)))*(n-k)/2;

    pillows = mid + left + right;
    //cout<<"pillows = "<<pillows<<endl;

    if(pillows <= m)
            return true;
       return false;
}

int main(){
    long long n, m, k;
    cin>>n>>m>>k;

    //wyszukujemy binarnie dobrej odpowiedzie
    long long l = 1, r = m, mid, frodo;
    while(r-l >= 0){
        mid = (l+r)/2;
        
        if(works(mid, k, m, n)){
            frodo = mid;
            l = mid+1;
        }
        else r = mid - 1;
    }

    cout<<frodo<<endl;

    return 0;
}