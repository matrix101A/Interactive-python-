import simpleguitk as simplegui

# intialize globals
store = 12
operand = 3


# event handlers for calculator with a store and operand

def output():
    """prints contents of store and operand"""
    print("Store = ", store)
    print("Operand = ", operand)



def swap():
    """ swap contents of store and operand"""
    global store, operand
    store, operand = operand, store
    output()


def add():
    """ add operand to store"""
    global store
    store = store + operand
    output()


def sub():
    """ subtract operand from store"""
    global store
    store = store - operand
    output()


def mult():
    """ multiply store by operand"""
    global store
    store = store * operand
    output()


def div():
    """ divide store by operand"""
    global store
    store = store / operand
    output()

def enter(inp):
    global operand
    operand=float(inp)
    output()

# create frame
f = simplegui.create_frame("Calculator", 300, 300)

# register event handlers
f.add_button("Print", output, 100)
f.add_button("Swap", swap, 100)
f.add_button("+", add, 20)
f.add_button("-", sub, 20)
f.add_button("*", mult, 20)
f.add_button("/", div, 20)
imp=f.add_input("Enter Operand !",enter,100)
# get frame rolling
f.start()