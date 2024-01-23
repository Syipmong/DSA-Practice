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

    
}