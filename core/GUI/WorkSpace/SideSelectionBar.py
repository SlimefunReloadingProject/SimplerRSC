import customtkinter as ctk

from core.g_var import Addons
from core.handle.SaveAddons import SaveAddons
import core.main

class SideSelectionBar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master,width=200,height=550,fg_color="#e1e1e1")
        # 保存附属
        ctk.CTkButton(self,text="保存 Ctrl+S",height=35,width=172,command=SaveAddons).place(x=14,y=495)
        core.main.main.bind("<Control-s>",Save_Addons)

def Save_Addons(e):
    SaveAddons()