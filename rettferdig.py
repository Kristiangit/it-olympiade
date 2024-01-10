
list_length, turns = map(int, input().split())
number_list = []
#Arne er 1, Berit er -1
players = ["", 0, 0]
curr_player = 1
for i in range(list_length):
    number_list.append(int(input()))


done = False
curr = 0
for i in range(list_length):
    if i+1 >= list_length:
        if curr < list_length:
            players[curr_player] += number_list[curr]
        break
    if i < curr:
        continue

    num_total = [[number_list[i]], number_list[i]]
    ii = i+1
    next_num = number_list[ii]

    while num_total[-1] <= next_num:
        if ii +1 >= list_length:
            break
        if num_total[-1] + next_num >= number_list[ii+1]:
            if num_total[-1] + next_num == number_list[ii+1]:
                players[curr_player] += num_total[0][0]
                curr_player *= -1
                curr += 1
                done = True
            print("br", num_total[-1], next_num, number_list[ii+1], ii+1)
            break

        num_total[-1] += next_num
        num_total[0].append(next_num)
        ii += 1
        if ii +1 >= list_length:
            break
        next_num =  number_list[ii]

    if done:
        done = False
        continue
    curr = ii+1
    if (num_total[-1] > next_num and len(num_total[0]) == 1) or num_total[-1] == next_num:
        num_total[-1], next_num = 0, num_total[-1]
        curr = ii
        # curr = number_list.index(max(num_total[0]))

    players[curr_player] += next_num
    curr_player *= -1
    players[curr_player] += num_total[-1]

    print(num_total, next_num, players, curr, i, ii)
print(players[1], players[-1])

"""
7 1
1
1
3
5
4
3
6
"""
"""
8 1
9
8
7
7
5
4
3
1
"""
