#include <iostream>
#include <iomanip>  

using namespace std;

int main()
{
    double a,b,c,d, pS, pZ, pp;
    cin>>a>>b>>c>>d;

    //prawdopodobieństwo wygranej SmallR
    pS = a/b;
    //prawdopodobieństwo wygranej przeciwnika
    pZ = c/d; 
    //prawdopodobieństwo że oboje przegrają
    //pp2 = (1-pS)*(1-pZ);
    pp = 1 - ((1-pS)*(1-pZ));

    cout<<setprecision(10)<<pS/pp<<endl;

    return 0;
} 


