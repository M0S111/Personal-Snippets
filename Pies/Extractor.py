import re #pyperclip

ph_regex = re.compile(r'''(\d{4})?
                          (\s|-|\.)?
                          (\d{3})
                          (\s|-|\.)?
                          (\d{4})''',re.VERBOSE)

ph = ph_regex.findall('4368-276-3469')

print(ph)

em_regex = re.compile(r'''(\d+|\w+)
                          (@)
                          (\w+)
                          (\.com|\.org)''',re.VERBOSE)

em = em_regex.findall('stormbrewer@yandex.org')

dom_regex = re.compile(r'''(/|//www\.|www\.)?(\w+(-)*\w+)(\.)''',re.VERBOSE)

dom = dom_regex.search('www.xakep.ru')

print(em)

print(dom.group(2))

#txt = str(pyperclip.paste())
