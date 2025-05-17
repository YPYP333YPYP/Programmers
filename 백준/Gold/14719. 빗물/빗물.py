H, W = map(int, input().split())
block = list(map(int, input().split()))

left_max = [0] * W
left_max[0] = block[0]
for i in range(1, W):
    left_max[i] = max(left_max[i-1], block[i])

right_max = [0] * W
right_max[W-1] = block[W-1]
for i in range(W-2, -1, -1):
    right_max[i] = max(right_max[i+1], block[i])

result = 0
for i in range(W):
    water_level = min(left_max[i], right_max[i])
    result += max(0, water_level - block[i])

print(result)