class Queue{

    constructor(){
        this.items = [];
    }
    enqueue(item){
        this.items.push(item);
    }

    size(){
        return this.items.length;
    }

    isEmpty(){
        return this.items.length == 0;
    }

    dequeue(){
        if(this.isEmpty()){
            return "Underflow";
        }
        return this.items.shift();

    }
    front(){
        if(this.isEmpty()){
            return "No elements in Queue"
        }
        return this.items[0]
        
    }
    display(){
        return this.items
    }
}


q = new Queue();

q.enqueue(1);
q.enqueue(2);
q.enqueue(3);
q.enqueue(4);
console.log(q.size())