import random as rd
import string
# use google service
# goo.gl
def shorten(URL):
    url = URL
    lib = string.uppercase + string.digits + string.lowercase
    n = len(lib)
    ret = "goo.gl/"
    for i in xrange(6):
        ret += lib[int(rd.random() * n)]

    return ret
# avoid collisions
# if key exists, re-generate the shorten url until it's unique.
mapping = {}
url = "www.uber.com/cities/beijing"
i = 0
while i < 4:
    short_url = shorten(url)
    if short_url in mapping:
        continue
    mapping[short_url] = url
    i += 1
print mapping.items()

# However, hashing strings are a much more complex job.
