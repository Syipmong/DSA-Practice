class Queue{

    constructor(){
        this.items = [];
    }
    add(item){
        this.items.push(item);
    }

    size(){
        return this.items.length;
    }

    isEmpty(){
        return this.items.length == 0;
    }

    remove(){
        if(this.isEmpty()){
            return "Underflow";
        }
        return this.items.shift();

    }
}


q = new Queue();

q.add(1);
q.add(2);
q.add(3);
q.add(4);
console.log(q.size())
q.remove()
q.add(5);
q.add(6);
q.add(7);
console.log(q.size())
q.remove()
console.log(q.size())