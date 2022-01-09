import os

const KEYBOARD_NAME*: string = "xkblayout-state"
let QTILE_PATH*: string = expandTilde("~") / ".config" / "qtile"

proc KEYBOARD_SCRIPT*(): string {.inline.} = 
    if fileExists(KEYBOARD_NAME):
        return expandFilename(KEYBOARD_NAME)
    else: 
        raise newException(OSError, "Keyboard File was not found!")