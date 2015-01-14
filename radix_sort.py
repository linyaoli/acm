def radix_sort(array, base=10):
    """
    A simple implementation of Radix Sort.
    """

    def list_to_buckets(array, base, iteration):
        buckets = [[] for _ in range(base)]
        for number in array:
            # Isolate the base-digit from the number
            digit = ( number // (base ** iteration) ) % base
            # Drop the number into the correct bucket
            buckets[digit].append(number)
        return buckets

    def buckets_to_list(buckets):
        array = []
        # Collapse buckets back into a list
        for bucket in buckets:
            array.extend(bucket)
        return array

    # Find the largest value in the array to
    maxval = 0
    for i in array:
        if i > maxval:
            maxval = i

    it = 0
    # Iterate, sorting the array by each base-digit
    while ( (base ** it) <= maxval):
        array = buckets_to_list(list_to_buckets(array, base, it))
        it += 1

    return array


from random import random

if __name__ == "__main__":
    # Run radix_sort() against python's sorted() to verify implementation
    array_size = 2 ** 10
    array = [int(random()*array_size) for _ in range(array_size)]
    assert ( sorted(array) == radix_sort(array) )
    print array
