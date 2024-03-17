import customtkinter as ctk
import CTkListbox as ctklb 

from core.g_var import Addons

class Main(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,height=550,width=800)
        ctk.CTkLabel(self,text="分类/物品组",font=("宋体",16,"bold")).place(x=10,y=7)
        # 物品组选择
        self.groups_listbox=ctklb.CTkListbox(self,width=725,height=160,command=self.update_info,highlight_color="#1BAFEE",hover_color="#3b7cd0",text_color="#000000")
        self.groups_listbox.place(x=25,y=45)
        # 判断是否有物品组
        if "groups" in Addons.data.keys():
            # 物品组类型表
            self.groups_type={"normal":"普通物品组","locked":"锁定物品组","seasonal":"季节性物品组",
                        "nested":"父物品组","parent":"父物品组","sub":"子物品组"}
            # 添加列表
            for arg in Addons.data["groups"].keys():
                text=arg+' - '+Addons.data["groups"][arg]["item"]["name"]
                # 标注物品组类型
                if "type" in Addons.data["groups"][arg].keys():
                    # 子物品组处理
                    if Addons.data["groups"][arg]["type"]=="sub":
                        text="[子物品组(父物品组:"+Addons.data["groups"][arg]["parent"]+")] "+text
                    else:
                        text="["+self.groups_type[Addons.data["groups"][arg]["type"]]+"] "+text
                else:
                    text="[普通物品组] "+text
                self.groups_listbox.insert("end",text)
        # 物品组信息
        self.groups_info=ctklb.CTkListbox(self,width=210,height=275,button_color="#dbdbdb",text_color="#000000")
        self.groups_info.place(x=25,y=240)
        # 基本信息表
        _group_info=["物品组ID","物品组名称","物品组类型","物品组外观"]
        for arg in _group_info:
            self.groups_info.insert("end",arg)
        # 新增物品组
        ctk.CTkButton(self,text="new",width=72).place(x=700,y=230)

    # 更新分类信息
    def update_info(self,selected_option:str):
        self.groups_info.delete("all")
        group_id=selected_option.split(" ")[1]
        # 物品组ID
        self.groups_info.insert("end","物品组ID "+group_id)
        # 物品组名称
        self.groups_info.insert("end","物品组名称 "+Addons.data["groups"][group_id]["item"]["name"])
        # 物品组类型
        # 筛出无标识物品组
        if "type" in Addons.data["groups"][group_id].keys():
            self.groups_info.insert("end","物品组类型 "+self.groups_type[Addons.data["groups"][group_id]["type"]])
            # 特殊类型物品组判断-添加特殊词条
            if Addons.data["groups"][group_id]["type"]=="sub":
                self.groups_info.insert("end","父物品组 "+Addons.data["groups"][group_id]["parent"])
        else:
            self.groups_info.insert("end","物品组类型 "+"普通物品组")
        # 物品组外观
        self.groups_info.insert("end","物品组外观 "+Addons.data["groups"][group_id]["item"]["material"])