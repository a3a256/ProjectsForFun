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

int* unique(int arr[], int size){
    static int u[50];
    u[0] = arr[0];
    int length = 1;
    bool exists=false;
    for(int i = 0; i<size; i++){
        exists=false;
        for(int j = 0; j<length; j++){
            if(u[j] == arr[i]){
                exists = true;
            }
        }
        if(!(exists)){
            u[length] = arr[i];
            length ++;
        }
    }
    return u;
}

float* sorting(float arr[], int size){
    bool sorted = false;
    float temp=(float)0;
    while (!(sorted)){
        sorted = true;
        for(int i = 1; i<size; i++){
            if(arr[i]<arr[i-1]){
                sorted=false;
                temp = arr[i];
                arr[i] = arr[i-1];
                arr[i-1] = temp;
            }
        }
    }
    return arr;
}

float* percentile(float arr[], int percs[], int arr_size, int perc_size){
    static float percentages[100];
    float* modified;
    modified = sorting(arr, arr_size);
    int ids[perc_size];
    for(int i = 0; i<perc_size; i++){
        ids[i] = ((arr_size*percs[i])/100);
    }
    for(int i = 0; i<perc_size; i++){
        percentages[i] = modified[ids[i]];
    }
    return percentages;
}

float* quantiles(float arr[], int size){
    static float quantile[4];
    float* modified;
    std::cout<<"\n";
    modified = sorting(arr, size);
    int quarter = size/4;
    int three_quarter = quarter*3;
    quantile[0] = modified[0];
    quantile[1] = modified[quarter];
    quantile[2] = modified[three_quarter];
    quantile[3] = modified[size-1];
    return quantile;
}

float** eye(int dim){
    static float** arr = 0;
    arr = new float*[1000];
    for(int i = 0; i<dim; i++){
        arr[i] = new float[1000];
        for(int j = 0; j<dim; j++){
            if(i == j){
                arr[i][j] = 1.0f;
            }else{
                arr[i][j] = 0.0f;
            }
        }
    }
    return arr;
}

float determinant(float arr[][1000], int rows, int cols){
    float det = 0.0f;
    if(rows == 2 && cols == 2){
        det = arr[0][0]*arr[1][1] - arr[0][1]*arr[1][0];
        return det;
    }
    for(int i = 0; i<cols; i++){
        static float new_arr[1000][1000];
        // new_arr = new float*[1000];
        for(int j = 0; j<rows; j++){
            for(int z  = 0; z<cols; z++){
                if(j != 0 && z != i){
                    new_arr[j-1][z] = arr[j][z];
                }
            }
        }
        std::cout << pow(-1, (1+i+1));
        det += pow(-1, (1+i+1))*arr[0][i]*determinant(new_arr, rows-1, cols-1);
    }
    return det;
}



float** multiply_matrix(float arr1[][1000], float arr2[][1000], int rows1, int rows2, int cols1, int cols2){
    static float** new_arr = 0;
    new_arr = new float*[1000];
    for(int i = 0; i<rows1; i++){
        int a = 0;
        new_arr[i] = new float[1000];
        for(int j = 0; j<cols2; j++){
            for(int k=0; k<cols1; k++){
                a += arr1[i][k]*arr2[k][i];
            }
            new_arr[i][j] = a;
        }
    }
    return new_arr;
}


float** transpose_matrix(float arr[][1000], int rows, int columns){
    static float** new_arr = 0;
    new_arr = new float*[1000];
    for(int i = 0; i<columns; i++){
        new_arr[i] = new float[1000];
        for(int j =0; j<rows; j++){
            new_arr[i][j] = arr[j][i];
        }
    }

    return new_arr;
}


float* addition_1d(float arr[], float arr2[], int size){

    static float new_arr[1000];
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

float mean(float *arr, int length){
    float res;
    float sum = 0.0f;
    for(int i = 0; i<length; i++){
        sum += arr[i];
    }
    res = sum/(float)length;
    return res;
}

float standard_deviation(float *arr, int length){
    float r;
    float mn;
    mn = mean(arr, length);
    float upper = 0.0f;
    float temp = 0.0f;
    for(int i = 0; i<length; i++){
        temp = arr[i] - mn;
        upper += pow(temp, 2);
    }
    r = sqrt(upper/(float)length);
    return r;
}
