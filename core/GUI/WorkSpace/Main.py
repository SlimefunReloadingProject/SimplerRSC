import customtkinter as ctk

from core.g_var import GUI
from core.GUI.WorkSpace.SideSelectionBar import SideSelectionBar

class Main(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,width=1000,height=550,fg_color="#ebebeb")
        # 侧边栏
        SideSelectionBar(self).place(x=0,y=0)

    def WorkSpace_Frame(self,Frame:ctk.CTkFrame):
        # 清理工作区
        if GUI.WorkSpace_Frame!=None:
            GUI.WorkSpace_Frame.destroy()
        # 放在工作区
        GUI.WorkSpace_Frame=Frame(self).place(x=200,y=0)
