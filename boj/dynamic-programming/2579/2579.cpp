/*
"계단 오르기"
"https://www.acmicpc.net/problem/2579"
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

  vector<int> dp(num+1);
  vector<int> score(num+1);

  for(int i = 1; i <= num; ++i) {
    cin >> score[i];
  }

  dp[1] = score[1];
  dp[2] = dp[1] + score[2];
  
  for(int i = 3; i <= num; ++i) {
      dp[i] = max(dp[i-3] + score[i-1] + score[i], dp[i-2] + score[i]);
  }
  cout << dp[num] << '\n';

  return 0;
}
