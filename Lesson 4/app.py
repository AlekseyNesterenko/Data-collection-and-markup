from lxml import etree


tree = etree.parse('Lesson 4/src/web_page.html')


# # title_el = tree.find('body/p')

# list_item = tree.findall('body/ul/li')

# for li in list_item:
#     a = li.find('a')
#     if a is not None:
#         print(f'{li.text.strip()} {a.text}')
#     else:
#         print(li.text)
    



# # title_el = tree.xpath('//p/text()')[0]
# list_iters = tree.xpath('//ul/descendant::li')

# for li in list_iters:
#     text = ''.join(map(str.strip, li.xpath('.//text()')))
#     print(text)

html = tree.getroot()

title_el = html.cssselect('p')
print(title_el[0].text)