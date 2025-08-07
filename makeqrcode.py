#! /usr/bin/env python3

from segno import helpers

card = {
    'name' : "Ulrike,Martin",
    'email':"logopaedie-martin@web.de",
    ***REMOVED***
    'url' :"https://sms-2025.pages.dev/",
}
output_filename = "images/qr.png"
output_option = {
    'dark': "black",
    'light': "#8DBEF1FF",
    'border': 5,
    'scale': 5
}

qrcode = helpers.make_mecard(**card)
qrcode.save(output_filename, **output_option)

