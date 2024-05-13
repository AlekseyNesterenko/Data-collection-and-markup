from lxml import etree

def print_tree(el, depth=0):
    print('-'*depth + el.tag)

    for child in el.iterchildren():
        print_tree(child, depth + 1)

tree = etree.parse('Lesson 4/src/web_page.html')

root = tree.getroot()

print_tree(root)