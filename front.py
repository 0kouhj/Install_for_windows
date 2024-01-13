import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText
from main import MainPage


class FrontPage:
    def __init__(self, master: ttk.Window):
        def change():
            self.page.destroy()
            MainPage(self.root)
        # 杂项设置
        self.root = master
        self.root.title("提示")
        # 设置软件长宽
        self.width_root = int(300 * 1.618)
        self.height_root = 300
        # 获取windows长宽，使窗口对准屏幕中心
        self.windows_x = self.root.winfo_screenwidth()
        self.windows_y = self.root.winfo_screenheight()
        self.x = (self.windows_x - self.width_root) / 2
        self.y = (self.windows_y - self.height_root) / 2
        self.root.geometry(f"{self.width_root}x{self.height_root}+{int(self.x)}+{int(self.y)}")

        self.page = tk.Frame(self.root)
        self.page.pack()

        self.title = ttk.Label(self.page, text="         免责声明及注意事项         ", font=('微软雅黑', 20))
        self.title.pack(anchor=N)

        self.Note = ScrolledText(self.page, bootstyle="litera", padding=5, height=11, width=20)
        self.Note.pack(fill=BOTH, expand=YES)
        self.Note.insert(END,
                         "                         该软件仅使用于windows系统\n请务必认真阅读和理解本《软件许可使用协议》（以下简称《协议》）中规定的所有权利和限制。除非您接受本《协议》条款，否则您无权下载、安装或使用本”软件”及其相关服务。您一旦安装、复制、下载、访问或以其它方式使用本软件产品，将视为对本《协议》的接受，即表示您同意接受本《协议》各项条款的约束。如果您不同意本《协议》中的条款，请不要安装、复制或使用本软件。\n1.权利声明本”软件”的一切知识产权，以及与”软件”相关的所有信息内容，包括但不限于：文字表述及其组合、图标、图饰、图像、图表、色彩、界面设计、版面框架、有关数据、附加程序、印刷材料或电子文档等均为作者所有，受著作权法和国际著作权条约以及其他知识产权法律法规的保护。\n2.许可范围\n2.1下载、安装和使用：本软件为免费软件，用户可以非商业性、无限制数量地下载、安装及使用本软件。\n2.2复制、分发和传播：用户可以非商业性、无限制数量地复制、分发和传播本软件产品。但必须保证每一份复制、分发和传播都是完整和真实的，包括所有有关本软件产品的软件、电子文档，版权和商标，亦包括本协议。\n3.权利限制\n3.1禁止反向工程、反向编泽和反向汇编：用户不得对本软件产品进行反向工程(Rverse Engineer)、反向编译(Decompile)或反向汇编(Disassemble),同时不得改动编译在程序文件内部的任何资源。除法律、法规明文规定允许上述活动外，用户必须遵守此协议限制。\n3.2组件分割：本软件产品是作为一个单一产品而被授予许可使用，用户不得将各个部分分开用于任何目的。\n3.3个别授权：如需进行商业性的销售、复制、分发，包括但不限于软件销售、预装、捆绑等，必须获得作者的授权和许可。\n3.4保留权利：本协议未明示授权的其他一切权利仍归作者所有，用户使用其他权利时必须获得作者的书面同意。\n4.用户使用须知\n4.1本软件由作者提供产品支持。\n4.2软件的修改和升级：作者保留为用户提供本软件的修改、升级版本的权利。\n4.3本软件不含有任何旨在破坏用户计算机数据和获取用户隐私信息的恶意代码，不含有任何跟踪、监视用户计算机的功能代码，不会监控用户网上、网下的行为，不会收集用户使用其它软件、文档等个人信息，不会泄漏用户隐私。\n4.4用户应在遵守法律及本协议的前提下使用本软件。用户无权实施包括但不限于下列行为：\n4.4.1不得故意避开或者破坏著作权人为保护本软件著作权而采取的技术措施，\n4.4.2用户不得利用本软件误导、欺骗他人：\n4.4.3违反国家规定，对计算机信息系统功能进行删除、修改、增加、干扰，造成计算机信息系统不能正常运行，\n4.4.4未经允许，进入计算机信息风网络或者使用计算机信息网络资源\n4.4.5未经允许，对计算机信息网络功能进行删除、修改或者增加的；\n4.4.6未经允许，对计算机信息网络中存储、处理或者传输的数据和应用程序进行删除、修改或者增加；\n4.4.7破坏本软件系统或网站的正常运行，故意传播计算机病毒等破坏性程序：\n4.4.8其他任何危害计算机信息网络安全的。\n4.8对于从非作者指定站点下载的本软件产品以及从非作者发行的介质上获得的本软件产品，作者无法保证该软件是否感染计算机病毒、是否隐藏有伪装的特洛伊木马程序或者黑客软件，使用此类软件，将可能导致不可预测的风险，建议用户不要轻易下载、安装、使用，作者不承担任何由此产生的一切法律责任。\n4.8.1不得使用本软件发布违反国家法律的非法广告信息，如色情，赌博等，其造成的一切后果与本作者无关，请自觉营造和谐良性的网络营销环境。违法行为一经发现，本作者有权终止服务并追究法律责任。\n5.免责与责任限制\n5.1本软件经过详细的测试，但不能保证与所有的软硬件系统完全兼容，不能保证本软件完全没有错误。如果无法解决兼容性问题，用户可以删除本软件。\n5.2使用本软件产品风险由用户自行承担，在适用法律允许的最大范围内，对因使用或不能使用本软件所产生的损害及风险，包括但不限于直接或间接的个人损害、商业赢利的丧失、贸易中断、商业信息的丢失或任何其它经济损失，作者不承担任何责任。\n5.3对于因电信系统或互联网网络故障、计算机故障或病毒、信息损坏或丢失、计算机系统问题或其它任何不可抗力原因而产生损失，作者不承担任何责任。\n5.4用户违反本协议规定，对作者公司造成损害的。作者有权采取包括但不限于中断使用许可、停止提供服务、限制使用、法律追究等措施。\n6.法律及争议解决6.1本协议适用中华人民共和国法律。\n6.2因本协议引起的或与本协议有关的任何争议，各方应友好协商解决：协商不成的，任何一方均可将有关争议提交至仲裁委员会并按照其届时有效的仲裁规则仲裁，仲裁裁决是终局的，对各方均有约束力。\n7.其他条款\n7.1如果本协议中的任何条款无论因何种原因完全或部分无效或不具有执行力，或违反任何适用的法律，则该条款被视为删除，但本协议的其余条款仍应有效并且有约束力。\n7.2作者有权根据有关法律、法规的变化以及公司经营状况和经营策略的调整等修改本协议。修改后的协议会随附于新版本软件。当发生有关争议时，以最新的协议文本为准。如果不同意改动的内容，用户可以自行删除本软件。如果用户继续使用本软件，则视为您接受本协议的变动。\n7.3本协议的一切解释权与修改权归作者。")

        fr = ttk.Frame(self.page)
        fr.pack(side=BOTTOM)
        self.Button_yes = ttk.Button(fr, text='同意', bootstyle='litera',command=change)
        self.Button_yes.pack(side=LEFT, padx=20)
        self.Button_no = ttk.Button(fr, text='不同意', bootstyle='litera', command=self.page.quit)
        self.Button_no.pack(side=RIGHT, padx=10)


if __name__ == '__main__':
    root = ttk.Window()
    FrontPage(master=root)
    root.mainloop()
