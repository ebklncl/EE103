num = int(input("Enter a number to calculate the sum: "))
total_sum = 0
for i in range(1, num):
    total_sum += i
sum_gauss = num * (num + 1) / 2
if total_sum == sum_gauss:
    print("My running sum code works correctly")
else:
    print("My running sum code failed badly")

