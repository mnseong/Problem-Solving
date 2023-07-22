/*
"제곱수의 합"
"https://www.acmicpc.net/problem/1699"
*/


#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int num;
    cin >> num;

    vector<int> dp(100001);
    for (int i = 1; i <= num; i++) {
        dp[i] = i;
        for (int j = 2; j * j <= i; j++) {
            dp[i] = min(dp[i], dp[i-j*j]+1);
        }
    }
    cout << dp[num] << '\n';
    
    return 0;
}