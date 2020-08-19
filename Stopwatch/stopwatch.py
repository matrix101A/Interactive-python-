
# template for "Stopwatch: The Game"
import  simpleguitk as  simplegui
# define global variables
A=0
B=0
C=0
D=0
time=0
message="Hello"
attempts=0
success=0
stop=1

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format():
    global A,B,C,D
    sec=int(time/10)
    D=(time%10)
    C=int((sec%60))%10
    B=int((sec%60)/10)
    A=sec/60
    A=int(sec/60)

    f.set_draw_handler(draw)


# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    global stop
    t.start()
    stop=0


def stop():
    global attempts,D,success,stop
    if(stop==0):
        t.stop()
        attempts += 1
        if(int(D)==0):
            success+=1
        stop=1

def reset():
    global A, B, C, D, time,attempts,success
    A = 0
    B = 0
    C = 0
    D = 0
    time=0
    attempts = 0
    success = 0
    f.set_draw_handler(draw)


# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time+=1
    format()



# define draw handler
def draw(canvas):
    global message, A, B, C, D,attempts,success
    message = str(A) + ":" + str(B) + str(C) + "." + str(D)
    canvas.draw_text(message,[110,110],30,'White')
    canvas.draw_text(str(success)+"/"+str(attempts),[250,50],15,'White')



# create frame

f=simplegui.create_frame("Stopwatch",300,200)
t=simplegui.create_timer(100, tick)

# register event handlers

f.add_button("Start",start,100)
f.add_button("Stop",stop,100)
f.add_button("Reset",reset,100)


# start frame

f.start()

# Please remember to review the grading rubric




















