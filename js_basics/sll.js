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
}


var sll = new SLL(1);

sll.insert_at_start(2);

sll.show();
