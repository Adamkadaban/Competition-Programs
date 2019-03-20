#include <string>
#include <iostream>
// #include <vector>
using namespace std;
bool isPal(int n) {
	int reversedInteger = 0, remainder, originalInteger;

	originalInteger = n;

	while (n != 0) {
		remainder = n % 10;
		reversedInteger = reversedInteger * 10 + remainder;
		n /= 10;
	}

	if (originalInteger == reversedInteger)
		return true;
	return false;

}
string findNext(int n) {
	int r = n + 1;
	while (!isPal(r)) {
		r++;
	}
	return to_string(r);
}



int main() {
	int N;
	cin >> N;
	// vector<int> nums;
	int nums[N];
	for (int i = 0; i < N; i++) {
		cin >> nums[i];
	}
	for (int i = 0; i < N; i++) {
		cout << nums[i];
		cout << "\n";
	}
}
