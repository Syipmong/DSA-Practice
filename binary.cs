// binary search

using System;

class BinarySearch {
    static void Main(string[] args) {
        int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8 };
        int key = 5;
        int index = PerformBinarySearch(arr, key);
        Console.WriteLine("Index of {0} is {1}", key, index);
        Console.ReadKey();
    }

    static int PerformBinarySearch(int[] arr, int key) {
        int min = 0;
        int max = arr.Length - 1;
        while (min <= max) {
            int mid = (min + max) / 2;
            if (key == arr[mid]) {
                return mid;
            } else if (key < arr[mid]) {
                max = mid - 1;
            } else {
                min = mid + 1;
            }
        }
        return -1; // Return -1 if the key is not found
    }
}