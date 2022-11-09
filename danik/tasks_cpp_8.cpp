#include <iostream>

void task8(){
    int arr[10] = {2, 5, 1, 7, 8, 10, 4, 17, 9 , 23};
    int length = sizeof(arr)/sizeof(arr[0]);
    for(int i=0;i<length;i++){
        if(arr[i]%2!=0){
            std::cout<<arr[i]<<" ";
        }
    }
    std::cout<<"\n";
}


void task9(){
    int arr[10] = {2, 5, 1, 7, 8, 10, 4, 17, 9 , 23};
    int length = sizeof(arr)/sizeof(arr[0]);
    for(int i=length-1;i>-1;i--){
        if(arr[i]%2==0){
            std::cout<<arr[i]<<" ";
        }
    }
    std::cout<<"\n";
}


void task10(){
    int arr[10] = {2, 5, 1, 7, 8, 10, 4, 17, 9 , 23};
    int length = sizeof(arr)/sizeof(arr[0]);
    for(int i=0;i<length;i++){
        if(arr[i]%2==0){
            std::cout<<arr[i]<<" ";
        }
    }
    std::cout<<"\n";
    for(int i=length-1; i>-1; i--){
        if(arr[i]%2!=0){
            std::cout<<arr[i]<<" ";
        }
    }
    std::cout<<"\n";
}


void task11(){
    int arr[10] = {2, 5, 1, 7, 8, 10, 4, 17, 9 , 23};
    int length = sizeof(arr)/sizeof(arr[0]);
    int k=3, l=6;
    int sum=0;
    for(int i=0;i<length;i++){
        if(i>=3 && i<=6){
            sum += arr[i];
        }
    }
    std::cout << "Summation of all values between index "<<k<<" and "<<l<<": "<<sum<<"\n";
}


void task12(){
    int arr[10] = {2, 5, 1, 7, 8, 10, 4, 17, 9 , 23};
    int length = sizeof(arr)/sizeof(arr[0]);
    int count = 0;
    int k=3, l=6;
    int sum=0;
    for(int i=0;i<length;i++){
        if(i<3 || i>6){
            sum += arr[i];
            count += 1;
        }
    }
    std::cout << "Summation of all values except index "<<k<<" and "<<l<<": "<<(float)sum/(float)count<<"\n";
}


void task13(){
    int arr[10] = {2, 5, 1, 7, 8, 10, 4, 17, 9 , 23};
    int length = sizeof(arr)/sizeof(arr[0]);
    int k=3, l=6;
    int sum=0;
    for(int i=0;i<length;i++){
        if(i<3 || i>6){
            sum += arr[i];
        }
    }
    std::cout << "Summation of all values except index "<<k<<" and "<<l<<": "<<sum<<"\n";
}


int task14(){
    int arr[10] = {-1, 2, -3, 4, -5, 6, -7, 8, -9, 10};
    int length = sizeof(arr)/sizeof(arr[0]);
    for(int i=1; i<length; i++){
        if(arr[i]%2 == 0){
            if(arr[i-1]%2==0){
                return 0;
            }
        }else{
            if(arr[i-1]%2!=0){
                return 0;
            }
        }
    }
    return 1;
}


int task15(){
    int arr[10] = {-1, 2, -3, 4, -5, 6, -7, 8, -9, 10};
    int length = sizeof(arr)/sizeof(arr[0]);
    for(int i=1; i<length; i++){
        if(arr[i] >= 0){
            if(arr[i-1]>=0){
                return 0;
            }
        }else{
            if(arr[i-1]<0){
                return 0;
            }
        }
    }
    return 1;
}


int main()
{
    task8();

    return 0;
}