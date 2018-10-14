small=1
big=100
def guessmynumber():
    return int(small+big)/2
def smaller():
    global small,big
    big=guessmynumber()-1
    return guessmynumber()
def bigger():
    global small,big
    small=guessmynumber()+1
    return guessmynumber()
def restart():
    global small,big
    small=1
    big=100
    return guessmynumber()

