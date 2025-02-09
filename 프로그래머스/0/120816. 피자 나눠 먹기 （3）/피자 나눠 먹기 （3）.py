def solution(slice, n):
    if n <= slice:
        return 1
    elif n > slice:
        i = 2
        while True:
            if i * slice >= n:
                return i
                break
            i += 1