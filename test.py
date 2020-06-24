from xml.dom import minidom

mydoc = minidom.parse('hefty.xml')
titles = mydoc.getElementsByTagName('title')[0]
a = 3
for title in titles:
    if a == 0:
        break
    print(title)
    a = a - 1

