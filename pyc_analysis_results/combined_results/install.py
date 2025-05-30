# Source Generated with Decompyle++
# File: install_ui.pyc (Python 3.10)

import tkinter as tk
from tkinter import ttk
import time
import os
import sys
import webbrowser
from translate import Translate
KBA_LINK = 'https://nvidia.custhelp.com/app/answers/detail/a_id/5337/~/how-do-i-install-geforce-now-on-steam-deck'

class Style:
    fg = '#b2b2b2'
    title_fg = '#ffffff'
    link_fg = '#86B637'
    bg = '#292929'
    font = 'Sans-serif'
    font_size = 11
    title_font_size = 12


class UI:
    
    def __init__(self, translate_service):
        self.root = None
        self.content_frame = None
        self.state = None
        self.ts = translate_service
        self.root = tk.Tk()
        self.root.title('GeForceNOW - Installer')
        self.root.geometry('600x360')
        self.root.overrideredirect(1)
        self.root.configure(Style.bg, **('bg',))
        window_width = 600
        window_height = 360
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = screen_width // 2 - window_width // 2
        y = screen_height // 2 - window_height // 2
        self.root.geometry(f'''{window_width}x{window_height}+{x}+{y}''')
        self.content_frame = tk.Frame(self.root, Style.bg, 20, 20, **('bg', 'padx', 'pady'))
        self.content_frame.pack(True, tk.BOTH, **('expand', 'fill'))
        self.icon_frame = tk.Frame(self.content_frame, Style.bg, **('bg',))
        self.icon_frame.pack('top', 'w', **('side', 'anchor'))
        if getattr(sys, 'frozen', False):
            gfn_logo = os.path.join(sys._MEIPASS, 'assets/icons/NVIDIA_GeForceNOW_Logo.png')
        else:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            gfn_logo = os.path.join(script_dir, 'assets/icons/NVIDIA_GeForceNOW_Logo.png')
        self.icon_image = tk.PhotoImage(gfn_logo, **('file',))
        self.scaled_icon = self.icon_image
        self.icon_label = tk.Label(self.icon_frame, self.scaled_icon, Style.bg, **('image', 'bg'))
        self.icon_label.pack('left', (20, 20), (52, 0), **('side', 'padx', 'pady'))
        self.x = None
        self.y = None
        self.root.bind('<Button-1>', self.start_move)
        self.root.bind('<B1-Motion>', self.on_drag)
        self.root.bind('<ButtonRelease-1>', self.stop_move)

    
    def _on_manage(self):
        self.state = 'MANAGE'

    
    def _on_accept(self):
        self.state = 'OK'

    
    def _on_decline(self):
        self.state = 'CANCEL'
        self.root.destroy()

    
    def _on_open_link(self, url):
        webbrowser.open(url)

    
    def wait_for_state(self):
        if not self.state:
            time.sleep(0.5)
            if self.state:
                r_state = self.state
                self.state = None
                return r_state

    
    def _add_label(self, title, sub_title, msg, learn_more = (False,)):
        if title:
            self.message_label_title = tk.Label(self.content_frame, title, (Style.font, Style.title_font_size), Style.bg, Style.title_fg, 'left', 520, 'w', '520', 20, **('text', 'font', 'bg', 'fg', 'justify', 'wraplength', 'anchor', 'width', 'padx'))
            self.message_label_title.pack((40, 10), 'w', **('pady', 'anchor'))
        if sub_title:
            self.message_label_sub_title = tk.Label(self.content_frame, sub_title, (Style.font, Style.font_size), Style.bg, Style.fg, 'left', 500, 'w', '500', 20, **('text', 'font', 'bg', 'fg', 'justify', 'wraplength', 'anchor', 'width', 'padx'))
            self.message_label_sub_title.pack((0, 0), 'w', **('pady', 'anchor'))
        if msg:
            self.message_label_msg = tk.Label(self.content_frame, msg, (Style.font, Style.font_size), Style.bg, Style.fg, 'left', 500, 'w', '500', 30 if title else 20, **('text', 'font', 'bg', 'fg', 'justify', 'wraplength', 'anchor', 'width', 'padx'))
            self.message_label_msg.pack((0, 0), 'w', **('pady', 'anchor'))
        if learn_more:
            self.message_label_learn = tk.Label(self.content_frame, self.ts.text('button', 'text', 'learn_more'), (Style.font, Style.font_size), Style.bg, Style.link_fg, 'left', 'w', 20, 'hand2', **('text', 'font', 'bg', 'fg', 'justify', 'anchor', 'padx', 'cursor'))
            self.message_label_learn.pack((0, 0), 'w', **('pady', 'anchor'))
            None(None, (lambda e = None: self._on_open_link(KBA_LINK)))
            return None

    
    def show(self):
        self.root.mainloop()

    
    def add_progress(self, msg):
        self._clean_dialog()
        style = ttk.Style(self.root)
        style.theme_use('default')
        style.configure('green.Horizontal.TProgressbar', Style.bg, 0, 0.5, '#76b900', **('troughcolor', 'thickness', 'borderwidth', 'background'))
        self.progress_bar = ttk.Progressbar(self.content_frame, 'progress', 'green.Horizontal.TProgressbar', 'indeterminate', 520, **('name', 'style', 'mode', 'length'))
        self.progress_bar.pack((20, 20), (40, 0), **('padx', 'pady'))
        self.progress_bar.start()
        self.progress_label = tk.Label(self.content_frame, 'progress_label', msg, (Style.font, Style.font_size), Style.bg, Style.fg, 'w', 520, 0, **('name', 'text', 'font', 'bg', 'fg', 'anchor', 'width', 'padx'))
        self.progress_label.pack((20, 20), (10, 0), **('padx', 'pady'))

    
    def update_progress_text(self, msg):
        None(None, (lambda : self.progress_label.config(msg, **('text',))))

    
    def _clean_dialog(self):
        for widget in self.content_frame.winfo_children():
            if widget.winfo_id() == self.icon_frame.winfo_id():
                continue
            widget.destroy()

    
    def display_error(self, title, sub_title, msg, learn_more = (True,)):
        self._clean_dialog()
        self._add_label(title, sub_title, msg, learn_more)
        self.ok_button = tk.Button(self.content_frame, self.ts.text('button', 'text', 'close'), self.root.destroy, (Style.font, Style.font_size), Style.bg, Style.fg, 0, **('text', 'command', 'font', 'bg', 'fg', 'highlightthickness'))
        self.ok_button.pack('bottom', 'e', (10, 0), **('side', 'anchor', 'pady'))

    
    def add_success_message(self, title, sub_title, msg):
        self._clean_dialog()
        self._add_label(title, sub_title, msg)
        self.ok_button = tk.Button(self.content_frame, self.ts.text('button', 'text', 'close'), self.root.destroy, (Style.font, Style.font_size), Style.bg, Style.fg, 0, **('text', 'command', 'font', 'bg', 'fg', 'highlightthickness'))
        self.ok_button.pack('bottom', 'e', (10, 0), **('side', 'anchor', 'pady'))

    
    def ask_install(self, title, sub_title, msg, learn_more = (True,)):
        self._clean_dialog()
        self._add_label(title, sub_title, msg, learn_more)
        button_frame = tk.Frame(self.content_frame, Style.bg, **('bg',))
        button_frame.pack('bottom', 'e', **('side', 'anchor'))
        decline_button = tk.Button(button_frame, self.ts.text('button', 'text', 'manage'), self._on_manage, (Style.font, Style.font_size), Style.bg, Style.fg, 0, **('text', 'command', 'font', 'bg', 'fg', 'highlightthickness'))
        decline_button.grid(0, 0, (10, 10), **('row', 'column', 'padx'))
        accept_button = tk.Button(button_frame, self.ts.text('button', 'text', 'reinstall'), self._on_accept, (Style.font, Style.font_size), Style.bg, Style.fg, 0, **('text', 'command', 'font', 'bg', 'fg', 'highlightthickness'))
        accept_button.grid(0, 1, (10, 0), **('row', 'column', 'padx'))

    
    def ask_uninstall(self, title, sub_title, msg, learn_more = (True,)):
        self._clean_dialog()
        self._add_label(title, sub_title, msg, learn_more)
        button_frame = tk.Frame(self.content_frame, Style.bg, **('bg',))
        button_frame.pack('bottom', 'e', **('side', 'anchor'))
        decline_button = tk.Button(button_frame, self.ts.text('button', 'text', 'cancel'), self._on_decline, (Style.font, Style.font_size), Style.bg, Style.fg, 0, **('text', 'command', 'font', 'bg', 'fg', 'highlightthickness'))
        decline_button.grid(0, 0, (10, 10), **('row', 'column', 'padx'))
        accept_button = tk.Button(button_frame, self.ts.text('button', 'text', 'uninstall'), self._on_accept, (Style.font, Style.font_size), Style.bg, Style.fg, 0, **('text', 'command', 'font', 'bg', 'fg', 'highlightthickness'))
        accept_button.grid(0, 1, (10, 0), **('row', 'column', 'padx'))

    
    def start_move(self, event):
        self.x = event.x_root - self.root.winfo_x()
        self.y = event.y_root - self.root.winfo_y()

    
    def stop_move(self, event):
        self.x = None
        self.y = None

    
    def on_drag(self, event):
        if self.x is not None or self.y is not None:
            x = event.x_root - self.x
            y = event.y_root - self.y
            self.root.geometry(f'''+{x}+{y}''')
            return None
        return None


