# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Consumer Control codes (media keys)

# The syntax for Consumer Control macros is a little peculiar, in order to
# maintain backward compatibility with the original keycode-only macro files.
# The third item for each macro is a list in brackets, and each value within
# is normally an integer (Keycode), float (delay) or string (typed literally).
# Consumer Control codes are distinguished by enclosing them in a list within
# the list, which is why you'll see double brackets [[ ]] below.
# Like Keycodes, Consumer Control codes can be positive (press) or negative
# (release), and float values can be inserted for pauses.

# To reference Consumer Control codes, import ConsumerControlCode like so...
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_macropad import keycodes as Keycode # REQUIRED if using Keycode.* values
# You can still import Keycode as well if a macro file mixes types!
# See other macro files for typical Keycode examples.

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'IntelliJ Debugging', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x303030, 'Test 1', [Keycode.CONTROL, Keycode.LEFT_SHIFT, Keycode.F10]),
        (0x003000, 'Run', [Keycode.LEFT_SHIFT, Keycode.F10]),
        (0x303000, 'Debug', [Keycode.LEFT_SHIFT, Keycode.F9]),
        # 2nd row ----------
        (0x000530, 'Into', [Keycode.F7]),
        (0x000030, 'Over', [Keycode.F8]),
        (0x880000, 'Out', [Keycode.LEFT_SHIFT, Keycode.F8]),
        # 3rd row ----------
        (0x003010, 'Rerun', [Keycode.CONTROL, Keycode.F5]),
        (0x003000, 'Resume', [Keycode.F9]),
        (0x300000, 'Stop', [Keycode.CONTROL, Keycode.F2]),
        # 4th row ----------
        (0x000000, 'ESC', [Keycode.ESCAPE]),
        (0x303000, 'Evaluate', [Keycode.OPTION, Keycode.F8]),
        (0x300000, 'Close', [Keycode.CONTROL, Keycode.F4]),
        # Encoder button ---
        (0x000000, '', [])
    ],
    'logo': './logos/IntelliJ.bmp'
}
