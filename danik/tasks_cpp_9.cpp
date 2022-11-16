#include <iostream>

void task15(){
    int arr[10] = {2, 15, 1, 20, 8, 10, 4, 17, 9 , 23};
    int length = sizeof(arr)/sizeof(arr[0]);
    int i = 0, j = length-1;
    int val;
    while(i<=j){
        if(arr[i]%2==0 && arr[j]%2!=0){
            val = arr[i];
            arr[i] = arr[j];
            arr[j] = val;
            i=0;
            j=length-1;
        }else if(arr[j]%2!=0){
            i++;
        }else if(arr[i]%2==0){
            j--;
        }else{
            i++;
            j--;
        }
    }
    for(int i=0;i<length;i++){
        std::cout<<arr[i]<<" ";
    }
    std::cout<<"\n";
}


void task14(){
    int arr[10] = {2, 15, 1, 20, 8, 10, 4, 17, 9 , 23};
    int length = sizeof(arr)/sizeof(arr[0]);
    bool sorted = false;
    int val;
    while(!(sorted)){
        sorted=true;
        for(int i=1; i<length; i++){
            if(arr[i]>arr[i-1]){
                sorted=false;
                val = arr[i];
                arr[i] = arr[i-1];
                arr[i-1] = val;
            }
        }
    }
    for(int i=0;i<length;i++){
        std::cout<<arr[i]<<" ";
    }
    std::cout<<"\n";
}


void task13(){
    int arr[10] = {2, 15, 1, 20, 8, 10, 4, 17, 9 , 23};
    int length = sizeof(arr)/sizeof(arr[0]);
    bool sorted = false;
    int val;
    while(!(sorted)){
        sorted=true;
        for(int i=1; i<length; i++){
            if(arr[i]<arr[i-1]){
                sorted=false;
                val = arr[i];
                arr[i] = arr[i-1];
                arr[i-1] = val;
            }
        }
    }
    for(int i=0;i<length;i++){
        std::cout<<arr[i]<<" ";
    }
    std::cout<<"\n";
}

void task12(){
    int arr[10] = {2, 15, 1, 20, 8, 10, 4, 17, 9 , 23};
    int length = sizeof(arr)/sizeof(arr[0]);
    for(int i=1; i<length; i+=2){
        arr[i] = 0;
    }
    for(int i=0;i<length;i++){
        std::cout<<arr[i]<<" ";
    }
    std::cout<<"\n";
}


void task11(){
    int arr[10] = {2, 15, 1, 20, 8, 10, 4, 17, 9 , 23};
    int length = sizeof(arr)/sizeof(arr[0]);
    for(int i=0; i<length; i+=2){
        arr[i] = 0;
    }
    for(int i=0;i<length;i++){
        std::cout<<arr[i]<<" ";
    }
    std::cout<<"\n";
}


void task10(){
    int arr[10] = {2, 15, 1, 11, 8, 20, 4, 17, 9 , 11};
    int length = sizeof(arr)/sizeof(arr[0]);
    int min=arr[0], max=0;
    int min_index=0, max_index=0;
    for(int i=0; i<length; i++){
        if(arr[i]>max){
            max=arr[i];
            max_index=i;
        }
        if(arr[i]<min){
            min=arr[i];
            min_index=i;
        }
    }
    for(int i=0; i<length; i++){
        if(i>min_index && i<max_index){
            arr[i] = 0;
        }
    }
    for(int i=0;i<length;i++){
        std::cout<<arr[i]<<" ";
    }
    std::cout<<"\n";
}


void task9(){
    int arr[10] = {2, 15, 1, 11, 8, 20, 4, 17, 9 , 11};
    int length = sizeof(arr)/sizeof(arr[0]);
    int i=0, j=length-1;
    int temp;
    while(i<=j){
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        i ++;
        j--;
    }
    for(int i=0;i<length;i++){
        std::cout<<arr[i]<<" ";
    }
    std::cout<<"\n";
}


