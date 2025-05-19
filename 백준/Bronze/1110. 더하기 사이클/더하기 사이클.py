n = int(input())
number = n
cnt = 0

while True:
    # 문자열로 변환
    number_str = str(number)
    if len(number_str) == 1:  # 한 자리 수인 경우
        number_str = "0" + number_str

    # 각 자리 숫자의 합
    digit_sum = int(number_str[0]) + int(number_str[1])

    # 새로운 수 생성
    number = int(number_str[1] + str(digit_sum)[-1])

    cnt += 1

    if number == n:
        break

print(cnt)