from libqtile import hook

from settings.keys import modkey, keys
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.widgets import widget_defaults, extension_defaults
from settings.screens import screens
from settings.mouse import mouse
from settings.path import qtile_path

from os import path
import subprocess
from time import sleep

@hook.subscribe.startup_once
def autostart():
    subprocess.call(['python', path.join(qtile_path, 'autostart.py')])
    #sleep(5)# Tiempo de espera (para que se inicie el daemon de los widgets)
    #subprocess.call([path.join(qtile_path, 'scripts', 'bar_complements')])

main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = 'urgent'
wmname = "Nya! ichi ni san, nya! arigato~"# 'LG3D'
