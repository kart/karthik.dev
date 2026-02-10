#include <iostream>
#include <vector>

using namespace std;

const int64_t MODULO = 1e9 + 7;

int solve(int n) {
    std::vector<int> dp(n + 1, 0);
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 2; // 1 + 1, 2
    dp[3] = 4; // 1 + 1 + 1, 1 + 2, 2 + 1, 3
    for (int i = 4; i <= n; i++) {
        for (int dice = 1; dice <= 6; dice++) {
            if (dice <= i) {
                dp[i] = (dp[i] + dp[i - dice]) % MODULO;
            }
        }
    }
    return dp[n];
}

int main() {
    // Optimization for faster I/O (Required for CSES large inputs)
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    if (cin >> n) {
        cout << solve(n) << "\n";
    }

    return 0;
}
