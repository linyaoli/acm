import random

def random_subset( it, K ):
    result = []
    N = 0
    s = 0

    for item in it:
        N += 1
        if len( result ) < K:
            result.append( item )
        else:
            s = int(random.random() * N)
        if s < K:
            result[ s ] = item

    return result
    
lst = range(100)
it = range(1,100,1)
for i in it:
    print random_subset(it, 1)
