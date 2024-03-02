import customtkinter as ctk
import core.main

# 顶栏
class TopHurdle(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,width=1000,height=50)
        # 标题
        self.top_title=ctk.CTkLabel(self,text="SimplerRSC",font=("微软雅黑",17),text_color="#000000",fg_color="#d7d7d7")
        self.top_title.place(x=20,y=10)
        # 关闭按钮
        ctk.CTkButton(self,text="X",text_color="#ffffff",font=("微软雅黑",17,"bold"),width=50,height=50,command=master.close_win,fg_color="#d7d7d7",hover_color="#d0d0d0").place(x=950,y=0)

class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.attributes('-topmost','true')
        self.title("SimplerRSC - Main")
        self.geometry("1000x600")
        self.resizable(0, 0)
        self.overrideredirect(True)
        self.wm_attributes('-transparentcolor','#0000ff')
        self.attributes('-topmost','false')
        # 顶栏
        self.Top_hurdle=TopHurdle(self)
        self.Top_hurdle.place(x=0,y=0)
        # 识别鼠标拖拽事件
        self.winx=0
        self.winy=0
        self.Top_hurdle.bind("<ButtonPress-1>",on_drag_start)
        self.Top_hurdle.bind("<B1-Motion>",on_drag)
        self.Top_hurdle.bind("<ButtonRelease-1>",on_drag_stop)

    # 关闭按钮
    def close_win(self):
        self.destroy()

# 处理鼠标按下事件
def on_drag_start(event):
    # 识别按下位置
    core.main.main.winx=event.x
    core.main.main.winy=event.y

# 处理鼠标移动事件
def on_drag(event):
    if core.main.main.winy!=0:
        deltax=event.x-core.main.main.winx
        deltay=event.y-core.main.main.winy
        new_x=core.main.main.winfo_x()+deltax
        new_y=core.main.main.winfo_y()+deltay
        core.main.main.geometry(f"+{new_x}+{new_y}")

# 处理鼠标释放事件
def on_drag_stop(event):
    core.main.main.winx=0
    core.main.main.winy=0