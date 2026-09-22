#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main () {
    int n;
    cout << "Enter the number of elements : ";
    cin >> n; 
    int element;
    vector <int> v; 
    for (int i = 0; i <= n - 1; i++) {
        cout << "Enter the element " << i + 1 << " : ";
        cin >> element;
        v.push_back(element);
    } 
    cout << "\n After sorting in descending order : ";
    sort(v.begin(), v.end(), [](int x, int y) {
        return x > y;
    });
    for (int i = 0; i <= v.size() - 1; i++) {
        cout << v.at(i) << " ";
    }
    auto it = find_if(v.begin(), v.end(), [](int x) {
        return x % 2 == 0;
    });
    if (it != v.end()) { 
        cout << "\n First even number :" << *it << "\n";
        cout << "Index of the even number :" << it - v.begin() << "\n";
        cout << "Position of the even number :" << (it - v.begin()) + 1 << "\n";
    } else { 
        cout << "\n No even number available!";
    }
    return 0;
}