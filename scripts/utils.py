from math import sin, cos

'''
`g` is gravity
`m1` and `m2` is masses
`l1` and `l2` is lengths
`a1` and `a2` is angles
`a_v1` and `a_v2` is angular velocities
'''

def first_acceleration(g, m1, m2, l1, l2, a1, a2, a_v1, a_v2) -> float:
    num1 = -g * (2 * m1 + m2) * sin(a1)
    num2 = -m2 * g * sin(a1 - 2 * a2)
    num3 = -2 * sin(a1 - a2) * m2
    num4 = a_v2 * a_v2 * l2 + a_v1 * a_v1 * l1 * cos(a1 - a2)

    numerator = num1 + num2 + num3 * num4
    denominator = l1 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2))

    return numerator / denominator

def second_acceleration(g, m1, m2, l1, l2, a1, a2, a_v1, a_v2) -> float:
    num1 = 2 * sin(a1 - a2)
    num2 = (a_v1 * a_v1 * l1 * (m1 + m2))
    num3 = g * (m1 + m2) * cos(a1)
    num4 = a_v2 * a_v2 * l2 * m2 * cos(a1 - a2)

    numerator = num1 * (num2 + num3 + num4)
    denominator = l2 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2))

    return numerator / denominator
