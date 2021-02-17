#include <iostream>
#include <cmath>

using namespace std;

double f1(double x)
{
    return 2021 * pow(x, 5) - 2020 * pow(x, 4) + 2019 * pow(x, 2);
}

double f2(double x)
{
    return 1 / (1 + 25 * x * x);
}

double f3(double x)
{
    return sin(7 * x - 2) / x;
}

double sumabis(double a, double b, double h, double (*f)(double))
{
    double suma = 0.5 * (f(a) + f(b));
    for (double i = a; i < b; i = i + h)
    {
        suma = suma + f(i);
    }
    return suma;
}

double policz(double a, double b, double (*f)(double))
{
    int n = 16;
    double tabT[n + 1];

    //wzor trapezow
    for (int k = 0; k <= n; k++)
    {
        double h = (b - a) / pow(2, k);
        tabT[k] = h * sumabis(a, b, h, f);
    }

    for (int m = 1; m <= n; m++)
    {
        for (int k = n - m; k >= 0; k--)
        {
            tabT[k + 1] = (pow(4, m) * tabT[k + 1] - tabT[k]) / (pow(4, m) - 1);
        }
    }
    return tabT[n];
}

int main()
{
    cout << policz(-1, 2, f1) << endl;
    cout << policz(-2, 2, f2) << endl;
    cout << policz(2, 3 * M_PI, f3) << endl;

    return 0;
}