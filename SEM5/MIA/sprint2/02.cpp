#include <iostream>

using namespace std;

long long sum(long long x, long long y) {
    return (x * (x + 1) + y * (x + 1)) * (y + 1) / 2;
}

int main() {
    long long m, b, result = 0;
    cin>>m>>b;

    for (long long y = 0; y <= b; y++) {
        //y = -x/m + b  |*m
        //y*m = -x +b*m
        //x = b*m - y*m = m*(b-y)
        long long x = m*(b-y);
        result = max(result, sum(x, y));
    }

    cout << result << endl;
    return 0;
}

