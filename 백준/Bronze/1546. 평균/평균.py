N = int(input())

numbers = list(map(int, input().split()))

max_number = max(numbers)

new_numbers = list()
for v in numbers:
    val = v/max_number * 100
    val = round(val, 2)
    new_numbers.append(val)

avg = sum(new_numbers)/len(new_numbers)

print(avg)