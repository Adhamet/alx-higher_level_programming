// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
int main() {
    int a = 3;
    char s = 'z';
    double d = 1.03;
    int *pa = &a;
    char *ps = &s;
    double *pd = &d;
    cout << sizeof(pa) << sizeof(*pa) << sizeof(&pa) << endl;
    cout << sizeof(ps) << sizeof(*ps) << sizeof(&ps) << endl;
    cout << sizeof(pd) << sizeof(*pd) << sizeof(&pd) << endl;
}
