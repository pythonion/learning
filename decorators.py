def decorator(f):
    def wrap(*args,**kwargs):
        x = f(*args,**kwargs)
        return x.title()
    return wrap

@decorator
def name(x,y):
    return "%s, %s" % (x,y)
