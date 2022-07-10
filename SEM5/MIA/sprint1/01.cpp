#include <iostream>

using namespace std;

int prof(int h, int c, int b, int p, int f){
    int sum=0;
    while(p>0 && b>1){
        sum += h;
        p -= 1;
        b -= 2;
    }
    while(f>0 && b>1){
        sum += c;
        f -= 1;
        b -= 2;
    }
    return sum;
}

int main(){
    //b-buns
    //p-beef patty
    //f-chicken cutlet
    //h-hamburger price
    //c-chickenburger price
    int t, b, p, f, h, c;
    
    cin>>t;

    for(int i = 0; i < t; i++){
        cin>>b>>p>>f;
        cin>>h>>c;

        if(h>c){
            cout<<prof(h,c,b,p,f)<<endl;
        }            
        else{
            cout<<prof(c,h,b,f,p)<<endl;
        }
    }

    return 0;
} 