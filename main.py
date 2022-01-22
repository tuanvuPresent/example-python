def is_perfectly_balanced(input_str):
    if(len(input_str) == 1):
        print('YES')
        return True
    
    count_index = {}
    for i in input_str:
        if i in count_index:
            count_index[i] += 1
        else:
            count_index[i] = 1
    
    min_time  = min(list(count_index.values()))
    different_count = 0
    for value in count_index.values():
        if value != min_time and value - min_time > 1:
            print('NO')
            return False
        if value != min_time and value - min_time == 1:
            different_count += 1
        
        if different_count == 2:
            print('NO')
            return False
            
    print('YES')
    return True
is_perfectly_balanced('abc')
is_perfectly_balanced('abcc')
is_perfectly_balanced('abcddeee')