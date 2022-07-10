#include <iostream>

using namespace std;


int main(){
    int n, res = 0, x, pom;
    cin>>n;

    //v-cry in room ,d-cry in hall ,p-confidece
    long long v[n], d[n], p[n];

    for(int i = 0; i < n; i++){
        cin>>v[i]>>d[i]>>p[i];
    }

    for(int i = 0; i < n; i++){
        x = 0;
        if(p[i] >= 0){
            for(int j = i+1; j < n; j++){
                if(p[j]>=0){
                    if(v[i] - x >= 0){
                        pom = v[i] - x;
                        //x++;
                    }
                    else
                        pom = 0;

                    if(p[j] - pom >= 0){
                        p[j] = p[j] - pom;
                    }
                    else
                    {
                        p[j] = -2;
                    }
                    x++;
                    
                }
            }
            for(int j = i + 1; j < n; j++){
                if(p[j] == -2){
                    for(int k = j + 1; k < n; k++){
                        if(p[k] >= 0){
                            p[k] -= d[j];
                            if(p[k] < 0){
                                p[k] = -2;
                            }
                        }
                    }
                    p[j] = -1;
                }
            }
        }
    }


    for(int i = 0; i < n; i++){
        if(p[i] >= 0)
        {
            res++;
        }
    }

    cout<<res<<endl;
    
    for(int i = 0; i < n; i++){
        if(p[i] >= 0)
            cout<<i+1<<" ";
    }

    cout<<endl;
    return 0;
}