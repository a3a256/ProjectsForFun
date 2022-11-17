#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>


int argmax(int arr[], int size){
    int max=arr[0];
    int index=0;
    for(int i=0; i<size; i++){
        if(arr[i]>max){
            max = arr[i];
            index=i;
        }
    }
    return index;
}



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

float** transform_scaler(int arr[][1000], int rows, int columns){
    static float** new_arr = 0;
    static int min[1000];
    static int max[1000];
    for(int i = 0; i<columns; i++){
        min[i] = arr[0][i];
        max[i] = 1;
        for(int j = 0; j<rows; j++){
            if(min[i]>arr[j][i]){
                min[i] = arr[j][i];
            }
            if(max[i]<arr[j][i]){
                max[i] = arr[j][i];
            }
        }
    }
    new_arr = new float*[1000];
    for(int i =0; i<rows; i++){
        new_arr[i] = new float[1000];
        for(int j =0; j<columns; j++){
            new_arr[i][j] = 0;
        }
    }
    for(int i =0; i<columns; i++){
        for(int j =0; j<rows; j++){
            new_arr[j][i] = (arr[j][i]-min[i])/(max[i]-min[i]);
        }
    }
    return new_arr;
}

float std(int arr[], int size){
    float sum = 0;
    for(int i = 0; i<size; i++){
        sum += arr[i];
    }
    float n = size;
    float mean = (float)sum/n;
    float upper = 0;
    float a;
    for(int i = 0; i<size; i++){
        a = arr[i] - mean;
        upper += pow(a, 2);
    }
    float val;
    val = (float)upper/(n-1);
    val = sqrt(val);
    return val;
}
