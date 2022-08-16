# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_macropad import keycodes as Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Windows Edge', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x003000, '< Back', [Keycode.ALT, Keycode.LEFT_ARROW]),
        (0x003000, 'Fwd >', [Keycode.ALT, Keycode.RIGHT_ARROW]),
        (0x300000, 'Up', [Keycode.SHIFT, ' ']),      # Scroll up
        # 2nd row ----------
        (0x303000, '- Size', [Keycode.CONTROL, Keycode.KEYPAD_MINUS]),
        (0x303000, 'Size +', [Keycode.CONTROL, Keycode.KEYPAD_PLUS]),
        (0x300000, 'Down', ' '),                     # Scroll down
        # 3rd row ----------
        (0x000030, 'Reload', [Keycode.CONTROL, 'r']),
        (0x000030, 'Restore', [Keycode.CONTROL, 'T']),
        (0x000030, 'Close', [Keycode.CONTROL, 'w']),
        # 4th row ----------
        (0x111111, 'Private', [Keycode.CONTROL, 'N']),
        (0x300000, 'Todo', [Keycode.CONTROL, 't', -Keycode.COMMAND,
                            'https://todoist.com/app/today\n']),   # Digi-Key in new tab
        (0x000000, '', []), 
        # Encoder button ---
        (0x000000, '', []) # Close tab
    ],
    'logo': './logos/Edge.bmp'
}
