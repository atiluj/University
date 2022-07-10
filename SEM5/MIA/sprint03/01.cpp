#include <iostream> 
#include<algorithm>

using namespace std;

int main(){
    int n, num, sum = 0, m; 
    cin>>n;

    int tab[n];
    for(int i = 0; i < n; i++){
        cin>>num;
        sum += num;
        tab[i] = sum;
    }

    int juicy[sum+1], itter=0;
    for(int i = 0; i <= sum; i++){

        if(i <= tab[itter]){
            juicy[i] = itter + 1;;
        }
        else{
            itter++;
            i--;
        }
    }

    cin>>m;
    for(int i = 0; i < m; i++){
        cin>>num;
        cout<<juicy[num]<<endl;
    }





    return 0;
}