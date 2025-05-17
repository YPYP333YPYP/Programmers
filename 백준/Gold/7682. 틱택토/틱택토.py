while True:
    string = str(input())
    if string == "end":
        break

    # 배열 초기화 및 X, O 개수 세기
    board = []
    o_cnt = 0
    x_cnt = 0

    for i in range(3):
        row = []
        for j in range(3):
            ch = string[i * 3 + j]
            if ch == 'O':
                o_cnt += 1
            elif ch == 'X':
                x_cnt += 1
            row.append(ch)
        board.append(row)


    # 승리 조건 확인 함수
    def check_win(player):
        # 가로 확인
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True

        # 세로 확인
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True

        # 대각선 확인
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True

        return False


    x_win = check_win('X')
    o_win = check_win('O')

    # 유효성 판단
    valid = False

    if o_win and not x_win and o_cnt == x_cnt:
        valid = True

    elif x_win and not o_win and x_cnt == o_cnt + 1:
        valid = True

    elif not o_win and not x_win and o_cnt == 4 and x_cnt == 5:
        valid = True

    if valid:
        print("valid")
    else:
        print("invalid")