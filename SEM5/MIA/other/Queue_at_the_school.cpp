#include <iostream>

using namespace std;

int main(){
    int n,t;
    string queue;
    cin>>n>>t>>queue;

    for(int i = 0; i < t; i++){
        for(int j = 0; j < n-1; j++){
            if(queue[j]=='B' && queue[j+1]=='G'){
                queue[j]='G';
                queue[j+1]='B';
                j++;
            }
        }
    }

    cout<<queue<<endl;

    return 0;
}