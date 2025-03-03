#include <bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> v;
    for (int i = 1; i <= 4; ++i)
    {
        v.push_back(i); // try changing 4 to 5
    }
    vector<int>::iterator it = v.begin();
    cout << *it << "\n"; // should output v[0] = 1
    v.push_back(rand()); // increase vector size by 1
    it = v.begin();
    cout << *it << "\n "; // isn’t v[0] should remain 1?
}