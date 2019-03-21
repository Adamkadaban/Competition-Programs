#include <iostream>
#include <string>
#include <math.h>

using namespace std;

bool isPrime(int n) {
	for (int i = 2; i <= sqrt(n); i++) {
		if (n%i == 0) 
			return false;
	}
	return !(n==1);
}
int main(){
  int n;
  cin >> n;
  for(int i=0;i<n;i++){
    int n1;
    int n2;
    cin >> n1;
    cin >> n2;
    for(int j=n1;j<=n2;j++){
      if(isPrime(j)){
        cout << j << endl;
      }
    }
    cout << endl;
  }
}
