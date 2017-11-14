
def naive(number):
    values = {'tank': 5000, 'car': 1000, 'human': 80}
    diffs = {}
    for key, value in list(values.items()):
        if int(number/value) == 0:
            del values[key]
    for key, value in values.items():
        diff = abs(int(number/value) - number/value)
        diffs[key] = diff

    best = min(diffs, key=lambda x: x[1])

    print("That's approximately weight of %d %s" % (int(number / values[best]), best) + "s.")

naive(10000)
