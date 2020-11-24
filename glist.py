import requests
import json

class Glist:
    def __init__(self):
        pass

    def check(self, mode=None):
        r = requests.get('http://epicgamesfree4all.herokuapp.com/?json')
        
        if mode == 'trigger':
            return r.json()
            
        else:
            t = []
            for i in r.json()['games']:
                with open('gamesordered.txt', 'r') as a:
                    if not i['title'] in [ j.replace('\n', '') for j in a.readlines() ]:
                        t.append(i)

            return t

    def owned(self, gname, gdta):
        a = open('gamesordered.txt', 'a+')
        f = open('data.txt', 'a+')
        if gname in a.readlines():
            print('Already owned')
        else:
            a.write(gname)
            a.write('\n')

            json.dump(gdta, f)
            f.write('\n')

            print('Added to purchased list')
