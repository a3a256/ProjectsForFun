#include <iostream>
#include <iomanip>
#include "np_define.h"

void eye_test(){
    float** r;
    r = eye((int)5);
    for(int i = 0; i<5; i++){
        for(int j = 0; j<5; j++){
            std::cout << r[i][j] << " ";
        }
        std::cout << "\n";
    }
}

void determinant_test(){
    float arr[1000][1000] = {{1.2f, 1.7f, 3.1f}, {5.6f, 1.0f, 1.2f}, {9.8f, 4.5f, 9.9f}};
    float dt;
    dt = determinant(arr, (int)3, (int)3);
    std::cout << dt << std::endl;
}

int main(){
    determinant_test();
    return 0;
}

// int main(){
//     // int arr[5] = {0, 1, 2, 3, 4};
//     // int arr2[5] = {5, 6, 7, 8, 10};
//     // int s = 5;
//     // float arr3[5] = {0.5f, 1.2f, 6.5f, 2.6f, 9.1f};
//     // float* res;
//     // res = mean(arr3, s);
//     // std::cout<< res[0] <<std::endl;
//     // float sd;
//     // sd = standard_deviation(arr3, s);
//     // std::cout<< sd<<"\n";
//     // int size = sizeof(arr)/sizeof(arr[0]);
//     // int test[5] = {4, 1, 6, 9, 1};
//     // std::cout<<argmax(test, size)<<std::endl;
//     // int* k;
//     // k = addition_1d(arr, arr2, size);
//     // std::cout << "check"<<std::endl;
//     // for(int i = 0; i<size; i++){
//     //     std::cout << k[i] << std::endl;
//     // }
//     // int n[2][1000] = {{1, 2}, {3, 4}};
//     // int p[2][1000] = {{5, 6}, {3, 9}};
//     // int** l;
//     // int rows = 2;
//     // int cols = 2;
//     // l = transpose_matrix(n, rows, cols);
//     // for(int i =0; i<2; i++){
//     //     for(int j=0; j<2; j++){
//     //         std::cout<<l[i][j]<<" ";
//     //     }
//     //     std::cout<<"\n";
//     // }
//     // int** d = multiply_matrix(n, p, rows, cols, rows, cols);
//     // for(int i =0; i<2; i++){
//     //     for(int j=0; j<2; j++){
//     //         std::cout<<d[i][j]<<" ";
//     //     }
//     //     std::cout<<"\n";
//     // }
//     // float** f;
//     // f = transform_scaler(n, rows, cols);
//     // for(int i =0; i<2; i++){
//     //     for(int j=0; j<2; j++){
//     //         std::cout<<f[i][j]<<" ";
//     //     }
//     //     std::cout<<"\n";
//     // }
// }
