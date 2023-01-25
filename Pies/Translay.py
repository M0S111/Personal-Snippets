#! python3

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:

    insert = ' '.join(sys.argv[1:])

else:

    insert = pyperclip.paste()

address = '?sl=ur&tl=en&text=' + insert + '&op=translate'

webbrowser.open('https://translate.google.com/' + address)
