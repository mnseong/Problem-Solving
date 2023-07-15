/*
"합분해"
"https://www.acmicpc.net/problem/2225"
*/

#include <iostream>
#define mod 1000000000
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int num;
    int k;
    cin >> num >> k;
    
    long long dp[201][201] = {0, };

    for (int i = 0; i <= num; i++) {
      dp[1][i] = 1;
    }
    for (int i = 2; i <= k; i++) {
      for (int j = 0; j <= num; j++) {
        for (int l = 0; l <= j ; l++) {
          dp[i][j] += dp[i-1][l];
        }
        dp[i][j] %= mod;
      }
    }
    cout << dp[k][num] << '\n';

    return 0;
}