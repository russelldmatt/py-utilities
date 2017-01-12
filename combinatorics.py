def choose_indices(n, max_):
    """ Choose `n` items out of `max` total items.  
    Yields all ordered lists of length `n`, out of list(range(max_))

    Examples:
        >>> for l in choose_indices(3, 4): print l
        [0, 1, 2]
        [0, 1, 3]
        [0, 2, 3]
        [1, 2, 3]
    """
    def choose_indices_inner(num_left, indices, min_, max_):
        if num_left == 0: 
            yield indices
        else:
            start = indices[-1] + 1 if len(indices) > 0 else min_
            for i in range(start, max_):
                indices.append(i)
                for r in choose_indices_inner(num_left - 1, indices, min_, max_): 
                    yield r
                indices.pop()
    for i in choose_indices_inner(n, [], 0, max_):
        yield i

def choose(n, l):
    """Choose `n` items out of the list `l`.
    
    Yields all lists of length `n`, out of list `l`.  Yielded lists
    are ordered in the same way as `l`.

    Examples:
        >>>> for l in choose(3, [4, 2, 10, 0]): print l
        [4, 2, 10]
        [4, 2, 0]
        [4, 10, 0]
        [2, 10, 0]
    """
    for idxs in choose_indices(n, len(l)):
        yield [l[i] for i in idxs]

def permutation_indices(len_):
    """ All permutations of integers from 0 to `len` (exclusive).

    Examples:
        >>> for l in permutation_indices(3): print l
        [0, 1, 2]
        [0, 2, 1]
        [1, 0, 2]
        [1, 2, 0]
        [2, 0, 1]
        [2, 1, 0]
    """
    def loop(indices_left, acc):
        if len(indices_left) == 0: 
            yield acc
        for i in indices_left:
            indices_left.remove(i) # dangerous?
            acc.append(i)
            for r in loop(indices_left, acc): yield r
            acc.remove(i)
            indices_left.add(i)
    indices_left = set(range(len_))
    for r in loop(indices_left, []): yield r

def permutations(l):
    """ All permutations of list `l`.

    Examples:
        >>> for l in combinatorics.permutations([4,10,7]): print l
        [4, 10, 7]
        [4, 7, 10]
        [10, 4, 7]
        [10, 7, 4]
        [7, 4, 10]
    """
    for idxs in permutation_indices(len(l)):
        yield [l[i] for i in idxs]

