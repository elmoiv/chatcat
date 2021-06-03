from socket import gethostbyname, getfqdn
from threading import Thread

def threaded(fn):
    """
    Thread wrapper function (decorator)
    """
    def run(*k, **kw):
        t = Thread(target=fn, args=k, kwargs=kw)
        t.start()
        return t
    return run

@threaded
def play_sound(sa_sound_object):
    sa_sound_object.play()

def get_my_ip():
    return gethostbyname(getfqdn())

def send_msg(client, server, raw_text, name):
    dct = {
        'type': 'msg',
        'text': raw_text,
        'name': name or 'Anonymous'
        }
    client.send(str(dct), server)
    return dct

def send_info(client, server, raw_text, name):
    dct = {
        'type': 'info',
        'text': raw_text,
        'name': name or 'Anonymous'
        }
    client.send(str(dct), server)
    return dct

def ip2id(ip):
    return ''.join(hex(int(i))[2:].rjust(2, '0') for i in ip.split('.'))

def id2ip(id):
    return '.'.join(str(int('0x' + id[i:i + 2], 16)) for i in range(0, 8, 2))