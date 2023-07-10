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

print(em)

#txt = str(pyperclip.paste())