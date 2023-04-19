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
            if(num >= this.root.val){
                if(this.root.right != null){
                    this.right.add(num);
                }else{
                    this.right = new BST(num);
                }
            }else{
                if(this.root.left != null){
                    this.left.add(num);
                }else{
                    this.left = new BST(num);
                }
            }
        }
    }

    iot = function(tree){
        if(tree != null){
            iot(tree.left);
            arr.push(tree.val);
            iot(tree.right);
        }
    }
}