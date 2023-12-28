#!/bin/bash
# code goes here
echo "Enter the number of rows you want in your matrix: "
read numrows
echo "Enter the number of columns you want in your matrix: "
read numcols
if [ $numrows -le 0 ] || [ $numcols -le 0 ]; then
echo "Invalid input. Please enter a positive integer for both dimensions."
else
matrix=$(printf "%*s\n" $((numcols + 1)) | tr ' ' '.')
for ((i=1; i<=numrows; i++)); do
echo "$((RANDOM % 9 + 1))$matrix" | sed "s/\.$//"
done
