def init_cube():
    # 큐브 초기화: 각 면을 해당 색상으로 채움
    cube = {}
    cube['U'] = [['w' for _ in range(3)] for _ in range(3)]  # 윗면 - 흰색
    cube['D'] = [['y' for _ in range(3)] for _ in range(3)]  # 아랫면 - 노란색
    cube['F'] = [['r' for _ in range(3)] for _ in range(3)]  # 앞면 - 빨간색
    cube['B'] = [['o' for _ in range(3)] for _ in range(3)]  # 뒷면 - 오렌지색
    cube['L'] = [['g' for _ in range(3)] for _ in range(3)]  # 왼쪽면 - 초록색
    cube['R'] = [['b' for _ in range(3)] for _ in range(3)]  # 오른쪽면 - 파란색
    return cube

def rotate_face(face, dir):
    # 면 자체 회전
    n = 3
    result = [[0] * n for _ in range(n)]
    
    if dir == '+':  # 시계 방향
        for i in range(n):
            for j in range(n):
                result[j][n-1-i] = face[i][j]
    else:  # 반시계 방향
        for i in range(n):
            for j in range(n):
                result[n-1-j][i] = face[i][j]
    
    return result

def rotate(cube, face, dir):
    # 면 회전
    cube[face] = rotate_face(cube[face], dir)
    
    # 회전에 따른 인접 면 변경
    if face == 'U':
        # 윗면 회전 시 F, L, B, R의 윗줄이 변경됨
        rows = []
        rows.append([cube['F'][0][0], cube['F'][0][1], cube['F'][0][2]])
        rows.append([cube['L'][0][0], cube['L'][0][1], cube['L'][0][2]])
        rows.append([cube['B'][0][0], cube['B'][0][1], cube['B'][0][2]])
        rows.append([cube['R'][0][0], cube['R'][0][1], cube['R'][0][2]])
        
        if dir == '+':  # 시계방향 (F->R->B->L->F)
            cube['F'][0] = rows[3]  # R의 윗줄이 F의 윗줄로
            cube['R'][0] = rows[2]  # B의 윗줄이 R의 윗줄로
            cube['B'][0] = rows[1]  # L의 윗줄이 B의 윗줄로
            cube['L'][0] = rows[0]  # F의 윗줄이 L의 윗줄로
        else:  # 반시계방향 (F->L->B->R->F)
            cube['F'][0] = rows[1]  # L의 윗줄이 F의 윗줄로
            cube['L'][0] = rows[2]  # B의 윗줄이 L의 윗줄로
            cube['B'][0] = rows[3]  # R의 윗줄이 B의 윗줄로
            cube['R'][0] = rows[0]  # F의 윗줄이 R의 윗줄로
            
    elif face == 'D':
        # 아랫면 회전 시 F, R, B, L의 아랫줄이 변경됨
        rows = []
        rows.append([cube['F'][2][0], cube['F'][2][1], cube['F'][2][2]])
        rows.append([cube['R'][2][0], cube['R'][2][1], cube['R'][2][2]])
        rows.append([cube['B'][2][0], cube['B'][2][1], cube['B'][2][2]])
        rows.append([cube['L'][2][0], cube['L'][2][1], cube['L'][2][2]])
        
        if dir == '+':  # 시계방향 (F->L->B->R->F)
            cube['F'][2] = rows[3]  # L의 아랫줄이 F의 아랫줄로
            cube['L'][2] = rows[2]  # B의 아랫줄이 L의 아랫줄로
            cube['B'][2] = rows[1]  # R의 아랫줄이 B의 아랫줄로
            cube['R'][2] = rows[0]  # F의 아랫줄이 R의 아랫줄로
        else:  # 반시계방향 (F->R->B->L->F)
            cube['F'][2] = rows[1]  # R의 아랫줄이 F의 아랫줄로
            cube['R'][2] = rows[2]  # B의 아랫줄이 R의 아랫줄로
            cube['B'][2] = rows[3]  # L의 아랫줄이 B의 아랫줄로
            cube['L'][2] = rows[0]  # F의 아랫줄이 L의 아랫줄로
            
    elif face == 'F':
        # 앞면 회전 시 U, R, D, L의 일부가 변경됨
        if dir == '+':  # 시계방향
            # 임시 저장
            temp_u = [cube['U'][2][0], cube['U'][2][1], cube['U'][2][2]]
            temp_r = [cube['R'][0][0], cube['R'][1][0], cube['R'][2][0]]
            temp_d = [cube['D'][0][2], cube['D'][0][1], cube['D'][0][0]]
            temp_l = [cube['L'][2][2], cube['L'][1][2], cube['L'][0][2]]
            
            # 변경
            cube['U'][2][0], cube['U'][2][1], cube['U'][2][2] = temp_l
            cube['R'][0][0], cube['R'][1][0], cube['R'][2][0] = temp_u
            cube['D'][0][2], cube['D'][0][1], cube['D'][0][0] = temp_r
            cube['L'][2][2], cube['L'][1][2], cube['L'][0][2] = temp_d
        else:  # 반시계방향
            # 임시 저장
            temp_u = [cube['U'][2][0], cube['U'][2][1], cube['U'][2][2]]
            temp_r = [cube['R'][0][0], cube['R'][1][0], cube['R'][2][0]]
            temp_d = [cube['D'][0][2], cube['D'][0][1], cube['D'][0][0]]
            temp_l = [cube['L'][2][2], cube['L'][1][2], cube['L'][0][2]]
            
            # 변경
            cube['U'][2][0], cube['U'][2][1], cube['U'][2][2] = temp_r
            cube['R'][0][0], cube['R'][1][0], cube['R'][2][0] = temp_d
            cube['D'][0][2], cube['D'][0][1], cube['D'][0][0] = temp_l
            cube['L'][2][2], cube['L'][1][2], cube['L'][0][2] = temp_u
            
    elif face == 'B':
        # 뒷면 회전 시 U, L, D, R의 일부가 변경됨
        if dir == '+':  # 시계방향
            # 임시 저장
            temp_u = [cube['U'][0][2], cube['U'][0][1], cube['U'][0][0]]
            temp_l = [cube['L'][0][0], cube['L'][1][0], cube['L'][2][0]]
            temp_d = [cube['D'][2][0], cube['D'][2][1], cube['D'][2][2]]
            temp_r = [cube['R'][2][2], cube['R'][1][2], cube['R'][0][2]]
            
            # 변경
            cube['U'][0][2], cube['U'][0][1], cube['U'][0][0] = temp_r
            cube['L'][0][0], cube['L'][1][0], cube['L'][2][0] = temp_u
            cube['D'][2][0], cube['D'][2][1], cube['D'][2][2] = temp_l
            cube['R'][2][2], cube['R'][1][2], cube['R'][0][2] = temp_d
        else:  # 반시계방향
            # 임시 저장
            temp_u = [cube['U'][0][2], cube['U'][0][1], cube['U'][0][0]]
            temp_l = [cube['L'][0][0], cube['L'][1][0], cube['L'][2][0]]
            temp_d = [cube['D'][2][0], cube['D'][2][1], cube['D'][2][2]]
            temp_r = [cube['R'][2][2], cube['R'][1][2], cube['R'][0][2]]
            
            # 변경
            cube['U'][0][2], cube['U'][0][1], cube['U'][0][0] = temp_l
            cube['L'][0][0], cube['L'][1][0], cube['L'][2][0] = temp_d
            cube['D'][2][0], cube['D'][2][1], cube['D'][2][2] = temp_r
            cube['R'][2][2], cube['R'][1][2], cube['R'][0][2] = temp_u
            
    elif face == 'L':
        # 왼쪽면 회전 시 U, F, D, B의 일부가 변경됨
        if dir == '+':  # 시계방향
            # 임시 저장
            temp_u = [cube['U'][0][0], cube['U'][1][0], cube['U'][2][0]]
            temp_f = [cube['F'][0][0], cube['F'][1][0], cube['F'][2][0]]
            temp_d = [cube['D'][0][0], cube['D'][1][0], cube['D'][2][0]]
            temp_b = [cube['B'][2][2], cube['B'][1][2], cube['B'][0][2]]
            
            # 변경
            cube['U'][0][0], cube['U'][1][0], cube['U'][2][0] = temp_b
            cube['F'][0][0], cube['F'][1][0], cube['F'][2][0] = temp_u
            cube['D'][0][0], cube['D'][1][0], cube['D'][2][0] = temp_f
            cube['B'][2][2], cube['B'][1][2], cube['B'][0][2] = temp_d
        else:  # 반시계방향
            # 임시 저장
            temp_u = [cube['U'][0][0], cube['U'][1][0], cube['U'][2][0]]
            temp_f = [cube['F'][0][0], cube['F'][1][0], cube['F'][2][0]]
            temp_d = [cube['D'][0][0], cube['D'][1][0], cube['D'][2][0]]
            temp_b = [cube['B'][2][2], cube['B'][1][2], cube['B'][0][2]]
            
            # 변경
            cube['U'][0][0], cube['U'][1][0], cube['U'][2][0] = temp_f
            cube['F'][0][0], cube['F'][1][0], cube['F'][2][0] = temp_d
            cube['D'][0][0], cube['D'][1][0], cube['D'][2][0] = temp_b
            cube['B'][2][2], cube['B'][1][2], cube['B'][0][2] = temp_u
            
    elif face == 'R':
        # 오른쪽면 회전 시 U, B, D, F의 일부가 변경됨
        if dir == '+':  # 시계방향
            # 임시 저장
            temp_u = [cube['U'][0][2], cube['U'][1][2], cube['U'][2][2]]
            temp_b = [cube['B'][2][0], cube['B'][1][0], cube['B'][0][0]]
            temp_d = [cube['D'][0][2], cube['D'][1][2], cube['D'][2][2]]
            temp_f = [cube['F'][0][2], cube['F'][1][2], cube['F'][2][2]]
            
            # 변경
            cube['U'][0][2], cube['U'][1][2], cube['U'][2][2] = temp_f
            cube['B'][2][0], cube['B'][1][0], cube['B'][0][0] = temp_u
            cube['D'][0][2], cube['D'][1][2], cube['D'][2][2] = temp_b
            cube['F'][0][2], cube['F'][1][2], cube['F'][2][2] = temp_d
        else:  # 반시계방향
            # 임시 저장
            temp_u = [cube['U'][0][2], cube['U'][1][2], cube['U'][2][2]]
            temp_b = [cube['B'][2][0], cube['B'][1][0], cube['B'][0][0]]
            temp_d = [cube['D'][0][2], cube['D'][1][2], cube['D'][2][2]]
            temp_f = [cube['F'][0][2], cube['F'][1][2], cube['F'][2][2]]
            
            # 변경
            cube['U'][0][2], cube['U'][1][2], cube['U'][2][2] = temp_b
            cube['B'][2][0], cube['B'][1][0], cube['B'][0][0] = temp_d
            cube['D'][0][2], cube['D'][1][2], cube['D'][2][2] = temp_f
            cube['F'][0][2], cube['F'][1][2], cube['F'][2][2] = temp_u

# 메인 함수
t = int(input())
for _ in range(t):
    cube = init_cube()
    n = int(input())
    commands = input().split()
    
    for cmd in commands:
        face, dir = cmd[0], cmd[1]
        rotate(cube, face, dir)
    
    # 윗면 출력
    for i in range(3):
        print(''.join(cube['U'][i]))