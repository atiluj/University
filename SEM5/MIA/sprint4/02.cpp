#include <iostream>
#include <math.h>
#include <algorithm>

using namespace std;

int main(){
    int n, maks, result=0;
    cin>>n;

    int tab[n];
    for(int i = 0; i < n; i++){
        cin>>tab[i];
    }

    maks = tab[n-1];

    int dp[maks+1]={0}, d[maks+1]={0};

    for(int i = 0; i < n; i++){
        dp[tab[i]]=1;
        d[tab[i]]=1;

        for(int j = 2; j*j<=tab[i]; j++){
            if(tab[i]%j == 0){
                dp[tab[i]] = max(dp[tab[i]],d[j]+1);
                dp[tab[i]] = max(dp[tab[i]],d[tab[i]/j]+1);
            }
        }

        for(int j = 2; j*j<=tab[i]; j++){
            if(tab[i]%j == 0){
                d[j]=dp[tab[i]];
                d[tab[i]/j] = dp[tab[i]];
            }
        }

        result = max(result, dp[tab[i]]);   
    }

    cout<<result<<endl;

    return 0;
}