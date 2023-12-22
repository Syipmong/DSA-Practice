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


function myBin(newList, n)
{
    var left = 0;
    var right = newList.length -1;
    while(left <= right)
     {
        var mid = 
     }
}