#include<bits/stdc++.h>

using namespace std;

unsigned int *f;

bool get(int index) {
    unsigned int x = 1;
    return f[index / 32] & x << ((index % 32) - 1);
}

void make(int index, bool value) {
    unsigned int x = 1;
    if(value && !get(index)) {
        f[index / 32] = f[index / 32] + (x << ((index % 32) - 1));
        return;
    }
    
    if(!value && get(index)) {
        f[index / 32] = f[index / 32] - (x << ((index % 32) - 1));
        return;
    }
}

int repeatedNumber(const vector<int> &A) {
    int n = A.size();
    f = new unsigned int [n / 32 + 1] {0};
    for(int i = 0; i < n; i++) {
        if(get(A[i])) {
            return A[i];
        } else {
            make(A[i], true);
        }
    }
    return -1;
}


int main() {
    bool x;
    cout << sizeof(x);
    //vector<int> arr { 3, 4, 1, 4, 1 };
    //int a = repeatedNumber(arr);
    //cout << a;
    return 0;
}