def on_logo_touched():
    basic.show_string("S")
    serial.write_line("kusuguttaikarayamete-")
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_button_pressed_a():
    basic.show_string("A")
    serial.write_line("gya")
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_string("Y")
    serial.write_line("sorawotobuzo-")
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    basic.show_string("B")
    serial.write_line("o-no-")
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

for index in range(4):
    basic.show_icon(IconNames.SQUARE)
serial.redirect(SerialPin.P1, SerialPin.P0, BaudRate.BAUD_RATE9600)

def on_forever():
    basic.pause(500)
    basic.show_arrow(ArrowNames.EAST)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.show_arrow(ArrowNames.WEST)
basic.forever(on_forever)
