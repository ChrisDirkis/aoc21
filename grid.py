from itertools import permutations, chain, product
from collections import namedtuple
from math import sqrt, prod

vec2 = namedtuple('vec2', ['x', 'y'])
vec3 = namedtuple('vec3', ['x', 'y', 'z'])
vec4 = namedtuple('vec4', ['x', 'y', 'z', 'w'])

def to_vec(t):
    if len(t) == 2:
        return vec2(*t)
    elif len(t) == 3:
        return vec3(*t)
    elif len(t) == 4:
        return vec4(*t)
    return t

def add_t(a, b):
    return to_vec(tuple(sum(v) for v in zip(a, b)))

def sub_t(a, b):
    return to_vec(tuple(v1 - v2 for v1, v2 in zip(a, b)))

def dot_t(a, b):
    return to_vec(tuple(prod(v) for v in zip(a, b)))

def in_grid(addr, dims):
    return all(v >= 0 and v < dims[i] for i, v in enumerate(addr))

def adj(addr, dims):
    n = len(addr)
    offsets = chain(permutations([1] + [0] * (n - 1)), permutations([-1] + [0] * (n - 1)))
    adjs = (add_t(addr, offset) for offset in offsets)
    return (adj for adj in adjs if in_grid(addr, dims))

def adj_diag(addr, dims):
    offsets = (v for v in product([-1, 0, 1], repeat=len(dims)) if any(v))
    adjs = (add_t(addr, offset) for offset in offsets)
    return (adj for adj in adjs if in_grid(addr, dims))

def length(addr):
    return sqrt(sum(v**2 for v in addr))

def length_taxi(addr):
    return sum(abs(v) for v in addr)