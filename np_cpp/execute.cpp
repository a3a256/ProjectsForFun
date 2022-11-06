#include <iostream>
#include <iomanip>
#include "np_define.h"

int main(){
    int arr[5] = {0, 1, 2, 3, 4};
    int arr2[5] = {5, 6, 7, 8, 10};
    int size = sizeof(arr)/sizeof(arr[0]);
    addition_1d(arr, arr2, size);
}
