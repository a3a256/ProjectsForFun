class Node{
    constructor(num){
        this.val = num;
        this.next = null;
    }
}


class SLL{
    constructor(num){
        this.head = new Node(num);
    }


    insert_at_start = function(num){
        var node = new Node(num);
        if(this.head == null){
            head = Node(num);
            return;
        }

        node.next = this.head;

        this.head = new Node(node.val);
        this.head.next = node.next;
    }

    insert_at_end = function(num){
        var node = new Node(num);
        var itr = this.head;
        while(itr.next != null){
            itr = itr.next;
        }

        itr.next = node;
    }

    show = function(){
        var itr = this.head;
        var line = "";
        while(itr != null){
            line += itr.val;
            line += "->";
            itr = itr.next;
        }


        console.log(line.slice(0, -2));
    }

    length = function(){
        var itr = this.head;
        var count = 0;
        while(itr != null){
            count += 1;
            itr = itr.next;
        }

        return count;
    }


    remove_at_index = function(index){
        var itr = this.head;
        if(index == 0){
            var begin = itr.next.val;
            this.head = new Node(begin);
            this.head.next = itr.next.next;
            return;
        }
    }

    insert_at = function(index, val){
        var itr = this.head;
        if(index == 0){
            this.head = new Node(val);
            this.head.next= itr;
            return;
        }

        for(let i=0; i<index; i++){
            itr = itr.next;
        }

        var temp = itr;
        // console.log(itr.val);
        itr = new Node(val);
        itr.next = temp;
        console.log(itr.val);
    }

    sort = function(){
        var sorted = false;
        while(!(sorted)){
            sorted = true;
            var itr = this.head;
            while(itr.next != null){
                if(itr.val > itr.next.val){
                    sorted = false;
                    var temp = itr.val;
                    itr.val = itr.next.val;
                    itr.next.val = temp;
                }
                itr = itr.next;
            }
        }
    }

    reverse = function(){
        var sorted = false;
    }
}


var sll = new SLL(1);

sll.insert_at_start(2);

sll.show();

sll.insert_at_end(4);

sll.show();

console.log(sll.length());

sll.insert_at(0, 6);

sll.insert_at(2, 9);

sll.show();
