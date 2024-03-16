import customtkinter as ctk

import core.main
from core.GUI.WorkSpace.AddonsGroups import Main as AddonsGroups_Main
from core.g_var import Addons
from core.handle.SaveAddons import SaveAddons
import core.main

class SideSelectionBar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master,width=200,height=550,fg_color="#e1e1e1")
        # 附属名称
        ctk.CTkLabel(self,text=Addons.data["info"]["id"],width=200).place(x=0,y=3)
        # 物品组
        ctk.CTkButton(self,text="物品组/分类",width=202,command=self.AddonsGroups,text_color="#000000",border_color="#d1d1d1",border_width=1,hover_color="#d5d5d5",height=35,fg_color="transparent",corner_radius=0).place(x=-1,y=35)
        # 物品
        ctk.CTkButton(self,text="物品",width=202,text_color="#000000",border_color="#d1d1d1",border_width=1,hover_color="#d5d5d5",height=35,fg_color="transparent",corner_radius=0).place(x=-1,y=68)
        # 保存附属
        ctk.CTkButton(self,text="保存 Ctrl+S",width=172,height=35,command=SaveAddons).place(x=14,y=495)
        core.main.main.bind("<Control-s>",Save_Addons)

    def AddonsGroups(self):
        self.WorkSpace_Frame(AddonsGroups_Main)

    def WorkSpace_Frame(self,Frame):
        core.main.main.WorkSpace_Main.WorkSpace_Frame(Frame)

def Save_Addons(e):
    SaveAddons()