import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter.filedialog import askdirectory
from ttkbootstrap.scrolled import ScrolledFrame
import threading

global app_list
global install_list
install_list = []
app_list = ['wx', 'qq', 'potplayer', 'bandzip']


# 获取路径模块
def selectPath(path):
    path_ = askdirectory()  # 使用askdirectory()方法返回文件夹的路径
    if path_ == "":
        path.get()  # 当打开文件路径选择框后点击"取消" 输入框会清空路径，所以使用get()方法再获取一次路径
    else:
        path_ = path_.replace("/", "\\")  # 实际在代码中执行的路径为“\“ 所以替换一下
        path.set(path_)


# 主页面
class MainPage:
    def __init__(self, master: ttk.Window):
        self.root = master
        self.root.title("自动安装程序v1.0")
        self.root.geometry(f"{800}x{400}")
        self.root.place_window_center()
        # page
        self.page = ttk.Frame()
        self.page.pack(fill=BOTH, expand=YES, padx=20, pady=10)
        # 调用菜单栏
        self.create_page()
        self.left()

    # 右边
    def right(self):
        fr_install_list = ttk.Frame(self.page)

    # 左边
    def left(self):
        # check值设置
        var_wx = ttk.StringVar(value="F")
        var_qq = ttk.StringVar(value="F")
        var_potplayer = ttk.StringVar(value="F")
        var_bandzip = ttk.StringVar(value="F")
        # 安装路径设置
        wx_path = ttk.StringVar(value="C:\Program Files\Tencent\WeChat")
        qq_path = ttk.StringVar(value="C:\Program Files\Tencent\WeChat")
        bandzip_path = ttk.StringVar(value="C:\Program Files\Tencent\WeChat")
        potplayer_path = ttk.StringVar(value="C:\Program Files\Tencent\WeChat")
        # 编写左tip
        tip = ttk.Label(self.page, text="请选择安装软件及路径", font=('微软雅黑', 20))
        tip.grid(row=0, column=1)
        # 编写左方组
        fr_left = ScrolledFrame(self.page, width=470, height=300, bootstyle='round')
        fr_left_yes = ttk.Frame(fr_left)
        fr_left_path = ttk.Frame(fr_left)
        fr_left_choose = ttk.Frame(fr_left)
        fr_left.grid(row=2, column=1, pady=10)
        fr_left_yes.grid(row=0, column=1)
        fr_left_path.grid(row=0, column=2)
        fr_left_choose.grid(row=0, column=3)
        # fr_left_yes编写
        wx_check = ttk.Checkbutton(fr_left_yes, onvalue='T', offvalue='F', variable=var_wx, text='   微信   ',
                                   bootstyle='success-toolbutton')
        qq_check = ttk.Checkbutton(fr_left_yes, onvalue='T', offvalue='F', variable=var_qq, text='    QQ   ',
                                   bootstyle='danger-toolbutton')
        bandzip_check = ttk.Checkbutton(fr_left_yes, onvalue='T', offvalue='F', variable=var_bandzip, text=' Bandzip ',
                                        bootstyle='toolbutton')
        potplayer_check = ttk.Checkbutton(fr_left_yes, onvalue='T', offvalue='F', variable=var_potplayer,
                                          text='Potplayer', bootstyle='warning-toolbutton')
        wx_check.pack(padx=10, pady=5, anchor=W)
        qq_check.pack(padx=10, pady=5, anchor=W)
        bandzip_check.pack(padx=10, pady=5, anchor=W)
        potplayer_check.pack(padx=10, pady=5, anchor=W)
        # fr_left_path
        wx_l = ttk.Entry(fr_left_path, width=30, textvariable=wx_path, font=('微软雅黑', 9), bootstyle='success')
        qq_l = ttk.Entry(fr_left_path, width=30, textvariable=qq_path, font=('微软雅黑', 9), bootstyle='danger')
        bandzip_l = ttk.Entry(fr_left_path, width=30, textvariable=bandzip_path, font=('微软雅黑', 9))
        potplayer_l = ttk.Entry(fr_left_path, width=30, textvariable=potplayer_path, font=('微软雅黑', 9),
                                bootstyle='warning')
        wx_l.pack(pady=5, padx=10)
        qq_l.pack(pady=5, padx=10)
        bandzip_l.pack(pady=5, padx=10)
        potplayer_l.pack(pady=5, padx=10)
        # fr_left_Button
        wx_b = ttk.Button(fr_left_choose, command=lambda: selectPath(wx_path), text='选择路径', bootstyle='success')
        qq_b = ttk.Button(fr_left_choose, command=lambda: selectPath(qq_path), text='选择路径', bootstyle='danger')
        bandzip_b = ttk.Button(fr_left_choose, command=lambda: selectPath(bandzip_path), text='选择路径')
        potplayer_b = ttk.Button(fr_left_choose, command=lambda: selectPath(potplayer_path), text='选择路径',
                                 bootstyle='warning')
        wx_b.pack(anchor=NE, pady=5, padx=5)
        qq_b.pack(anchor=NE, pady=5, padx=5)
        bandzip_b.pack(anchor=NE, pady=5, padx=5)
        potplayer_b.pack(anchor=NE, pady=5, padx=5)

    # 菜单栏
    def create_page(self):
        menubar = ttk.Menu(self.root, type="menubar")
        menubar.add_command(label="设置")
        menubar.add_command(label="关于")
        self.root['menu'] = menubar


if __name__ == '__main__':
    root = ttk.Window()
    MainPage(master=root)
    root.mainloop()
