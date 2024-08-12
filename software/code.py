import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC

from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys

from kmk.scanners import DiodeOrientation
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.media_keys import MediaKeys


keyboard = KMKKeyboard()

# -- Keyboard matrix
# Cols: GP18, GP19, GP20
# Rows: GP16, GP17
keyboard.col_pins = (board.GP20, board.GP19, board.GP18)
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
    flip=False,
)

display.entries = [
    TextEntry(
        text="Layer: 1",
        x_anchor="L",
        y_anchor="T",
        x=0,
        y=0,
        layer=0,
    ),
    TextEntry(
        text="Layer: 2",
        x_anchor="L",
        y_anchor="T",
        x=0,
        y=0,
        layer=1,
    ),
    TextEntry(
        text="Macropad",
        x_anchor="M",
        y_anchor="M",
        x=display.width / 2,
        y=display.height / 2,
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

keyboard.modules = [
    encoder_handler,
    Layers(),
    MouseKeys(),
]


# --- Keymap
encoder_handler.map = [
    # Layer 0
    ((KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP, KC.AUDIO_MUTE),),
    # Layer 1
    ((KC.MW_UP, KC.MW_DOWN, KC.MB_MMB),),
]


keyboard.keymap = [
    # Layer 0
    [KC.F14, KC.F15, KC.F16, KC.F17, KC.F18, KC.TG(1)],
    # Layer 1
    [
        KC.TRANSPARENT,
        KC.TRANSPARENT,
        KC.TRANSPARENT,
        KC.TRANSPARENT,
        KC.TRANSPARENT,
        KC.TG(0),
    ],
]

# keyboard.debug_enabled = True

if __name__ == "__main__":
    keyboard.go()
