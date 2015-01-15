A common structure of backtracking.

def backtracking(c):
    # the reject function should be a boolean-valued function.
    # the efficiency of backtracking algorithm depends on reject returning ture for candidates
    # that are close to the root as possible.
    if reject(P, c) then return
    if accept(P, c) then output(P, c)
    # generate the first extension of candidate c.
    # enumeration
    s <- first(P, c)
    while s != ^ :
        backtracking(s)
        # generate the next alternative extension of a candidate, after the extension s.
        s <- next(P, s)
