import 
    "./shell", # Vindaar's module.
    "./path",
    "./notify",
    osproc,
    os,
    strformat,
    strutils

const COMMAND = "setxkbmap"
let KEYBOARDS: seq[string] = @["us", "es"]

proc nextLayout(): string =
    let current_l: string = execCmdEx(fmt"{KEYBOARD_SCRIPT()} print %e").output
    var next_l: string

    try:
        next_l = KEYBOARDS[KEYBOARDS.find(current_l.strip()) + 1]
    except IndexDefect:
        next_l = KEYBOARDS[0]
    finally:
        return next_l


let nl = nextLayout()
shell:
    ($COMMAND) ($nl)

notifySend(
    title = "Keyboard Notification", 
    subtitle = fmt"Layout: {nl.toUpperAscii}", 
    time_out = 1000,
    icon = QTILE_PATH / "icons" / "SettingsBlue.png"
)
