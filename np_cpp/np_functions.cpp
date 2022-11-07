#include <iostream>
#include <iomanip>

int* addition_1d(int arr[], int arr2[], int size){
    int new_arr[size];
    for(int i = 0; i<size; i++){
        new_arr[i] = arr[i] + arr2[i];
        std::cout << new_arr[i] << "\n";
    }
    return new_arr;
}
