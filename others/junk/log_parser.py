"""
File:
== Abc*# ==
= I am a string\\
=== abc ===

Expected Json:
{'abc':
       {'title': 'abc*#',
        'body': 'i am a string\\'
        }
'abc-1':
       {'title': 'abc',
        'body': ''}
}

"""
import re
input = [[
    "== Abc*# ==", "= I am a string\\"
],
[
    "=== abc ===", ""
]
]
ret = {}
for i in input:
    key = re.split("=* ", i[0])[1].lower()

    value = re.split("=*", i[1])

    if value != ['']:
        value = value[1]
    title = key
    key = re.split("\W*", key)[0]

    if key in ret.keys():
        n = 1
        while key + '-' + str(n) in ret.keys():
            n += 1

        ret[key+'-'+str(n)] = {'title': title, 'body': value}

    else:
        ret[key] = {'title': title, 'body':value}
print ret
