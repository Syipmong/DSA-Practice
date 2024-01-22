class LinkedList{
    constructor(){
        this.head = null;
        this.tail = null;
        this.length = 0; 

    }
    // add to the end of the list
    append(value){
        const newNode = {value: value, next: null};
        if(this.tail){
            this.tail.next = newNode;
        }
        this.tail = newNode;
        if(!this.head){
            this.head = newNode;
        }
        this.length++;
    }
    // add to the beginning of the list
    prepend(value){
        const newNode = {value: value, next: this.head};
        this.head = newNode;
        if(!this.tail){
            this.tail = newNode;
        }
        this.length++;
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
    // print the list
    printList(){
        const array = [];
        let currentNode = this.head;
        while(currentNode !== null){
            array.push(currentNode.value);
            currentNode = currentNode.next;
        }
        return array;
    }
    // reverse the list
    reverse(){
        if(!this.head.next){
            return this.head;
        }
        let first = this.head;
        this.tail = this.head;
        let second = first.next;
        while(second){
            const temp = second.next;
            second.next = first;
            first = second;
            second = temp;
        }
        this.head.next = null;
        this.head = first;
    }
}

const myLinkedList = new LinkedList();
myLinkedList.append(10);
myLinkedList.append(5);
myLinkedList.append(16);
myLinkedList.prepend(1);
myLinkedList.insert(2, 99);
myLinkedList.remove(2);
myLinkedList.reverse();
console.log(myLinkedList.printList());
console.log(myLinkedList);