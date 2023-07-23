/*
"가장 긴 감소하는 부분 수열"
"https://www.acmicpc.net/problem/11722"
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int num;
    cin >> num;

    vector<int> dp(num+1, 1);
    vector<int> seq(num+1);

    for (int i = 1; i <= num; ++i) {
        cin >> seq[i];
    }
    for (int i = 1; i <= num; ++i) {
        for (int j = 1; j <= i; ++j) {
            if (seq[i] < seq[j] && dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
            }
        }
    }
    cout << *max_element(dp.begin(), dp.end()) << '\n';

    return 0;
}