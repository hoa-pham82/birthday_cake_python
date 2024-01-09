from turtle import *
from shapes import *
from voice import *

cake_pen = Turtle()
cake_pen.hideturtle()
cake_pen.speed(0)

candle_pen = Turtle()
candle_pen.hideturtle()
candle_pen.speed(0)

window = turtle.Screen()
window.bgcolor('#ADD8E6')
y = -140

ingredients = {}
ingredients["cherry"]="#C20067"
ingredients["raspberry"]="#e30b5d"
ingredients["lemon"]="#FFFA5C"
ingredients["milk chocolate"]="#BF671F"
ingredients["dark chocolate"]="#2A1506"
ingredients["icing"]="#FFFFFF"
ingredients["candle"]="#F73718" 

layers = []
layers.append(["raspberry",30])
layers.append(["dark chocolate",20])
layers.append(["lemon",60])
layers.append(["milk chocolate",40])

# draw plate
draw_rectangle(turtle, 'white', -150, y-10, +300, 10)

# draw cake layers
for layer in layers:
    draw_rectangle(cake_pen, ingredients[layer[0]], -120, y, 240, layer[1])
    y+=layer[1]

draw_icing(cake_pen, ingredients['icing'], y)

# draw cherry
draw_circle(cake_pen, ingredients['cherry'], 0, y+10, 15)

#draw candles
draw_circle(candle_pen, ingredients['candle'], 40, y+10, 10)
draw_circle(candle_pen, ingredients['candle'], 80, y+10, 10)

draw_circle(candle_pen, ingredients['candle'], -40, y+10, 10)
draw_circle(candle_pen, ingredients['candle'], -80, y+10, 10)

# Draw sitck and circle on stick
draw_stick(cake_pen, ingredients['cherry'], 100, y+10)
draw_circle_on_stick(cake_pen, ingredients["cherry"],ingredients["icing"], 40, y+110, 60)
write_text(cake_pen, "HPBD", ingredients["raspberry"], 65, y+120)
write_text(cake_pen, "Anh 🏋️", ingredients["raspberry"], 60, y+80)

candle_pen.getscreen().update()

# blow candles
record_to_file('blow_candles.wav')
candle_pen.clear()

cake_pen.getscreen().update()
turtle.done()