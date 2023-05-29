#include <iostream>
#include <vector>

// vector solution

std::vector<int> bubbleSort(std::vector<int> arr){
    bool sorted = false;
    int i, n, temp;
    while(!(sorted)){
        sorted = true;
        for(i=1; i<n; i++){
            if(arr[i] < arr[i-1]){
                sorted = false;
                temp = arr[i];
                arr[i] = arr[i-1];
                arr[i-1] = temp;
            }
        }
    }

    return arr;
}

int search(std::vector<int> arr, int start, int end, int target){
    int mid = (start+end)/2;
    if(arr[mid] == target){
        return mid;
    }else if(arr[mid] > target){
        return search(arr, start, mid-1, target);
    }else if(arr[mid] < target){
        return search(arr, mid+1, end, target);
    }

    return -1;
}

int main(){
    std::vector<int> arr = {3, 1, 4, 2, 9, 7, 11, 8, 5, 12};
    int u = 4;
    arr = bubbleSort(arr);
    int index;
    index = search(arr, 0, arr.size()-1, u);

    int i;
    std::cout << "Sorted array is\n";
    for(i=0; i<arr.size(); i++){
        std::cout << arr[i] << " ";
    }
    std::cout << "\n";
    std::cout << "Element " << u << " found in index " << index << "\n";
    return 0;
}