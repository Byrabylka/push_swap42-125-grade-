def check_move():
    letters = ['A','B','C','D','E','F','G','H']
    digits = [str(i) for i in range(1,9)]
    move = input()
    if len(move) != 5:
        print("ERROR")
        return 
    if letters.count(move[0])== 0 or letters.count(move[3]) == 0 or digits.count(move[1])== 0 or digits.count(move[4]) == 0 or move[2] != '-':
        print("ERROR")
        return
    d1, d2 = letters.index(move[0]) - letters.index(move[3]), int(move[1]) - int(move[4])
    if abs(d1 * d2) != 2:
        print("NO")
        return
    print("YES")


check_move()