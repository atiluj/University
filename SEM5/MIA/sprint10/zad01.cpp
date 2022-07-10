#include <iostream>
#include <string>

using namespace std;

string game(string s){
    int zero = 0, one = 0;

    for(int i = 0; i < s.length(); i++){
        if(s[i] == '1') one++;
        else zero++;
    }

    if(zero == 0 || one == 0) return "NET";

    if(one>zero){
        if(zero%2 == 0) return "NET";
        else return "DA";
    }
    else {
        if(one%2 == 0) return "NET";
        else return "DA";
    }

    return "error";
}

int main(){
    int t;
    string s;
    cin>>t;
    for(int i = 0; i < t; i++){
        cin>>s;
        cout<<game(s)<<endl;;
    }

    return 0;
}