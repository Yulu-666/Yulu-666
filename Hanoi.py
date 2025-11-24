step_count = 0
def hanoi(n, a, b, c):
    global step_count
    if n == 1:
        global step_count
        step_count += 1
    else:
        hanoi(n - 1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n -1, b, a, c)
    
    return step_count
print(hanoi(4, "a", "b", "c"))