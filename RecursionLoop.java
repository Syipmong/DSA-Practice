public class RecursionLoop {
    public int num;


    int doRecursion(int num)
    {
        this.num = num;
        while (this.num > 1) {
            return doRecursion(num - 1) * num;
        }
        return this.num;
    }

    
}
