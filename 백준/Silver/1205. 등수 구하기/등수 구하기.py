N, score, P = map(int, input().split())

if N == 0:
    print(1)
else:
    scores = list(map(int, input().split()))

    rank = 1

    for s in scores:
        if s > score:
            rank += 1

    if N == P and scores[-1] >= score:
        print(-1)
    else:
        print(rank)