function sort(left, right, pivot){
    var arr = left;
    arr.push(right);
    arr = arr.concat(pivot);

    return arr;
}

function quickSort(arr){
    if(arr.length <= 1){
        return arr;
    }

    var r = [];
    var l = [];

    var pivot = arr.shift();
    for(let i = 0; i<arr.length; i++){
        if(arr[i] > pivot){
            r.push(arr[i]);
        }else{
            l.push(arr[i]);
        }
    }

    return sort(quickSort(l), quickSort(r), pivot);
}