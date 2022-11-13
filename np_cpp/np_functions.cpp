#include <iostream>
#include <iomanip>
#include <cstdio>


int** multiply_matrix(int arr1[][1000], int arr2[][1000], int rows1, int rows2, int cols1, int cols2){
    static int** new_arr = 0;
    new_arr = new int*[1000];
    for(int i = 0; i<rows1; i++){
        int a = 0;
        new_arr[i] = new int[1000];
        for(int j = 0; j<cols2; j++){
            for(int k=0; k<cols1; k++){
                a += arr1[i][k]*arr2[k][i];
            }
            new_arr[i][j] = a;
        }
    }
    return new_arr;
}


int** transpose_matrix(int arr[][1000], int rows, int columns){
    static int** new_arr = 0;
    new_arr = new int*[1000];
    for(int i = 0; i<columns; i++){
        new_arr[i] = new int[1000];
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
    }
    return new_arr;
}
