hour = 12
min = 15

hour_hand_coords = {}

center = {
    'x': 0,
    'y': 0,
    'time': 1,
}


def get_coords_in_between(val, r, center_x, center_y, max_x, max_y, mode='minute'):
    arr = [[max_x, max_y]]

    sep = 2
    if mode == 'minute':
        redun = 2 + (2 * sep)
    elif mode == 'hour':
        redun = 2 + sep
    else:
        redun = 2

    if val in (0, 12, 3, 6, 9):
        sep += sep
        redun += int(sep/2)

    if val is 0 or val is 12:
        for i in range(sep, redun + sep):
            arr.append([max_x, max_y + i])
    elif val is 6:
        for i in range(sep, redun + sep):
            arr.append([max_x, max_y - i])

    elif val is 3:
        for i in range(sep, redun + sep):
            arr.append([max_x - i, max_y])
    elif val is 9:
        for i in range(sep, redun + sep):
            arr.append([max_x + i, max_y])

    elif val is 1 or val is 2:
        for i in range(sep, redun + sep):
            arr.append([max_x - i, max_y + i])

    elif val is 4 or val is 5:
        for i in range(sep, redun + sep):
            arr.append([max_x - i, max_y - i])

    elif val is 10 or val is 11:
        for i in range(sep, redun + sep):
            arr.append([max_x + i, max_y + i])

    elif val is 7 or val is 8:
        for i in range(sep, redun + sep):
            arr.append([max_x + i, max_y - i])

    return arr


def init(r):
    mid = r - int(r / 2)
    center_x = center['x'] = mid
    center_y = center['y'] = mid
    mid_by_3 = int(mid / 3)

    for i in range(0, 12):
        hour_hand_coords[i] = []

        if i is 0 or 12:
            max_x = mid
            max_y = 1

        if i is 6:
            max_x = mid
            max_y = r

        if i is 3:
            max_x = r
            max_y = mid

        if i is 9:
            max_x = 1
            max_y = mid

        if i is 1:
            max_x = mid + (1 * mid_by_3)
            max_y = 1 + (1 * mid_by_3)

        if i is 11:
            max_x = mid - (1 * mid_by_3)
            max_y = 1 + (1 * mid_by_3)

        if i is 2:
            max_x = mid + (2 * mid_by_3)
            max_y = 1 + (2 * mid_by_3)

        if i is 10:
            max_x = mid - (2 * mid_by_3)
            max_y = 1 + (2 * mid_by_3)

        if i is 4:
            max_x = mid + (2 * mid_by_3)
            max_y = mid + (1 * mid_by_3)

        if i is 8:
            max_x = mid - (2 * mid_by_3)
            max_y = mid + (1 * mid_by_3)

        if i is 5:
            max_x = mid + (1 * mid_by_3)
            max_y = mid + (2 * mid_by_3)

        if i is 7:
            max_x = mid - (1 * mid_by_3)
            max_y = mid + (2 * mid_by_3)

        hour_hand_coords[i] = get_coords_in_between(i, r, center_x, center_y, max_x, max_y)

    # for i in range(0, 12):
        # print(i, "\t", hour_hand_coords[i])


def can_i_print(r, xpos, ypos):
    # print("xpos\t", xpos, "\typos\t", ypos)
    # if xpos == center['x'] and ypos == center['y']:
    #     return True

    from datetime import datetime
    dt_hour = datetime.now().hour
    if dt_hour > 12:
        dt_hour = abs(12 - dt_hour)

    for pair in hour_hand_coords[center['time']]:
        if xpos == pair[0] and ypos == pair[1]:
            return True

    return False

