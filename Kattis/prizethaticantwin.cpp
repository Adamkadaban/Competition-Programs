#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int n;
    int x;
    cin >> n;
    cin >> x;
    vector<int> arr(n);
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr.begin(), arr.end());
    int r = 1;
    for(int i = 1; i < n; ++i) {
        if(arr[i] + arr[i-1] <= x) r = i+1;
    }
    cout << r<<"\n";
}