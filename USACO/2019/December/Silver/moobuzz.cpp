#include <iostream>
#include <fstream>
#include <string>
using namespace std;

//Doesn't work

int main() {
  ifstream myfile;
  myfile.open("moobuzz.in");
  int N;
  myfile >> N;
  myfile.close();
  int realNum=0;
  int c=0;

  while(c!=N){
    if(realNum%3!=0 && realNum%5!=0){
      c+=1;
    }
    realNum+=1;
  }
  realNum-=1;


  // cout << realNum;
  ofstream fout;
  fout.open("moobuzz.out");
  fout << realNum;
  fout << "\n";
  fout.close();
}