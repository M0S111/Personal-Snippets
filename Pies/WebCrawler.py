#! python3

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:

    address = ' '.join(sys.argv[1:])

else:

    address = pyperclip.paste()

webbrowser.open('https://en.wikipedia.org/wiki/' + address)
