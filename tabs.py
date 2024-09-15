import tkinter
import tkinter.messagebox
import customtkinter
# from customtkinter import CTk, CTkOptionMenu, CTkLabel
from CTkMessagebox import CTkMessagebox

def main():
    app = App()
    app.title("ASA Server Manager")
    app.mainloop()

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # create tabs
        self.tabs = ['Dashboard', 'Settings', 'tab 1', 'tab 2', 'tab 3']
        for name in self.tabs: 
            self.add(name=name)
            self.label = customtkinter.CTkLabel(master=self.tab(name))
            # self.label = customtkinter.CTkLabel(master=self.tab(tab.replace('_',' ')))
        self.dashboard()
        self.tab_2()
        self.tab_3()        
        # add widgets on tabs
        self.label.grid(row=0, column=0, padx=10, pady=5)
    def dashboard(self):
        self.button_1 = customtkinter.CTkButton(self.tab("Dashboard"),text='dashboard',command=lambda: self.blah(button=1))
        self.button_1.grid(row=0, column=0, padx=20, pady=20)

    def tab_1(self):
        # self.add("tab 1")
        self.label = customtkinter.CTkLabel(master=self.tab("tab 1"))

    def tab_2(self):
        # self.add("tab 2")
        self.button_1 = customtkinter.CTkButton(self.tab("tab 2"),text='penis',command=lambda: self.blah(button=1))
        # self.button_1.pack(padx=20, pady=20)
        self.button_1.grid(row=0, column=0, padx=20, pady=20)  

    def tab_3(self):
        # self.add("tab 3")
        self.newTabName = customtkinter.CTkEntry(self.tab("tab 3"), placeholder_text="CTkEntry")
        self.newTabName.grid(row=0, column=1, padx=5, pady=5)
        # value = self.newTabName.get()
        self.button_2 = customtkinter.CTkButton(self.tab("tab 3"),text='Create New Tab',command=lambda: self.blah(button=3, action="newtab", tab_title=self.newTabName.get()))
        self.button_2.grid(row=0, column=3, padx=5, pady=5)
        self.button_3 = customtkinter.CTkButton(self.tab("tab 3"),text='Delete Tab',command=lambda: self.blah(button=3, action="deltab", tab_title=self.newTabName.get()))
        self.button_3.grid(row=2, column=3, padx=5, pady=5) 

    def blah(self,button, action=None, tab_title=None):
        print(f"action: {action}, tab_title: {tab_title}")
        if action:
            if "newtab" in action:
                if tab_title:
                    try:
                        self.add(f"{tab_title}")
                    except Exception as e:
                        if "CTkTabview already has tab named" in str(e):
                            self.display_message(message="dumb dumb message", title="Dumb Dumb title")
            if "deltab" in action:
                # self.display_message(message="deleted tab", title="Deleted Tab")
                immutible = ['Dashboard','Settings']
                if tab_title not in immutible:
                    self.delete(f"{tab_title}")
                    # self.display_message(message="Nope", title='Fuck No')
                

    def display_message(self, message, title):
        CTkMessagebox(title=title, message=message)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)
        self.exit_button = customtkinter.CTkButton(master=self, text="Quit", command=self.destroy).grid(row=5, column=0)



if __name__ == "__main__":
    main()

