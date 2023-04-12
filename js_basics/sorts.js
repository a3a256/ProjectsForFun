function merge(left, right){
    var i = 0;
    var j = 0;
    var res = [];
    var l_length = left.length;
    var r_right = right.length;
    while(i<l_length && j<r_length){
        if(left[i] < right[j]){
            res.push(left[i]);
            i += 1;
        }else{
            res.push(right[j]);
            j += 1;
        }
    }

    if(j<r_length){
        res = res.concat(right.slice(j, r_length));
    }

    if(i < l_length){
        res = res.concat(left.slice(i, l_length));
    }


    return res;
}