#include <iostream>
#include <algorithm>

using namespace std;

int main(){

    int t, size;
    
    cin>>t;

    for(int i = 0; i < t; i++){
        cin>>size;

        string numbers, result = "", check1 = "", check2 = "";
        cin>>numbers;
        string sorted_numbers = numbers;

        for(int i = 0; i < size; i++){
            result += "2";
        }

        sort(sorted_numbers.begin(), sorted_numbers.end());

        int h = 0;
        for(int i = 0; i < size; i++){
            if(numbers[i] == sorted_numbers[h]){
                result[i] = '1';
                h++;
                check1 += numbers[i];

            }
            else
            {
                check2 += numbers[i]; 
            }
        }

        if(check1+check2 == sorted_numbers) {
            cout<<result<<endl;
        }
        else    
            cout<<"-"<<endl;

    }

    return 0;
} 