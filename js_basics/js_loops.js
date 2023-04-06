var arr = [3, 1, 5, 12, 4, 2, 7];


function bubble_sort(arr){
    var _sorted = false;
    var temp = 0;
    while (true){
        _sorted = true;
        for(let i = 0; i<arr.length-1; i++){
            if(arr[i] > arr[i+1]){
                _sorted = false;
                temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
            }
        }

        if(_sorted == true){
            break;
        }
    }

    return arr;
}

function insertion_sort(arr){
    var len = arr.length;
    var i = 1;
    var j = 0;
    var temp = 0;
    while (i<len){
        j = i
        while(j>0 && arr[j-1] > arr[j]){
            temp = arr[j];
            arr[j] = arr[j-1];
            arr[j-1] = temp;
            j -= 1;
        }
        i += 1;
    }

    return arr;
}

var res = bubble_sort(arr);

console.log(res);