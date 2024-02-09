# num_rows = int(input())
# left_sum = 0
# right_sum = 0
# for num in range(num_rows):
#     number = int(input())
#     left_sum += number
# for num in range(num_rows):
#     number = int(input())
#     right_sum += number
#
# if left_sum == right_sum:
#     print(f"Yes, sum = {left_sum}")
# else:
#     diff = abs(left_sum - right_sum)
#     print(f"No, diff = {diff}")

num_rows = int(input())
even_sum = 0
odd_sum = 0
for num in range(num_rows):
    number = int(input())
    if num % 2 == 0:
        even_sum += number
    else:
        odd_sum += number
if even_sum == odd_sum:
    print(f"Yes\nSum = {even_sum}")
else:
    diff = abs(even_sum - odd_sum)
    print(f"No\nDiff = {diff}")
