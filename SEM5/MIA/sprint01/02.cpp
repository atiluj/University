#include <iostream>

using namespace std;

bool possible(string students, int size){
    for(int i = 0; i < size; i++){
        int flag = 0;
        if(students[i] == 'A' && i!=size-1){
            flag = 1;
        }
        if(flag == 1 && students[i+1] == 'P'){
            return true;
        }
    }
    return false;
}

int main(){

    int t, size;
    
    cin>>t;

    for(int i = 0; i < t; i++){
        cin>>size;
        string students;
        cin>>students;

        int sum=0;
        while(possible(students, size)){
            for(int i = size-1; i > 0; i--){
                if(students[i] == 'P' && students[i-1] == 'A'){
                    students[i] = 'A';
                }
            }
            sum += 1; 
        }
        cout<<sum<<endl;
    }

    return 0;
} 