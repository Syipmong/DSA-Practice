function linearSearch(list, num){
    for(num in list){
        if (list[num] == num) {
            return num;
            }
    }
}

console.log(linearSearch([1,4,2,3,7,5],5))