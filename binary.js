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
    return `Number ${n} doesn't exist`;
}

// console.log(myBin([15, 8, 2, 11, 19, 6, 4, 10, 5, 14, 1, 13, 7, 20, 3, 12, 18, 9, 17, 16], 2));




// console.log(bin([7,5,3,4,8,1,6],5))

// we had some inefficiency in our previous binary search and now we are to improve it
//we will be sorting our data to improve the efficiency of our data structure
