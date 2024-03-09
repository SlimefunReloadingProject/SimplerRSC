import customtkinter as ctk

from core.GUI.WorkSpace.SideSelectionBar import SideSelectionBar

class Main(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,width=1000,height=550,fg_color="#ebebeb")
        # 侧边栏
        SideSelectionBar(self).place(x=0,y=0)
