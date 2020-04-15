import math
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog


class Painter(Tk):
    def __init__(self, startX=0, startY=0, curX=0, curY=0, endX=0, endY=0,
                 line=False, rect=False, oval=False, arc=False, circle=False, polygon=False):
        Tk.__init__(self, )
        self.title('Tkinter Draw')
        self.geometry('800x600')
        self.resizable(width=False, height=False)
        self.line = line
        self.rect = rect
        self.oval = oval
        self.arc = arc
        self.circle = circle
        self.polygon = polygon
        self.startX = startX
        self.startY = startY
        self.curX = curX
        self.curY = curY
        self.endX = endX
        self.endY = endY
        self.menu_bar = Menu(self)
        self.file_menu = Menu(self.menu_bar, tearoff=False)
        self.file_menu.add_command(label="新建", command=self.clean)
        self.file_menu.add_command(label="退出", command=self.destroy)
        self.menu_bar.add_cascade(label='文件', menu=self.file_menu)
        self.draw_menu = Menu(self.menu_bar, tearoff=False)
        self.draw_menu.add_command(label='椭圆', command=self.create_oval)
        self.draw_menu.add_command(label='圆', command=self.create_circle)
        self.draw_menu.add_command(label='圆弧', command=self.create_arc)
        self.draw_menu.add_command(label='矩形', command=self.create_rect)
        self.draw_menu.add_command(label='直线', command=self.create_line)
        self.menu_bar.add_cascade(label='绘图', menu=self.draw_menu)
        self.setting_menu = Menu(self.menu_bar, tearoff=False)
        self.setting_menu.add_command(label='设置图形样式...', command=self.settings)
        self.menu_bar.add_cascade(label='设置', menu=self.setting_menu)
        self.help_menu = Menu(self.menu_bar, tearoff=False)
        self.help_menu.add_command(label="关于", command=self.about)
        self.help_menu.add_command(label='使用帮助', command=self.helps)
        self.menu_bar.add_cascade(label='帮助', menu=self.help_menu)
        self.config(menu=self.menu_bar)
        self.canvas = Canvas(self, width=500, height=400, )
        self.canvas.bind('<Button-1>', self.get_start_info)
        self.canvas.bind('<ButtonRelease-1>', self.get_end_info)
        self.canvas.bind('<Motion>', self.get_cur_info)
        self.canvas.pack(side=TOP, expand=YES, fill=BOTH)

    def get_start_info(self, event):
        self.startX = event.x
        self.startY = event.y

    def get_cur_info(self, event):
        self.curX = event.x
        self.curY = event.y

    def get_end_info(self, event):
        self.endX = event.x
        self.endY = event.y
        if self.line:
            self.canvas.create_line(self.startX, self.startY, self.endX, self.endY, fill='blue')
        elif self.rect:
            self.canvas.create_rectangle(self.startX, self.startY, self.endX, self.endY, fill='red',
                                         tags="rect")
        elif self.oval:
            self.canvas.create_oval(self.startX, self.startY, self.endX, self.endY, fill='green',
                                    tags='oval')
        elif self.arc:
            self.canvas.create_arc(self.startX, self.startY, self.endX, self.endY, start=0, extent=90, width=2,
                                   fill="yellow", tags="arc")
        elif self.circle:
            x = self.startX
            y = self.startY
            r = math.sqrt((self.endX - x) ** 2 + (self.endY - y) ** 2)
            self.canvas.create_oval(x - r, y - r, x + r, y + r, fill='pink',
                                    tags='circle')

    def create_oval(self):
        self.oval = True
        self.rect = False
        self.line = False
        self.arc = False
        self.circle = False
        self.polygon = False

    def create_rect(self):
        self.rect = True
        self.line = False
        self.oval = False
        self.arc = False
        self.circle = False
        self.polygon = False

    def create_line(self):
        self.line = True
        self.rect = False
        self.oval = False
        self.arc = False
        self.circle = False
        self.polygon = False

    def create_arc(self):
        self.arc = True
        self.line = False
        self.rect = False
        self.oval = False
        self.circle = False
        self.polygon = False

    def create_circle(self):
        self.circle = True
        self.line = False
        self.rect = False
        self.oval = False
        self.arc = False
        self.polygon = False

    @staticmethod
    def helps():
        messagebox.showinfo('帮助', '1.从菜单栏中选择想要绘制的图形，移动鼠标至绘图区内；\n2.使用鼠标在主窗口绘图区中单击，选择图形起始点；\n3'
                                  '.单击后不要松开鼠标，继续拖动至所绘制图形结束点；\n4.松开鼠标即可画出相应的图形。')

    @staticmethod
    def settings():
        messagebox.showinfo('Warning', '功能开发中，稍后再撩！')

    def clean(self):
        self.update()
        self.canvas.delete('all')

    @staticmethod
    def about():
        messagebox.showinfo('关于', 'Tkinter 绘图程序')


if __name__ == "__main__":
    Painter().mainloop()
