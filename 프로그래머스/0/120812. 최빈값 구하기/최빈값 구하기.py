# import numpy as np
# def solution(array):
#     answer = 0
#     for i in array:
#         if i == array.mode:
#             array.append(i)
#     return answer

# from scipy import stats
# import numpy as np

# def solution(array):
#     modem, i = stats.mode(array)
#     mst = mode[0]
#     answer = np.append(array, mst)
    
#     return answer

# from collection import Counter

# def solution(array):
    
#     counter = Counter(array)
#     mode = counter.most_common [0] [0]
#     array.append(mode)
    
#     return array

def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1