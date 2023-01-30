from string import punctuation


def count_lines(name):
    with open(name) as f:
        rows = [l for l, _ in enumerate(f.readlines(), 1)]


def count_chars(name):
    with open(name) as f:
        counter = 0
        for i in f.read():
            if i in punctuation:
                counter += 1


def test(name):
    count_chars(name)
    count_lines(name)
