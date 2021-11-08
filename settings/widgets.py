from libqtile.widget import (
    Sep, 
    GroupBox, 
    CurrentLayoutIcon,
    TextBox, 
    Spacer, 
    GenPollText,
)

from settings.theme import colors
from custom.windowname import WindowName as CustomWindowName
from settings.path import qtile_path
from os import path, system
import datetime

BGMGR = 'color0'
FGMGR = 'color1'

def base(fg=FGMGR, bg=BGMGR, font='Fira Code'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg],
        'font': font
    }

def separator(padding=5, bg=BGMGR):
    return Sep(**base(bg=bg), linewidth=0, padding=padding)


def texts(fg=FGMGR, bg=BGMGR, fontsize=16, text="?", padding=3, font='Fira Code'):
    return TextBox(
        **base(fg=fg, bg=bg, font=font),
        fontsize=fontsize,
        text=text,
        padding=padding
    )


group_box_settings = {
    "padding": 15,
    "borderwidth": 0,
    "disable_drag": True,
    "font": 'Fira Code',
    "rounded": True,
    "highlight_color": colors[FGMGR],
    "this_screen_border": colors['color4'],
    "other_current_screen_border": colors[BGMGR],
    "other_screen_border": colors[BGMGR],
    "foreground": colors[FGMGR],
    "background": colors[BGMGR],
    "urgent_border": colors[BGMGR],
    "fontsize": 15,


    "margin_x": 0,
    "margin_y": 1,
    "this_current_screen_border": colors[BGMGR],
    "urgent_text": colors[FGMGR],
    "inactive": colors['color3'],
    "active": colors['color1']
}

def workspaces():
    return [
        GroupBox(
            **group_box_settings,
            visible_groups=["一"],
            block_highlight_text_color=colors['color2'],
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["二"],
            block_highlight_text_color=colors['color4'],
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["三"],
            block_highlight_text_color=colors['color5'],
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["四"],
            block_highlight_text_color=colors['color6'],
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["五"],
            block_highlight_text_color=colors['color7'],
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["六"],
            block_highlight_text_color=colors['color4'],
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["七"],
            block_highlight_text_color=colors['color9'],
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["八"],
            block_highlight_text_color=colors['color5'],
        ),
        GroupBox(
            **group_box_settings,
            visible_groups=["九"],
            block_highlight_text_color=colors['color7'],
        )
        
    ]
    
# def widgets():
#     return [
#         text(fg='color2', bg=BGMGR, fontsize=15, text='東', padding=3),
#         separator(padding=12, bg=BGMGR),
#         text(fg='color5', bg=BGMGR, fontsize=15, text='西', padding=3),
#         separator(padding=12, bg=BGMGR),
#         text(fg='color4', bg=BGMGR, fontsize=16, text='南', padding=3),
#         separator(padding=12, bg=BGMGR),
#         text(fg='color6', bg=BGMGR, fontsize=16, text='北', padding=3),
#     ]

bar_widgets = [
    separator(padding=8, bg=BGMGR),

    CurrentLayoutIcon(
        custom_icon_paths=[path.join(qtile_path, "icons", "Layouts-color-deep-mixed")],
        **base(bg=BGMGR, fg=FGMGR),
        padding=0,
        scale=0.37,
        fontsize=0.5
    ),
    #----
    *workspaces(),
    separator(padding=305, bg=BGMGR),
   
#    text(fg='color3', bg=BGMGR, text='|', fontsize=10, padding=-2),
#    separator(padding=10, bg=BGMGR),
#
#   *widgets(),
    
    CustomWindowName(
        **base(),
        max_chars=25,
        fontsize=13,
        empty_group_string='Desktop',
    ),

    # MERGE THE SCRIPTS - tmr

    #GenPollText(
    #    **base(),
    #    func=lambda: short_format(),
    #    update_interval=20,
    #    fontsize=13,
    #    ),
    
   separator(padding=15, bg=BGMGR),
]

secondary_widgets = [
    Spacer(**base()),
]

widget_defaults = {
    'font': 'Fira Code',
    'fontsize': 14,
    'padding': 1,
}

extension_defaults = widget_defaults.copy()
