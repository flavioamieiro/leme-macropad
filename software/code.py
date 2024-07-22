import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC

from kmk.modules.encoder import EncoderHandler

from kmk.scanners import DiodeOrientation
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# -- Keyboard matrix
# Cols: GP0
# Rows: GP1
keyboard.col_pins = (board.GP0, )
keyboard.row_pins = (board.GP1, )
keyboard.diode_orientation = DiodeOrientation.COL2ROW


# --- OLED display
# SCL = GP9
# SDA = GP8
i2c_bus = busio.I2C(board.GP9, board.GP8)

driver = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,
)

display = Display(
    display=driver,
)

display.entries = [
    TextEntry(
        text="Macropad", x_anchor="M", y_anchor="M", x=display.width/2, y=display.height/2
    ),
]

keyboard.extensions.append(display)


# ---  Rotary Encoder:
# switch - GP13
# CLK/pin A - GP14
# DT/pin B - GP15

keyboard.extensions.append(MediaKeys())
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP14, board.GP15, board.GP13),)

keyboard.modules = [encoder_handler]


# --- Keymap
encoder_handler.map = [
    ((KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP, KC.AUDIO_MUTE), ),
]


keyboard.keymap = [
    [KC.F14, ],
]


if __name__ == "__main__":
    keyboard.go()
