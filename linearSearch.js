function linearSearch(list, num){
    for(n in list){
        if (list[n] == num) {
            return n;
            }
    }
}

console.log(linearSearch([1,4,2,3,7,5],4))