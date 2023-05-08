function perms(arr){
    if(arr.length == 1){
        var res = [arr];
        return res;
    }

    var last = arr.pop();

    var output = [];

    for(let perm in perms(arr)){
        for(let i = 0; i<perm.length + 1; i++){
            var f = perm.slice(0, i);
            var l = perm.slice(i);
            console.log(f);
            f.push(last);
            var ne = f.concat(l);
            output.push(ne);
        }
    }

    return output.sort()
}

var arr = [1, 2, 3];

console.log(arr.slice(1));

console.log(arr);

for(let perm in perms(arr)){
    console.log(perm);
}