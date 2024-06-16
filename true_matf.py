
def divide(first, second):
    from math import inf
    if first >= 0 and second > 0:
        div = first / second
        return div
    if second == 0:
        return inf


divide(17, 0)