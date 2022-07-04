from libqtile.config import Key
from libqtile.command import lazy
from os.path import join

from settings.path import qtile_path
from settings.keyboard import next_layout

modkey = 'mod4'


keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([modkey], 'h', lazy.layout.left()),
    ([modkey], 'l', lazy.layout.right()),
    ([modkey], 'j', lazy.layout.down()),
    ([modkey], 'k', lazy.layout.up()),

    # Change window sizes
    ([modkey, 'shift', 'control'], 'j', lazy.layout.grow()),
    ([modkey, 'shift', 'control'], 'k', lazy.layout.shrink()),
    ([modkey, 'shift', 'control'], 'n', lazy.layout.normalize()),
    ([modkey, 'shift', 'control'], 'm', lazy.layout.maximize()),

    # Move windows in current stack
    ([modkey, 'shift'], 'h', lazy.layout.shuffle_left()),
    ([modkey, 'shift'], 'l', lazy.layout.shuffle_right()),
    ([modkey, 'shift'], 'j', lazy.layout.shuffle_down()),
    ([modkey, 'shift'], 'k', lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([modkey], 'Tab', lazy.next_layout()),

    # Toggle a window to floating & tiling
    ([modkey], 'f', lazy.window.toggle_floating()),


    # Kill window
    ([modkey], 'w', lazy.window.kill()),

    # Switch focus of monitors
    # ([mod], "period", lazy.next_screen()),
    # ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([modkey], 'F1', lazy.restart()),
    
    # ------------ App Configs ------------
    # Menu
    #([modkey], 'm', lazy.spawn(join(qtile_path, "scripts", "bin", "launcher"))),

    # Window Nav
    #([modkey, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    ([modkey], 'b', lazy.spawn('brave')),

    # Terminal
    ([modkey], 'Return', lazy.spawn('kitty')),

    # Redshift
    ([modkey], 'r', lazy.spawn('redshift -O 4000')),
    ([modkey, 'shift'], 'r', lazy.spawn('redshift -x')),

    # Screenshot
    ([modkey], 's', lazy.spawn('flameshot gui')),

    # keyboard layouts
    ([modkey], 'space', lazy.function(next_layout, ['es', 'us'])),


    # ------------ Hardware Configs ------------

    # Volume
    ([], 'XF86AudioLowerVolume', lazy.spawn(
        'pactl set-sink-volume @DEFAULT_SINK@ -5%'
    )),
    ([], 'XF86AudioRaiseVolume', lazy.spawn(
        'pactl set-sink-volume @DEFAULT_SINK@ +5%'
    )),
    ([], 'XF86AudioMute', lazy.spawn(
        'pactl set-sink-mute @DEFAULT_SINK@ toggle'
    )),

    # Brightness
    ([], 'F8', lazy.spawn('brightnessctl set 5%-')),
    ([], 'F9', lazy.spawn('brightnessctl set +5%')),
]]
