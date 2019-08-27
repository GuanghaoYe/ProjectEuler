#include <cstdio>
#include <cmath>
#include <iostream>
using namespace std;
long long C[105][105]; // C n k
int main() {
    C[1][1]=C[1][0] = 1;
    int ans = 0;
    for(int i=2;i<=100;++i) {
        C[i][0] = 1;
        for(int j=1;j<=i;++j) {
            C[i][j] = C[i-1][j-1] + C[i-1][j];
            if(C[i][j]> 1e7) {
                C[i][j] = 1e7;
            }
            if(C[i][j]>1000000) ans++;
        }
    }
    cout<<ans<<endl;
}