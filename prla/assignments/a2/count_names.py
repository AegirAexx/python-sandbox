import json
import urllib.request

# url = 'https://hagstofa.is/media/49531/names.json'
# req = urllib.request.Request(url)
# j = urllib.request.urlopen(req).read()
#
# cont = json.loads(r.decode('utf-8'))
# counter = 0
#
# ##parcing json
# for item in cont['data']['children']:
#     counter += 1
#     print("Title:", item['data']['title'], "\nComments:", item['data']['num_comments'])
#     print("----")
#
# ##print formated
# #print (json.dumps(cont, indent=4, sort_keys=True))
# print("Number of titles: ", counter)


def count_names(s):
    url = 'https://hagstofa.is/media/49531/names.json'
    req = urllib.request.Request(url)
    r = urllib.request.urlopen(req).read()
    t = json.loads(r.decode('utf-8'))
    one, two = [], []
    trigger = None
    for x in t:
        if x['Nafn'].startswith(s):
            one.append(int(x['Fjoldi1']))
            two.append(int(x['Fjoldi2']))
            trigger = True
    return tuple((sum(one), sum(two))) if trigger else tuple((0, 0))


print(count_names('Bja'))
# (3267, 1494)
print(count_names('Wat'))
# (8, 2)
print(count_names('Snati'))
# (0, 0)
