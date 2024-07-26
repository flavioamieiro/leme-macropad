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
# Cols: GP18, GP19, GP20
# Rows: GP16, GP17
keyboard.col_pins = (board.GP18, board.GP19, board.GP20)
keyboard.row_pins = (board.GP16, board.GP17)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


# --- OLED display
# SCL = GP5
# SDA = GP4
i2c_bus = busio.I2C(board.GP5, board.GP4)

driver = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,
)

display = Display(
    display=driver,
    flip=True
)

display.entries = [
    TextEntry(
        text="Macropad", x_anchor="M", y_anchor="M", x=display.width/2, y=display.height/2
    ),
]

keyboard.extensions.append(display)


# ---  Rotary Encoder:
# switch - GP11
# CLK/pin A - GP13
# DT/pin B - GP12

keyboard.extensions.append(MediaKeys())
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP13, board.GP12, board.GP11),)

keyboard.modules = [encoder_handler]


# --- Keymap
encoder_handler.map = [
    ((KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP, KC.AUDIO_MUTE), ),
]


keyboard.keymap = [
    [KC.F14, KC.F15, KC.F16, KC.F17, KC.F18, KC.F19],
]

# keyboard.debug_enabled = True

if __name__ == "__main__":
    keyboard.go()
