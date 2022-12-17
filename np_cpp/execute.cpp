#include <iostream>
#include <iomanip>
#include "np_define.h"
#include <vector>

void square_test(){
    std::vector<std::vector <int>> arr;
    for(int i = 0; i<3; i++){
        std::vector<int> temp;
        for(int j = 0; j<3; j++){
            temp.push_back(i+j);
        }
        arr.push_back(temp);
    }
    std::vector<std::vector <int>> renew;
    renew = square(arr);
    for(int i = 0; i<3; i++){
        for(int j = 0; j<3; j++){
            std::cout << renew[i][j] << " ";
        }
        std::cout << "\n";
    }
}

void bincount_test(){
    int* frequencies;
    int categories[] = {0, 0, 0, 0, 1, 1, 1, 1, 0};
    int length = sizeof(categories)/sizeof(categories[0]);
    frequencies = bincount(categories, length);
    int n = classes(categories, length);
    for(int i = 0; i<n; i++){
        std::cout << frequencies[i] << " ";
    }
    std::cout << "\n";
}

void classes_test(){
    int s;
    int pr[] = {0, 0, 1, 0, 2, 3};
    s = classes(pr, (int)5);
    std::cout << s << "\n";
}

void unique_test(){
    int* s;
    int pr[] = {0, 0, 1, 0, 2, 3};
    s = unique(pr, (int)5);
    for(int i = 0; i<3; i++){
        std::cout << s[i] << " ";
    }
    std::cout << "\n";
}

void percentile_test(){
    float* p;
    float arr[] = {3.5f, 1.2f, 9.6f, 2.3f, 9.098f, 0.5f};
    int per[] = {25, 75};
    p = percentile(arr, per, (int)6, (int)2);
    for(int i = 0; i<2; i++){
        std::cout << p[i] << " ";
    }
    std::cout << "\n";
}

void quantile_test(){
    float * q;
    float arr[] = {3.5f, 1.2f, 9.6f, 2.3f, 9.098f, 0.5f};
    q = quantiles(arr, (int)6);
    for(int i = 0; i<4; i++){
        std::cout << q[i] << " ";
    }
    std::cout << "\n";
}

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
    square_test();
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
