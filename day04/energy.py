import itertools
# plugs = ['plug1', 'plug2', 'plug3']
# sockets = ['socket1', 'socket2', 'socket3', 'socket4']
# cables = ['cable1', 'cable2', 'cable3', 'cable4']
plugs = ['plugZ', None, 'plugY', 'plugX']
sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
cables = ['cable2', 'cable1', False]

def filt_str(val):
    return filter(lambda x: type(x) == str, val)

def fix_wiring(cables, sockets, plugs):
    return [ str(f"plug {x[0]} into {x[1]} using {y} ") if y != None else str(f"weld {x[0]} to {x[1]} without plug") for x, y in itertools.zip_longest((zip(filt_str(cables), filt_str(sockets))), filt_str(plugs)) if x != None]


for i in fix_wiring(cables, sockets, plugs):
    print(i)