#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

int main(){
    double b,a,c,x1,x2;
    cout<<"a: ";
    cin>>a;
    cout<<"b: ";
    cin>>b;  
    cout<<"c: ";
    cin>>c;
    double delta = b*b-4*a*c;
    if(delta >= 0){
        if(b>0){
            x1 =(-b-sqrt(b*b-4.0*a*c))/(2.0*a);
            if(x1==0.0)
                x2=-b/a;
            else x2 = c/(a*x1); 
        }
        else{
        x1 = (-b+sqrt(b*b-4.0*a*c))/(2.0*a);
            if(x1==0.0)
                x2=-b/a;
            else x2 = c/(a*x1); 
        }
    }
    else cout<<"nie ma miejsc zerowych"<<endl;


    cout<<setprecision(12)<<(-b-sqrt(b*b-4.0*a*c))/(2.0*a)<<", ";
    cout<<setprecision(12) <<(-b+sqrt(b*b-4.0*a*c))/(2.0*a)<<endl;
    cout<<x1<<", "<<x2<<endl;


    return 0;
}