# def solution(array, height):
#     i = 0
#     for i in int(array):
#         if i > height:
#             return i.count()
#         else:
#             print(i)
            
def solution(array, height):
    count = 0
    for i in array:
        if i > height:
            count += 1
    return count