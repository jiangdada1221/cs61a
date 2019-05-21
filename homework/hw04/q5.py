def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n,start,end):
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "you are stupid"
    if n == 2:
        print_move(start,6-start-end)
        print_move(start,end)
        print_move(6-start-end,end)
    else:
        move_stack(n-1,start,6-start-end)
        print_move(start,end)
        move_stack(n-1,6-start-end,end)     #汉诺塔问题 要将最底下的那个取出，其余的都得在中转杆上，即move_stack(n-1,start,6-start-end)
                                            #然后print_move(start,end)
                                            #再把中转站上的移到终点 move_stack(n-1,6-start-end,end)
