function perms(arr){
    if(arr.length == 0){
        var res = [[]]
        return res;
    }

    var last = arr.pop();

    var output = [];

    for(let perm in arr){
        for(let i = 0; i<perm.length + 1; i++){
            var f = perm.slice(i);
            var l = perm.slice(i, perm.length);
            f.push(last);
            var ne = f.concat(l);
            output.push(ne);
        }
    }

    return output.sort()
}