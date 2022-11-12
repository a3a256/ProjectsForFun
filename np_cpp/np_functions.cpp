#include <iostream>
#include <iomanip>


int** transpose_matrix(int arr[][1000], int rows, int columns){
    int** new_arr = 0;
    new_arr = new int*[rows];
    for(int i = 0; i<columns; i++){
        new_arr = new int*[columns];
        for(int j =0; j<rows; j++){
            new_arr[i][j] = arr[j][i];
        }
    }

    return new_arr;
}


int* addition_1d(int arr[], int arr2[], int size){

    static int new_arr[1000];
    for(int i = 0; i<size; i++){
        new_arr[i] = arr[i] + arr2[i];
        std::cout << new_arr[i] << "\n";
    }
    return new_arr;
}
