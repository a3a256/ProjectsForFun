class Node{
    constructor(num){
        this.val = num;
        this.next = null;
    }
}


class SLL{
    constructor(num){
        this.head = Node(num);
    }


    insert_at_start = function(num){
        var node = Node(num);
        if(head == null){
            head = Node(num);
            return;
        }

        node.next = head;

        head = Node(node.val);
        head.next = node.next;
    }
}