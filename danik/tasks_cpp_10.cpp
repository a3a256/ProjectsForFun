#include <iostream>
#include <string>

void task1(){
    int m = 5;
    int n = 4;
    int arr[m][n];
    for(int i = 0; i<m; i++){
        for(int j = 0; j<n; j++){
            arr[i][j] = 10*(i+1);
        }
    }
    for(int i = 0; i<m; i++){
        for(int j = 0; j<n; j++){
            std::cout << arr[i][j] << " ";
        }
        std::cout<<"\n";
    }
}

void task2(){
    int m = 5;
    int n = 4;
    int arr[m][n];
    for(int i = 0; i<n; i++){
        for(int j = 0; j<m; j++){
            arr[j][i] = 5*(j+1);
        }
    }
    for(int i = 0; i<m; i++){
        for(int j = 0; j<n; j++){
            std::cout << arr[i][j] << " ";
        }
        std::cout<<"\n";
    }
}

void task3(){
    int m = 5;
    int n = 4;
    int arr[n] = {5, 3, 8, 9};
    int v[m][n];
    for(int i = 0; i<m; i++){
        for(int j = 0; j<n; j++){
            v[i][j] = arr[j];
        }
    }
    for(int i = 0; i<m; i++){
        for(int j = 0; j<n; j++){
            std::cout<<v[i][j]<<" ";
        }
        std::cout<<"\n";
    }
}

void task4(){
    int m = 5;
    int n = 4;
    int arr[m] = {5, 3, 8, 9, 10};
    int v[m][n];
    for(int i = 0; i<n; i++){
        for(int j = 0; j<m; j++){
            v[j][i] = arr[j];
        }
    }
    for(int i = 0; i<m; i++){
        for(int j = 0; j<n; j++){
            std::cout<<v[i][j]<<" ";
        }
        std::cout<<"\n";
    }
}

void task5(){
    int arr[5][4] = {{3, 4, 6, 1}, {8, 10, 13, 9}, {19, 34, 1, 99}, {18, 11, 0, 5}, {9, 11, 14, 7}};
    int k = 2;
    int m = sizeof(arr)/sizeof(arr[0]);
    int n = sizeof(arr[0])/sizeof(arr[0][0]);
    for(int i = 0; i<m; i++){
        for(int j = 0; j<n; j++){
            if(i==k){
                std::cout<<arr[i][j]<<" ";
            }
        }
    }
}

void task6(){
    int arr[5][4] = {{3, 4, 6, 1}, {8, 10, 13, 9}, {19, 34, 1, 99}, {18, 11, 0, 5}, {9, 11, 14, 7}};
    int k = 2;
    int m = sizeof(arr)/sizeof(arr[0]);
    int n = sizeof(arr[0])/sizeof(arr[0][0]);
    for(int i = 0; i<m; i++){
        for(int j = 0; j<n; j++){
            if(j==k){
                std::cout<<arr[i][j]<<" ";
            }
        }
    }
}

void task7(){
    int arr[5][4] = {{3, 4, 6, 1}, {8, 10, 13, 9}, {19, 34, 1, 99}, {18, 11, 0, 5}, {9, 11, 14, 7}};
    int k = 2;
    int m = sizeof(arr)/sizeof(arr[0]);
    int n = sizeof(arr[0])/sizeof(arr[0][0]);
    for(int i = 0; i<m; i++){
        for(int j = 0; j<n; j++){
            if(j==k){
                std::cout<<arr[i][j]<<" ";
            }
        }
    }
}

void task8(){
    int arr[5][4] = {{3, 4, 6, 1}, {8, 10, 13, 9}, {19, 34, 1, 99}, {18, 11, 0, 5}, {9, 11, 14, 7}};
    int m = sizeof(arr)/sizeof(arr[0]);
    int n = sizeof(arr[0])/sizeof(arr[0][0]);
    for(int i=0; i<m; i++){
        if(i%2==0){
            for(int j=0; j<n; j++){
                std::cout<<arr[i][j]<<" ";
            }
            std::cout<<"\n";
        }
    }
}


void task9(){
    int arr[5][4] = {{3, 4, 6, 1}, {8, 10, 13, 9}, {19, 34, 1, 99}, {18, 11, 0, 5}, {9, 11, 14, 7}};
    int m = sizeof(arr)/sizeof(arr[0]);
    int n = sizeof(arr[0])/sizeof(arr[0][0]);
    for(int i = 0; i<n; i++){
        if(i%2==1){
            for(int j=0; j<m; j++){
                std::cout<<arr[j][i]<<" ";
            }
            std::cout<<"\n";
        }
    }
}


void task10(){
    int arr[5][4] = {{3, 4, 6, 1}, {8, 10, 13, 9}, {19, 34, 1, 99}, {18, 11, 0, 5}, {9, 11, 14, 7}};
    int m = sizeof(arr)/sizeof(arr[0]);
    int n = sizeof(arr[0])/sizeof(arr[0][0]);
    for(int i=0; i<m; i++){
        if(i%2 == 0){
            for(int j=n-1; j>-1; j--){
                std::cout<<arr[i][j]<<" ";
            }
            std::cout<<"\n";
        }else{
            for(int j=0; j<n; j++){
                std::cout<<arr[i][j]<<" ";
            }
            std::cout<<"\n";
        }
    }
}


void task11(){
    int arr[5][4] = {{3, 4, 6, 1}, {8, 10, 13, 9}, {19, 34, 1, 99}, {18, 11, 0, 5}, {9, 11, 14, 7}};
    int m = sizeof(arr)/sizeof(arr[0]);
    int n = sizeof(arr[0])/sizeof(arr[0][0]);
    for(int i=0; i<n; i++){
        if(i%2 == 0){
            for(int j=m-1; j>-1; j--){
                std::cout<<arr[j][i]<<" ";
            }
            std::cout<<"\n";
        }else{
            for(int j=0; j<m; j++){
                std::cout<<arr[j][i]<<" ";
            }
            std::cout<<"\n";
        }
    }
}


void task12(){
    int k = 1;
    int arr[5][4] = {{3, 4, 6, 1}, {8, 10, 13, 9}, {19, 34, 1, 99}, {18, 11, 0, 5}, {9, 11, 14, 7}};
    int length = sizeof(arr[0])/sizeof(arr[0][0]);
    int sum=0, mult=1;
    for (int i = 0; i<length; i++){
        sum += arr[k][i];
        mult *= arr[k][i];
    }
    std::string end = "th";
    switch(k){
        case 1:
            end = "st";
            break;
        case 2:
            end = "nd";
            break;
        case 3:
            end = "rd";
            break;
    }
    std::cout << "Sum of all values on "<<k<<end<<" row is: "<<sum<<"\n";
    std::cout << "Multiplication of all values on "<<k<<end<<" row is: "<<mult<<"\n";
}


int main()
{
    task8();

    return 0;
}
