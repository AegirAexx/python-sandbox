
def tag_open(s):
    return '<{s}>'.format(s=s)


def tag_close(s):
    return '</{s}>'.format(s=s)


def zen_expand():
    tags = ['table', 'td', 'tr', 'p', 'head', 'body', 'html']
    for tag in tags:
        print(tag_open(tag), tag_close(tag))


zen_expand()

# >>> zen_expand("a+div+p*3")
# "<a></a><div></div><p></p><p></p><p></p>"

# >>> zen_expand("dd")
# "<dd></dd>"

# >>> zen_expand("table>tr*3>td*2")
# "<table><tr><td></td><td></td></tr><tr><td></td><td></td></tr>
# <tr><td></td><td></td></tr></table>"
