#include <iostream>
#include <map>
#include <string>
using namespace std;
int main() {
    map<string, string> m;
    string key;
    string value;
    int n;
    cout << "Enter the word-meaning pairs : ";
    cin >> n;
    cin.ignore();
    for (int i = 0; i < n; i++) {
        cout << "Enter the word " << i + 1 << ": ";
        getline(cin, key);
        cout << "Enter the meaning " << i + 1 << ": ";
        getline(cin, value);
        m.insert({ key, value });
    }
    cout << "\nword-meaning\n";
    for (auto val : m) {
        cout << val.first << " -> " << val.second << "\n";
    }
    return 0;
}