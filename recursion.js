function recursion(n)
{
    while(n > 1)
    {
        return recursion(n - 1) * n;
    }
        return 1;
}

console.log(recursion(1))