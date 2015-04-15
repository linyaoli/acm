import hashlib
m = hashlib.md5()

tmp = "google.com"
m.update(tmp)
print 'goo.gl/' + m.hexdigest()[:6]
