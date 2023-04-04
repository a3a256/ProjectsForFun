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

var res = bubble_sort(arr);

console.log(res);