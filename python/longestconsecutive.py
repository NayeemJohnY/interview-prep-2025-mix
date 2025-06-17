g_list = [1, 2, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4]
seq = {}
counter = 1
for i in range(1, len(g_list)):
    if i == len(g_list) - 1:
        print('ssss')
        print(g_list[i], g_list[i-1])
    if g_list[i] == g_list[i-1]:
        counter += 1
    else:
        seq[g_list[i-1]] = seq.get(g_list[i-1], counter)
        counter = 1

print(seq)
