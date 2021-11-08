#  Prominent Arduino map function :)
def _map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
# TEST
y = _map(0.2, -2, 2, 0, 480)
print(y)