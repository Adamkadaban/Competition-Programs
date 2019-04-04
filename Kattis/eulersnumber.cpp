#include <iostream>
#include <iomanip>
using namespace std;
double fact(int n){
  double prod=1.0000;
  for(int i=2;i<=n;i++){
    prod*=i;
  }
  return prod;
}
int main() {
  double n;
  cin >> n;
  double s=0.000;
  for(int i=0;i<=n;i++){
    s+=(1/fact(i));
  }
  cout << setprecision(15) << s;
}