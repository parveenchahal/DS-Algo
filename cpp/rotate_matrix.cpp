#include <bits/stdc++.h>

using namespace std;

void print_2d_vector(vector<vector<int>> &A) {
    int n = A.size();
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cout << A[i][j] << " ";
        }
        cout << endl;
    }
}

void transpose(vector<vector<int>> &mat) {
    int n = mat.size();
    for(int i = 0; i < n; i++) {
        for(int j = i; j < n; j++) {
            if(i == j) {
                continue;
            }
            int t = mat[i][j];
            mat[i][j] = mat[j][i];
            mat[j][i] = t;
        }
    }
}

void flip(vector<vector<int>> &mat) {
    int n = mat.size();
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < (n + 1) / 2; j++) {
            int t = mat[i][j];
            mat[i][j] = mat[i][n - j - 1];
            mat[i][n - j - 1] = t;
        }
    }
}

void rotate(vector<vector<int> > &A) {
    transpose(A);
    flip(A);
}

int main() {
    vector<int> r1 {1, 2};
    vector<int> r2 {3, 4};

    vector<vector<int>> mat;
    mat.push_back(r1);
    mat.push_back(r2);

    rotate(mat);

    print_2d_vector(mat);

    return 0;
}