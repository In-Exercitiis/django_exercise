#!/usr/bin/env python2.7


#
# Problem 1
#
def capitalized(func):
    def wrapper():
        return func().upper()
    return wrapper


@capitalized
def string_returning_function():
    return "foo"

#
# Problem 2
#
def compose(*args):
    def func_decorator(func):
        def wrapper(arg):
            ret = func(arg)
            for fn in args:
                ret = fn(ret)
            return ret
        return wrapper
    return func_decorator


def func1(arg):
    return '1%s1' % arg


def func2(arg):
    return '2%s2' % arg


def func3(arg):
    return '3%s3' % arg


@compose(func1, func2, func3)
def func0(param):
    return '0%s0' % param


#
# Problem 3
#

def words(file_path):
    file_dsc = open(file_path)
    char = file_dsc.read(1)
    buf = ''
    while char:
        if not char.isspace():
            buf += char
        else:
            yield buf
            buf = ''
        char = file_dsc.read(1)
#
# 3a. UTF-8 typically is one byte but can be up to four. This would
# mean having to adjust to reading 4 bytes and converting to utf-8
# before checking the chacter. This is not so much an issue in python3
# as everything in python3 is utf-8.
#

#
# 4. This is a partition problem, I would start with somethign along the lines below.
#

def partition(initial_set):
    A = set()
    B = set()
    for n in initial_set:
        if sum(A) < sum(B):
           A.add(n)
        else:
           B.add(n)
    return (A, B)

#
# 5. In simply looking at the code, it appears that dtype is being set
# to object which may or may not be more expensive than the type that
# series would infer from the set. Further investation with different
# dtypes could be useful.
#


if __name__ == '__main__':
    print string_returning_function()
    print func0('foo')

    file_path = '/home/lpowers/projects/research_python.txt'
    for word in words(file_path):
        if word:
            print word
