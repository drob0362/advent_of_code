def get_file_contents(filename):
    print("reading file {}".format(filename))
    with open(filename) as f:
        lines = f.readlines()

    return tuple(lines)