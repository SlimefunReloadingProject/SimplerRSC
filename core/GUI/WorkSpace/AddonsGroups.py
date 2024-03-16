import customtkinter as ctk

class AddonsGroups(ctk.CTkScrollableFrame):
    def __init__(self,master):
        super().__init__(master)

class Main(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,height=550,width=800)