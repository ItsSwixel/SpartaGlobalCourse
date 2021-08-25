touch bash_results.txt
echo "Please enter your first number."
read first_num
echo "Please enter your second number."
read second_num
let sum=$first_num+$second_num
let sub=$first_num-$second_num
let mul=$first_num*$second_num
if [[ $first_num -ne 0 ]] && [[ $second_num -ne 0 ]]
then
let div=$first_num/$second_num
fi
echo $first_num "+" $second_num "=" $sum
echo $first_num "-" $second_num "=" $sub
echo $first_num "*" $second_num "=" $mul
echo $sum > bash_results.txt
echo $sub >> bash_results.txt
echo $mul >> bash_results.txt
if [[ $first_num -eq 0 ]] || [[ $second_num -eq 0 ]]
then
echo "It is not possible to divide with a 0"
else
echo $first_num "/" $second_num "=" $div
echo $div >> bash_results.txt
fi
