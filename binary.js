function bin(list, num){
    let left = 0;
    let right = list.length -1;
    while (left <= right) {
        let mid = Math.floor((right + left)/2);
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

// console.log(bin([4,5,6,7,8,9,2,1], 1)); 


function myBin(newList, n)
{
    let left = 0;
    let right = newList.length -1;
    while(left <= right)
     {
        let mid = Math.floor((left + right)/2);
        if(n < newList[mid])
        {
            return right -1;
        }
        else if( n > newList[mid])
        {
            return left + 1;
        }
        else if ( n === newList[mid] )
        {
            return mid ;
        }
        else
        {
            return "Number doesnt exist";
        }
     }
}

// console.log(myBin([7,5,3,4,8,1,6],8))


function myBin(newList, n) 
{
    let left = 0;
    let right = newList.length - 1;
    while (left <= right) 
    {
        let mid = Math.floor((left + right) / 2);
        if (n < newList[mid]) 
        {
            right = mid - 1;
            return right;
        }
        else if (n > newList[mid]) 
        {
            left = mid + 1;
            return left;
        } 
        else if (n === newList[mid]) 
        {
            return mid;
        }
    }
    return `Number doesn't exist ${n}`;
}

console.log(myBin([7, 5, 3, 4, 8, 1, 6], 8));




// console.log(bin([7,5,3,4,8,1,6],5))
