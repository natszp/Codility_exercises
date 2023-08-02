#https://app.codility.com/programmers/trainings/7/count_bounded_slices/


def solution(array, k):
    n = len(array)
    counter = 0
    slices_list = []

    for i in range(n):
        minimum_i = array[i]
        maximum_i = array[i]
        for j in range(i, n):
            minimum = min(minimum_i, array[j])
            maximum = max(maximum_i, array[j])
            if maximum - minimum <= k:
                counter += 1
               # just to see slices by indexes
                slices_list.append((array.index(minimum), array.index(maximum)))
                print(slices_list)
            else:
                break

    return counter

#still not full correctness
