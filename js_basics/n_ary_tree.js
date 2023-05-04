class NTree{
    constructor(num){
        this.root = num;
        this.children = [];
    }

    add = function(num){
        if(this.root == null){
            this.root = new NTree(num);
            return;
        }

        const prompt = require('prompt-sync')();
        var name = prompt('Do you want to go to another level?(If no - node will be added to the current level');
        if(name == 'n'){
            this.children.push(new NTree(num));
        }else{
            for(let i=0; i<this.children.length; i++){
                var val = 'Do you want to add node to index ' + i.toString();
                name = prompt(val);
                if(name == 'y'){
                    this.children[i].add(num);
                    return;
                }
            }
        }
    }
}


var tree = new NTree(5);

tree.add(6);
tree.add(3);
tree.add(7);
tree.add(10);
tree.add(2);