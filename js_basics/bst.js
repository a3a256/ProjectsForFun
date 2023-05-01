class Node{
    constructor(num){
        this.val = num;
        this.left = null;
        this.right = null;
    }
}


class BST{
    constructor(num){
        this.root = num;
        this.left = null;
        this.right = null;
        this.arr = [];
    }

    add = function(num){
        var head = this.root;
        if(head == null){
            this.root = new BST(num);
        }else{
            if(num >= this.root){
                if(this.right != null){
                    this.right.add(num);
                }else{
                    this.right = new BST(num);
                }
            }else{
                if(this.left != null){
                    this.left.add(num);
                }else{
                    this.left = new BST(num);
                }
            }
        }
    }

    iot = function(tree){
        if(tree != null){
            this.iot(tree.left);
            console.log(tree.root);
            this.iot(tree.right);
        }
    }

    pot = function(tree){
        if(tree != null){
            console.log(tree.root);
            this.pot(tree.left);
            this.pot(tree.right);
        }
    }

    post = function(tree){
        if(tree != null){
            this.post(tree.left);
            this.post(tree.right);
            console.log(tree.root);
        }
    }

    lot = function(tree){
        var queue = [tree];
        var arr = [];
        var n;
        while(queue.length != 0){
            n = queue.length;
            var temp = [];
            while(n > 0){
                var curNode = queue.shift();
                temp.push(curNode.root);
                if(curNode.left != null){
                    queue.push(curNode.left);
                }
                if(curNode.right != null){
                    queue.push(curNode.right);
                }

                n -= 1;
            }

            arr.push(temp);
        }

        return arr;
    }

    height = function(tree){
        if(tree != null){
            return 1+Math.max(this.height(tree.left), this.height(tree.right));
        }

        return 0;
    }
}


var bst = new BST(5);

bst.add(2);
bst.add(3);
bst.add(1);
bst.add(7);
bst.add(6);
bst.add(8);

// bst.iot(bst);
// bst.pot(bst);
// bst.post(bst);

console.log(bst.lot(bst));

console.log(bst.height(bst));