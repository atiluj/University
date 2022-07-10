#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;

void wypisz(int *tab, int n){

    for(int i = 0; i < n; i++){
        cout<<tab[i]<<" ";
    }
    cout<<endl;
}

int removeDuplicates(int tab[], int n){

    if (n<=1)
        return n;
 
    int temp[n], j = 0;

    for (int i=0; i<n-1; i++)

        if (tab[i] != tab[i+1])
            temp[j++] = tab[i];
 
    temp[j++] = tab[n-1];
 
    for (int i=0; i<j; i++)
        tab[i] = temp[i];
 
    return j;
}
 

int check(int tab[], int n){

    //posortuj tablice
    sort(tab, tab + n);

    //usuń duplikaty
    n = removeDuplicates(tab, n);

    if(n<3){
        cout<<"NO"<<endl;;
        exit(0);
    } 

    for(int i = 0; i < n-2; i++){
        if(tab[i+1]-tab[i] == 1 && tab[i+2]-tab[i+1] == 1){
            cout<<"YES"<<endl;
            exit(0);
        }
    }
    cout<<"NO"<<endl;
    exit(0);
}


int main(){
    int n;
    cin>>n;

    int tab[n];
    for(int i = 0; i < n; i++){
        cin>>tab[i];
    }

    check(tab, n);

    return 0;
}