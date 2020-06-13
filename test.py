from xml.dom import minidom

mydoc = minidom.parse('hefty.xml')
titles = mydoc.getElementsByTagName('title')[0]
a = 3
for title in titles:
    if a == 0:
        break
    print(title.fi)
    a = a - 1