void task8(){
    int arr[10] = {2, 15, 1, 11, 8, 20, 4, 17, 9 , 11};
    int length = sizeof(arr)/sizeof(arr[0]);
    int i=0, j=length-1;
    int temp;
    for(int i=1; i<length; i+=2){
        temp = arr[i];
        arr[i] = arr[i-1];
        arr[i-1] = temp;
    }
    for(int i=0;i<length;i++){
        std::cout<<arr[i]<<" ";
    }
    std::cout<<"\n";
}

void task7(){
    int max=0;
    int min=0;
    int arr[] = {1, 5, 4, 6, 10, 12, 4, 5, 13, 8};
    for(int i = 0; i<sizeof(arr)/sizeof(arr[0]); i++){
        if(arr[min]<arr[i]){
            min = i;
        }
        if(arr[max]>arr[i]){
            max = i;
        }
    }
    int temp = arr[min];
    arr[min] = arr[max];
    arr[max] = temp;
    for(int i = 0; i<sizeof(arr)/sizeof(arr[0]); i++){
        std::cout<<arr[i]<<" ";
    }
}

void task6(){
    int arr[] = {1, 5, 4, 6, 10, 12, 4, 5, 13, 8};
    int odd;
    for(int i = 0; i<sizeof(arr)/sizeof(arr[0]); i++){
        if(arr[i]%2 != 0){
            odd = arr[i];
        }
    }
    for(int i = 0; i<sizeof(arr)/sizeof(arr[0]); i++){
        if(arr[i]%2!=0){
            arr[i]+= odd;
        }
        std::cout<<arr[i]<<" ";
    }
}

void task5(){
    int arr[] = {1, 5, 4, 6, 10, 12, 4, 5, 13, 19};
    int k = arr[0];
    for(int i = 0; i<sizeof(arr)/sizeof(arr[0]); i++){
        if(arr[i]%2==0){
            arr[i] += k;
        }
        std::cout<<arr[i]<<" ";
    }
}

void task4(){
    int arr[] = {1, 2, 3, 4, 5};
    int k = 3;
    for(int i=0; i<sizeof(arr)/sizeof(arr[0]); i++){
        arr[i] += k;
        std::cout << arr[i] <<" ";
    }
    std::cout << "\n";
}

void task3(){
    int count = 0;
    int arr[] = {1, 2, 6, 4, 9, 10, 11};
    int arr1[sizeof(arr)/sizeof(arr[0])];
    int j = 0;
    for(int i = 0; i<sizeof(arr)/sizeof(arr[0]); i++){
        if(arr[i]%2 == 0){
            arr1[j] = arr[i];
            std::cout<<arr1[j]<<" ";
            j += 1;
        }
    }
    std::cout<<"\n"<<"The length is "<<j<<"\n";
}

void task2(){
    int arr[] = {2, 13, 5, 9};
    int arr1[] = {6, 1, 11, 8};
    int length = sizeof(arr)/sizeof(arr[0]);
    int c[length];
    for(int i = 0; i<length; i++){
        if (arr[i]>arr1[i]){
            c[i] = arr[i];
        }else{
            c[i] = arr1[i];
        }
    }
    for(int i = 0; i<length; i++){
        std::cout<<c[i]<<" ";
    }
    std::cout<<"\n";
}

void task1(){
    int arr[] = {1, 2, 3, 4, 5};
    int arr1[] = {6, 7, 8, 9, 10};
    int length = sizeof(arr)/sizeof(arr[0]);
    int temp;
    for(int i = 0; i<length; i++){
        temp = arr[i];
        arr[i] = arr1[i];
        arr1[i] = temp;
    }
    for(int i = 0; i<length; i++){
        std::cout<<arr[i]<<" ";
    }
    std::cout<<"\n";
    for(int i = 0; i<length; i++){
        std::cout<<arr1[i]<<" ";
    }
    std::cout<<"\n";
}

int main()
{
    task8();

    return 0;
}
