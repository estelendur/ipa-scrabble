from phonedict import *

f = open('cmudict-0.7b.txt')
phones = PhoneDict()

line = f.readline()
while (line != ""):
    line = f.readline()
    if (line.startswith(';;;')):
        pass
    else:
        sounds = line.split()[1:]
        for phone in sounds:
            phones.increment(phone)

print phones

f.close()
