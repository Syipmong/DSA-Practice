function bin(list, num){
    var left = 0;
    var right = list.length -1;
    while (left <= right) {
        var mid = Math.floor((right + left)/2);
        if (num === list[mid]){
            return mid;
        }
        else if (num > list[mid]){
            left = mid + 1;
        }
        else{
            right = mid - 1;
        }
    }
}
console.log(bin([4,6,8,9,13], 9)); 