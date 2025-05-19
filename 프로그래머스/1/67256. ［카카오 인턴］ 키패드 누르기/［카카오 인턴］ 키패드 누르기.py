def solution(numbers, hand):
    answer = ''
    keypad = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
    left_loc = (3,0)
    right_loc = (3,2)
    
    left_list = [1,4,7]
    right_list = [3,6,9]
    
    def get_yx(val):
        y,x = 0,0
        for i,v in enumerate(keypad):
            if val in v:
                y = i
                x = v.index(val)
        return (y,x)
    
    for v in numbers:
        if v in left_list:
            answer += "L"
            left_loc = get_yx(v)
        elif v in right_list:
            answer += "R"
            right_loc = get_yx(v)
        else:
            middle_loc = get_yx(v)
            left_d = abs(left_loc[0] - middle_loc[0]) + abs(left_loc[1] - middle_loc[1])
            right_d = abs(right_loc[0] - middle_loc[0]) + abs(right_loc[1] - middle_loc[1])
            if left_d < right_d:
                answer += "L"
                left_loc = middle_loc
                
            elif left_d > right_d:
                answer += "R"
                right_loc = middle_loc
            else:
                if hand == "right":
                    answer += "R"
                    right_loc = middle_loc
                else:
                    answer += "L"
                    left_loc = middle_loc

    return answer