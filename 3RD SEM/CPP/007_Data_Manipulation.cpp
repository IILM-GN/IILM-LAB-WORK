#include <algorithm>
#include <cctype>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main() {
    vector<string> words = {"apple", "banana", "computer", "student"};
    vector<string> upperWords(words.size());
    transform(words.begin(), words.end(), upperWords.begin(),
              [](const string& word) {
                  string result = word;
                  transform(result.begin(), result.end(), result.begin(),
                            [](unsigned char ch) {
                                return static_cast<char>(toupper(ch));
                            });
                  return result;
              });
    for (const string& word : upperWords) {
        cout << word << '\n';
    }
    return 0;
}