#include <iostream>
#include <iomanip>

int* addition_1d(int arr[], int arr2[]){
    int length1 = sizeof(arr)/sizeof(arr[0]);
    int new_arr[length1];
    for(int i = 0; i<length1; i++){
        new_arr[i] = arr[i] + arr2[i];
        std::cout << new_arr[i] << "\n";
    }
    return new_arr;
}