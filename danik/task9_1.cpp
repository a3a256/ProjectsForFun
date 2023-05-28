#include <iostream>

int get_min(int arr[], int n){
    int minv;
    int i;
    minv = arr[0];
    for(i=0; i<n; i++){
        if(minv < arr[i]){
            minv = arr[i];
        }
    }

    return minv;
}

int get_max(int arr[], int n){
    int maxv;
    int i;
    maxv = arr[0];
    for(i=0; i<n; i++){
        if(maxv > arr[i]){
            maxv = arr[i];
        }
    }

    return maxv;
}


int main(){
    int arr [5][6] = {{2, 5, 1, 4, 9, 12}, {4, 8, 6, 1, 19, 3}, {1, 6, 5, 9, 10, 11}, {12, 13, 11, 25, 3, 9}, {9, 2, 6, 1, 15, 4}};
    int m=5, n=6;
    int i, j;
    int mean_col [n];
    int sumv;
    for(i=0; i<n; i++){
        sumv = 0;
        for(j=0; j<m; j++){
            sumv += arr[j][i];
        }
        mean_col[i] = sumv/m;
    }

    int mins[m];
    int maxs[m];
    for(i=0; i<m; i++){
        mins[i] = get_min(arr[i], n);
        maxs[i] = get_max(arr[i], n);
    }

    std::cout << "Mean of each column:\n";
    for(i=0; i<n; i++){
        std::cout << mean_col[i] << " ";
    }
    std::cout << "\n";
    for(i=0; i<m; i++){
        std::cout << "Min and max values of row with index " << i << " are " << mins[i] << " and " << maxs[i] << " respectively.\n";
    }
}