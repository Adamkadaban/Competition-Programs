#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool isPrime(int num)
{
	for (int i = 2; i <= sqrt(num); i++)
	{
		if (num % i == 0)
			return false;
	}
	return !(num == 1);
}
int main() {
	int amt; cin >> amt;
	vector<vector<int>> nums;
	for (int i = 0; i < amt; i++)
	{
		vector<int> sub; int a, b;
		cin >> a >> b;
		sub.push_back(a); sub.push_back(b);
		nums.push_back(sub);
	}
	for (vector<int> temp : nums)
	{
		for (int x= temp.at(0); x <= temp.at(1); x++)
		{
			if (isPrime(x))
				cout << x << "\n";
		}
		cout << "\n";
	}
}