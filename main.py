def on_button_pressed_a():
    global radiogroup
    radiogroup += 5
    if radiogroup >= 11:
        radiogroup = 1
    radio.set_group(radiogroup)
    basic.show_string("" + str(radiogroup))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global radiogroup
    radiogroup += 1
    if radiogroup == 11:
        radiogroup = 1
    radio.set_group(radiogroup)
    basic.show_string("" + str(radiogroup))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global radiogroup
    radiogroup += -5
    if radiogroup <= 0:
        radiogroup = 1
    radio.set_group(radiogroup)
    basic.show_string("" + str(radiogroup))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    global x, y
    if name == "x":
        x = value
    if name == "y":
        y = value
radio.on_received_value(on_received_value)

y = 0
x = 0
radiogroup = 0
radiogroup = 1
radio.set_group(radiogroup)
basic.show_string("" + str(radiogroup))

def on_forever():
    global x, y
    if -40 < x and x < 40:
        x = 0
    if -40 < y and y < 40:
        y = 0
    if y > 0:
        pins.digital_write_pin(DigitalPin.P12, 0)
        pins.digital_write_pin(DigitalPin.P8, 1)
        pins.digital_write_pin(DigitalPin.P16, 1)
        pins.digital_write_pin(DigitalPin.P0, 0)
    if y < 0:
        pins.digital_write_pin(DigitalPin.P12, 1)
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P16, 0)
        pins.digital_write_pin(DigitalPin.P0, 1)
    if x > 0:
        pins.digital_write_pin(DigitalPin.P12, 0)
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P16, 1)
        pins.digital_write_pin(DigitalPin.P0, 0)
    if x < 0:
        pins.digital_write_pin(DigitalPin.P12, 1)
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P16, 0)
        pins.digital_write_pin(DigitalPin.P0, 0)
    if x == 0 and y == 0:
        pins.digital_write_pin(DigitalPin.P12, 0)
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P16, 0)
        pins.digital_write_pin(DigitalPin.P0, 0)
    basic.pause(50)
basic.forever(on_forever)
