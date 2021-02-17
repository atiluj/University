#include <iostream>
#include <math.h>

using namespace std;

double szT(double x){
    double wynik = 0;
    for(int i = 0; i < 15; i=i+2)
        wynik = wynik + pow(-1,i+1)*pow(x, i)/(i+3);

    return wynik;
}

int main(){

    cout<<"A)"<<endl;
    for(double i=-1.0; i<=1; i=i+0.01){
        cout<<i<<"-------------"<<endl;
        cout<<4*cos(i)*cos(i)-3<<endl;
        cout<<-16*cos((i+M_PI/6)/2)*cos((i-M_PI/6)/2)*sin((i+M_PI/6)/2)*sin((i-M_PI/6)/2)<<endl;

        cout<<pow(i, -3)*(M_PI/2-i-atan(1.0/i))<<endl;
        cout<<szT(i)<<endl;    
    }
    cout<<"- - - - - - -"<<"dla pi/6"<<endl;
    cout<<4*cos(M_PI/6)*cos(M_PI/6)-3<<endl;
    cout<<-16*cos((M_PI/6+M_PI/6)/2)*cos((M_PI/6-M_PI/6)/2)*sin((M_PI/6+M_PI/6)/2)*sin((M_PI/6-M_PI/6)/2)<<endl;

    cout<<"- - - - - - -"<<"dla 0.00000000001"<<endl;
    cout<<pow(0.00000000001, -3)*(M_PI/2-0.00000000000001-atan(1.0/0.00000000001))<<endl;
    cout<<szT(0.00000000001)<<endl; 

    return 0;
}