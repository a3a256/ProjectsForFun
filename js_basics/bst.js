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
    }

    add = function(num){
        var head = this.root;
        if(head == null){
            this.root = new BST(num);
        }else{
            if(num > this.root.val){
                if(this.root.right != null){
                    this.left.add(num);
                }else{
                    this.left = new BST(num);
                }
            }
        }
    }
}