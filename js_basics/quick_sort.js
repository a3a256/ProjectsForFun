function sort(left, right, pivot){
    var arr = left;
    arr.push(pivot);
    arr = arr.concat(right);

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


var arr = [9, 8, 1,3, 5, 10];

arr = quickSort(arr);

console.log(arr);