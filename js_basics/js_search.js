function binary_search(arr, start, end, target){
    var mid = parseInt(start+end);
    if(arr[mid] == target){
        return mid;
    }else if(arr[mid] > target){
        return binary_search(arr, start, mid-1, target);
    }else if(arr[mid] < target){
        return binary_search(arr, mid+1, end, target);
    }
    return -1;
}