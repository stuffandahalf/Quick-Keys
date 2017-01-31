import uinput

with uinput.Device([uinput.KEY_LEFTALT, uinput.KEY_TAB]) as device:
    device.emit_combo([uinput.KEY_LEFTALT, uinput.KEY_TAB])
