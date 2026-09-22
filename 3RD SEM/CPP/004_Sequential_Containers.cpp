/*
Sequential Containers : Demonstrate the use of std :: array and std :: vector by storing a list of student marks and 
calculating the average marks.
*/

#include <array>
#include <iostream>
#include <vector>
using namespace std;
int main() {
  array<int, 5> arr;
  for (int i = 0; i < 5; i++) {
    cout << "Marks of Student" << i + 1 << ":";
    cin >> arr[i];
  }
  int sum = 0;
  cout << "\n Using array \n MARKS [5] =";
  for (int i = 0; i <= 4; i++) {
    sum += arr.at(i);
    cout << arr.at(i) << " ";
  }
  cout << "\n Total Marks :" << sum << "\n";
  cout << "\n Average Marks :" << float(sum) / arr.size() << "\n";
  int marks;
  int n;
  cout << "Enter a number : ";
  cin >> n;
  vector<int> vec;
  for (int i = 0; i <= n - 1; i++) {
    cout << "Enter the Marks of Student : " << i + 1 << ":";
    cin >> marks;
    vec.push_back(marks);
  }
  int new_sum = 0;
  cout << "\n Using vector \n MARKS [" << n << "] =";
  for (int i = 0; i <= vec.size() - 1; i++) {
    new_sum += vec.at(i);
    cout << vec.at(i) << " ";
  }
  cout << "\n Total Marks :" << new_sum << "\n";
  cout << "\n Average Marks :" << float(new_sum) / vec.size() << "\n";
  return 0;
}