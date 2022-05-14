import sys
from g_python.gextension import Extension
from g_python.hmessage import Direction



extension_info = {
    "title": "Fafke",
    "description": ":fafke on/off ",
    "version": "0.1",
    "author": "funkydemir66"
}

ext = Extension(extension_info, sys.argv, silent=True)
ext.start()

sec_kod3 = sec_kod2 = sec_kod = sc = False

def konusma(msj):
    global sc, sec_kod, sec_kod2, sec_kod3

    text = msj.packet.read_string()

    if text == ':fafke on':
        msj.is_blocked = True
        sec_kod = True
        sec_kod2 = True
        sec_kod3 = True
        sc = True
        ext.send_to_server('{out:AvatarExpression}{i:5}')
        ext.send_to_client('{in:Chat}{i:123456789}{s:"Script: on "}{i:0}{i:30}{i:0}{i:0}')

    if text == ':fafke off':
        msj.is_blocked = True
        sec_kod = False
        sec_kod2 = False
        sec_kod3 = False
        sc = False
        ext.send_to_client('{in:Chat}{i:123456789}{s:"Script: off "}{i:0}{i:30}{i:0}{i:0}')


def Look_to(f):

    if sec_kod:
        f.is_blocked = True

def StartWritting(g):

    if sec_kod2:
        g.is_blocked = True

def Move(h):

    if sec_kod3:
        h.is_blocked = True

ext.intercept(Direction.TO_SERVER, konusma, 'Chat')
ext.intercept(Direction.TO_SERVER, Look_to, 'LookTo')
ext.intercept(Direction.TO_SERVER, StartWritting, 'StartTyping')
ext.intercept(Direction.TO_SERVER, Move, 'MoveAvatar')
