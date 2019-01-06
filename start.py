import clock_maker as cm
from time import sleep


def priLn():
    print('\n')


def priDot():
    print('*    ', end='', flush=True)
    pass


def priHash():
    print('#    ', end='', flush=True)
    pass


def priBlank():
    print('     ', end='', flush=True)
    pass


def print_matrix():
    r = 61
    i = r
    while i > 0:
        priLn()
        j = r
        while j > 0:
            priDot()
            j = j - 1
        i = i - 1
    print('\n')


def print_90_degree_rotated_matrix():
    r = 61
    mid = r - int(r / 2)
    # print('mid\t', mid)

    cm.init(r)

    ypos = 1
    xpos = 1
    row = 0
    while row < mid:
        xpos = 1
        row = row + 1
        spacing = mid - row
        pts_to_print = (2 * row) - 1
        # print("spacing\t", spacing, "\tpts_to_print\t", pts_to_print)
        priLn()
        t = 0
        while t < spacing:
            priBlank()
            t = t + 1
            xpos += 1

        t = 1
        while t <= pts_to_print:
            if cm.can_i_print(r, xpos=xpos, ypos=ypos):
                priHash()
            elif t is 1 or t is pts_to_print:
                priDot()
            else:
                priBlank()
            t = t + 1
            xpos += 1
        ypos += 1

    while row > 0:
        xpos = 1
        row = row - 1
        spacing = mid - row
        pts_to_print = (2 * row) - 1
        # print("spacing\t", spacing, "\tpts_to_print\t", pts_to_print)
        priLn()
        t = 0
        while t < spacing:
            priBlank()
            t = t + 1
            xpos += 1

        t = 1
        while t <= pts_to_print:
            if cm.can_i_print(r, xpos=xpos, ypos=ypos):
                priHash()
            elif t is 1 or t is pts_to_print:
                priDot()
            else:
                priBlank()
            t = t + 1
            xpos += 1
        ypos += 1

    priLn()


def print_whole_circle_matrix():
    r = 41
    max_redundancy = 2

    cm.init(r)

    mid = r - int(r / 2)
    mid2 = int(mid / 2)
    print('mid\t', mid, "\tmid2\t", mid2, "\tmax_redundancy\t", max_redundancy)

    # circle_spacer = [1, 2, 2, 3, 3, 4, 3, 3, 2, 2, 1]
    circle_spacer = []
    t = 1
    redun = 1
    for i in range(1, mid + 1):
        circle_spacer.append(t)
        if redun >= max_redundancy:
            redun = 0
            if i < mid2:
                t = t + 1
            else:
                t = t - 1

        redun += 1

    print("spc\t", circle_spacer, "\nspc_len\t", len(circle_spacer))
    # return

    ypos = 1
    xpos = 1
    row = 0
    while row < mid:
        xpos = 1
        row = row + 1

        pts_to_print = ((2 * row) - 1) + (2 * circle_spacer[row - 1])
        spacing = int((r - pts_to_print))
        if spacing < 0:
            spacing = int((abs(spacing) / 2) * (-1))
        else:
            spacing = int((abs(spacing) / 2))
        # print("row\t", row, "\tspacing\t", spacing, "\tpts_to_print\t", pts_to_print, "\tcircle_spacer\t",
        #       circle_spacer[row - 1])
        priLn()
        t = 0
        while t < (spacing + 3):
            priBlank()
            t = t + 1
            xpos += 1

        t = 0
        while t < pts_to_print:
            if cm.can_i_print(r, xpos=xpos, ypos=ypos):
                priHash()
            elif t is 1 or t is pts_to_print:
                priDot()
            else:
                priBlank()
            t = t + 1
            xpos += 1
        ypos += 1

    while row > 0:
        xpos = 1
        row = row - 1

        pts_to_print = ((2 * row) - 1) + (2 * circle_spacer[row - 1])
        spacing = int((r - pts_to_print))
        if spacing < 0:
            spacing = int((abs(spacing) / 2) * (-1))
        else:
            spacing = int((abs(spacing) / 2))
        # print("row\t", row, "\tspacing\t", spacing, "\tpts_to_print\t", pts_to_print, "\tcircle_spacer\t",
        #       circle_spacer[row - 1])
        priLn()
        t = 0
        while t < spacing:
            priBlank()
            t = t + 1
            xpos += 1

        t = 0
        while t < pts_to_print:
            if cm.can_i_print(r, xpos=xpos, ypos=ypos):
                priHash()
            elif t is 1 or t is pts_to_print:
                priDot()
            else:
                priBlank()
            t = t + 1
            xpos += 1
        ypos += 1

    priLn()


def print_hollow_circle_matrix():
    r = 41
    max_redundancy = 2

    cm.init(r)

    mid = r - int(r / 2)
    mid2 = int(mid / 2)
    # print('mid\t', mid, "\tmid2\t", mid2, "\tmax_redundancy\t", max_redundancy)

    # circle_spacer = [1, 2, 2, 3, 3, 4, 3, 3, 2, 2, 1]
    circle_spacer = []
    t = 1
    redun = 1
    for i in range(1, mid + 1):
        circle_spacer.append(t)
        if redun >= max_redundancy:
            redun = 0
            if i < mid2:
                t = t + 1
            else:
                t = t - 1

        redun += 1

    # print("spc\t", circle_spacer, "\nspc_len\t", len(circle_spacer))
    # return

    ypos = 1
    xpos = 1
    row = 0
    while row < mid:
        xpos = 1
        row = row + 1

        pts_to_print = ((2 * row) - 1) + (2 * circle_spacer[row - 1])
        spacing = int((r - pts_to_print))
        if spacing < 0:
            spacing = int((abs(spacing) / 2) * (-1))
        else:
            spacing = int((abs(spacing) / 2))
        # print("row\t", row, "\tspacing\t", spacing, "\tpts_to_print\t", pts_to_print, "\tcircle_spacer\t",
        #       circle_spacer[row - 1])
        priLn()
        t = 0
        while t < spacing:
            priBlank()
            t = t + 1
            xpos += 1

        t = 1
        while t <= pts_to_print:
            if cm.can_i_print(r, xpos=xpos, ypos=ypos):
                priHash()
            elif t is 1 or t is pts_to_print:
                priDot()
            else:
                priBlank()
            t = t + 1
            xpos += 1
        ypos += 1

    while row > 0:
        xpos = 1
        row = row - 1

        pts_to_print = ((2 * row) - 1) + (2 * circle_spacer[row - 1])
        spacing = int((r - pts_to_print))
        if spacing < 0:
            spacing = int((abs(spacing) / 2) * (-1))
        else:
            spacing = int((abs(spacing) / 2))
        # print("row\t", row, "\tspacing\t", spacing, "\tpts_to_print\t", pts_to_print, "\tcircle_spacer\t",
        #       circle_spacer[row - 1])
        priLn()
        t = 0
        while t < spacing:
            priBlank()
            t = t + 1
            xpos += 1

        t = 1
        while t <= pts_to_print:
            if cm.can_i_print(r, xpos=xpos, ypos=ypos):
                priHash()
            elif t is 1 or t is pts_to_print:
                priDot()
            else:
                priBlank()
            t = t + 1
            xpos += 1
        ypos += 1

    priLn()


while True:
    print_hollow_circle_matrix()
    sleep(1)
    cm.center['time'] += 1
    if cm.center['time'] > 11:
        cm.center['time'] = 0
