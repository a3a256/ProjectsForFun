#include <iostream>
#include <iomanip>
#include "np_define.h"

int main(){
    int arr[5] = {0, 1, 2, 3, 4};
    int arr2[5] = {5, 6, 7, 8, 10};
    int size = sizeof(arr)/sizeof(arr[0]);
    int* k;
    k = addition_1d(arr, arr2, size);
    std::cout << "check"<<std::endl;
    for(int i = 0; i<size; i++){
        std::cout << k[i] << std::endl;
    }
    int n[2][2] = {{1, 2}, {3, 4}};
    int p[2][2] = {{5, 6}, {3, 9}};
    int* l;
    int rows = 2;
    int cols = 2;
    transpose_matrix(n, rows, cols);
}
