import customtkinter as ctk
import CTkListbox as ctklb 

from core.g_var import Addons

class Groups_info(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)


class Main(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,height=550,width=800)
        ctk.CTkLabel(self,text="分类/物品组",font=("宋体",16,"bold")).place(x=10,y=7)
        # 物品组选择
        self.groups_listbox=ctklb.CTkListbox(self,width=725,height=160,highlight_color="#1BAFEE",hover_color="#3b7cd0",text_color="#000000")
        self.groups_listbox.place(x=25,y=45)
        # 判断是否有物品组
        if "groups" in Addons.data.keys():
            # 物品组类型表
            groups_type={"normal":"普通物品组","locked":"锁定物品组","seasonal":"季节性物品组",
                        "nested":"父物品组","parent":"父物品组"}
            # 添加列表
            for arg in Addons.data["groups"].keys():
                text=arg+' - '+Addons.data["groups"][arg]["item"]["name"]
                # 标注物品组类型
                if "type" in Addons.data["groups"][arg].keys():
                    # 子物品组处理
                    if Addons.data["groups"][arg]["type"]=="sub":
                        text="[子物品组 - 父"+Addons.data["groups"][arg]["parent"]+"] "+text
                    else:
                        text="["+groups_type[Addons.data["groups"][arg]["type"]]+"] "+text
                else:
                    text="[普通物品组] "+text
                self.groups_listbox.insert("end",text)