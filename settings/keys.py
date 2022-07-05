from libqtile.config import Key
from libqtile.command import lazy
from settings.keyboard import next_layout
from libqtile.widget import Notify

modkey = 'mod4'
altkey = 'mod1'


keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([altkey], 'h', lazy.layout.left()),
    ([altkey], 'l', lazy.layout.right()),
    ([altkey], 'j', lazy.layout.down()),
    ([altkey], 'k', lazy.layout.up()),

    # Change window sizes
    (['control'], 'j', lazy.layout.grow()),
    (['control'], 'k', lazy.layout.shrink()),
    (['control'], 'n', lazy.layout.normalize()),
    (['control'], 'm', lazy.layout.maximize()),

    # Move windows in current stack
    ([modkey], 'h', lazy.layout.shuffle_left()),
    ([modkey], 'l', lazy.layout.shuffle_right()),
    ([modkey], 'j', lazy.layout.shuffle_down()),
    ([modkey], 'k', lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([modkey], 'Tab', lazy.next_layout()),

    # Toggle a window to floating & tiling
    ([modkey], 'f', lazy.window.toggle_floating()),

    # Kill window
    ([modkey], 'w', lazy.window.kill()),

    # Restart Qtile
    ([modkey], 'F1', lazy.restart()),
    

    # ------------ App Configs ------------

    # Launcher
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
