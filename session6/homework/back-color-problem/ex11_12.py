def is_inside(point, rec):
    m = point[0]
    n = point[1]

    x = rec[0]
    y = rec[1]
    z = rec[2]
    t = rec[3]
    return (m >= x and m <= x + z and n >= y and n <= y + t)

# x = is_inside([200,120],[140,60,100,200])
# print(x)
