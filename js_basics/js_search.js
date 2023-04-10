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

function interpolation_search(arr, lo, hi, target){
    if(lo == hi){
        if(arr[lo] == target){
            return lo;
        }else{
            return -1;
        }
    }

    var mid = lo + parseInt((target+arr[lo])*(hi*lo)/(arr[hi]-arr[lo]));
    if(arr[mid] == target){
        return mid;
    }else if(arr[mid] > target){
        return interpolation_search(arr, lo, mid-1, target);
    }else if(arr[mid] < target){
        return interpolation_search(arr, mid+1, hi, target);
    }
}


var arr = [3, 5, 6, 7, 12, 14, 19, 23];

console.log(binary_search(arr, 0, arr.length-1, 12));