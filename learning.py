import simpleguitk as simplegui

def draw(canvas):
    canvas.draw_text("Hello!",[300,200],24,'White')
    canvas.draw_circle([6,6],50,2,'Green')
    canvas.draw_line((200, 0), (0, 300), 10, "Green")

f=simplegui.create_frame("My frame",200,300)

f.set_draw_handler(draw)

f.start()
