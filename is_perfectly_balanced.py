def is_perfectly_balanced(input_str):
    count_index = {}
    for i in input_str:
        if i in count_index:
            count_index[i] += 1
        else:
            count_index[i] = 1
    
    max_time = max(list(count_index.values()))
    min_time = min(list(count_index.values()))
    count_max = list(count_index.values()).count(max_time)
    count_min = list(count_index.values()).count(min_time)
    if count_max == len(list(count_index.values())) or count_max == len(list(count_index.values())) - 1 and min_time == 1:
        print('YES')
        return True
            
    if count_min == len(list(count_index.values())) or count_min == len(list(count_index.values())) - 1 and max_time - 1 == min_time:
        print('YES')
        return True
    
    print('NO')
    return False
