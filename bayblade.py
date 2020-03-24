q = int(input())

size = int(input())

team_a = sorted([ int(str(i).strip()) for i in str(input()).strip().split(" ")])

team_b = sorted([ int(str(i).strip()) for i in str(input()).strip().split(" ")])



for i in range(0, q):
    m_b = 0
    possible_wins = 0
    for power in team_a:
        if power > team_b[m_b]:
            possible_wins += 1
            m_b+=1

    print(possible_wins)
        