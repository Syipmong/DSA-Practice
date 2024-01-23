class Box{
    constructor(){
        this.vertices = [];
        this.edges = [];
        this.faces = [];
        this.l1 = null;
        this.l2 = null;
        this.l3 = null;
        this.l4 = null;

    }

    vertices(l1,l2,l3,l4){
        this.l1 = l1;
        this.l2 = l2;
        this.l3 = l3;
        this.l4 = l4;
    }
    edges(){
        this.edges.push(this.l1);
        this.edges.push(this.l2);
        this.edges.push(this.l3);
        this.edges.push(this.l4);
    }
    faces(){
        this.faces.push(this.l1);
        this.faces.push(this.l2);
        this.faces.push(this.l3);
        this.faces.push(this.l4);
    }
    // insert at a given index
    insert(index, value){
        if(index >= this.length){
            return this.append(value);
        }
        const newNode = {value: value, next: null};
        const leader = this.traverseToIndex(index-1);
        const holdingPointer = leader.next;
        leader.next = newNode;
        newNode.next = holdingPointer;
        this.length++;
    }
    // remove at a given index
    remove(index){
        if(index >= this.length){
            return;
        }
        const leader = this.traverseToIndex(index-1);
        const unwantedNode = leader.next;
        leader.next = unwantedNode.next;
        this.length--;
    }
    // traverse to a given index
    traverseToIndex(index){
        let counter = 0;
        let currentNode = this.head;
        while(counter !== index){
            currentNode = currentNode.next;
            counter++;
        }
        return currentNode;
    }


}