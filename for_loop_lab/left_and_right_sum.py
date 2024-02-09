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
left_sum = 0
right_sum = 0
for num in range(2 * num_rows):
    number = int(input())
    if num < num_rows:
        left_sum += number
    else:
        right_sum += number
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")





























































