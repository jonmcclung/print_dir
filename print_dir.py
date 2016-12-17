import os, argparse


def get_prev(prev):
    res = ''
    for bar in prev[:-1]:
        res += ' |   ' if bar else '     '
    return res + (' |' if prev[-1] else ' +') + '-- '


def _print_file(file, prev):
    print(get_prev(prev) + file)


def _print_tree(path, files, prev=[]):
    prev.append(len(files))
    if files:
        for file in files:
            prev[-1] -= 1
            _print_file(file, prev)
            dirname = os.path.join(path, file)
            if os.path.isdir(dirname):
                _print_tree(dirname, os.listdir(dirname))
    prev.pop()


def print_tree(dir):
    print(dir)
    _print_tree(dir, os.listdir(dir))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='prints directory structures in pretty ASCII format')
    parser.add_argument('directory')
    dir = parser.parse_args().directory
    if os.path.isabs(dir):
        dir = os.path.abspath(dir)
    else:
        dir = os.path.relpath(dir)
    if not os.path.isdir(dir):
        print(dir, 'is not a directory. Exiting')
        sys.exit(1)
    print_tree(dir)
