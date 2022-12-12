def on_logo_long_pressed():
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 0)
    pins.digital_write_pin(DigitalPin.P3, 0)
    pins.digital_write_pin(DigitalPin.P4, 0)
    pins.digital_write_pin(DigitalPin.P5, 0)
    pins.digital_write_pin(DigitalPin.P6, 0)
    pins.digital_write_pin(DigitalPin.P7, 0)
    pins.digital_write_pin(DigitalPin.P8, 0)
    pins.digital_write_pin(DigitalPin.P9, 0)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 1)
    pins.digital_write_pin(DigitalPin.P3, 1)
    pins.digital_write_pin(DigitalPin.P4, 1)
    pins.digital_write_pin(DigitalPin.P5, 1)
    pins.digital_write_pin(DigitalPin.P6, 1)
    pins.digital_write_pin(DigitalPin.P7, 1)
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.digital_write_pin(DigitalPin.P9, 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    pins.digital_write_pin(DigitalPin.P1, 0)
    basic.pause(150000)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    pins.digital_write_pin(DigitalPin.P5, 1)
    basic.pause(1000)
    pins.digital_write_pin(DigitalPin.P1, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)
