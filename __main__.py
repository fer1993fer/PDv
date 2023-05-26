
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
import os
from time import sleep


class App(tk.Tk) :
    def __init__(self) :
        super().__init__()
        self.geometry("455x150")
        self.resizable(False, False)

        self.fr1 = ttk.Frame(master=self)
        self.fr1.configure(height=150, width=270, style="F1.TFrame", border=0)
        self.fr2 = ttk.Frame(master=self)
        self.fr2.configure(height=150, width=185, style="F2.TFrame")
        self.fr3 = ttk.Frame(master=self.fr1)
        self.fr3.configure(height=60, width=240, style="F3.TFrame", borderwidth=2)
        self.fr1.place(x=0, y=0)
        self.fr2.place(x=271, y=0)
        self.fr3.place(x=13, y=45)

        
        self.etk = ttk.Label(master=self.fr1)
        self.etk.configure(text="X", foreground="red", background="Black")
        self.etk2 = ttk.Label(master=self.fr1)
        self.etk2.configure(text="videos", foreground="white", background="black")
        self.etk3 = ttk.Label(master=self.fr1)
        self.etk3.configure(text="85", foreground="red", background="black")
        self.etk4 = ttk.Label(master=self.fr1)
        self.etk4.configure(text="TUBE", foreground="white", background="black")
        self.etk41 = ttk.Label(master=self.fr1)
        self.etk41.configure(text="MISS", foreground="white", background="black")
        self.etk42 = ttk.Label(master=self.fr1)
        self.etk42.configure(text="AV", foreground="pink", background="black")
        self.etk5 = ttk.Label(master=self.fr2)
        self.etk5.configure(text="5f肉抱", foreground="green", background="white")
        self.etk6 = ttk.Label(master=self.fr2)
        self.etk6.configure(text="Tk Tube ", foreground="gray", background="white")
        self.etkURL = ttk.Label(master=self.fr3)
        self.etkURL.configure(text="URL : ", background="black", foreground="white")
        self.etk.place(x=12, y=10)
        self.etk2.place(x=23, y=10)
        self.etk3.place(x=100, y=10)
        self.etk4.place(x=118, y=10)
        self.etk41.place(x=200, y=10)
        self.etk42.place(x=233,y=10)
        self.etk5.place(x=20, y=10)
        self.etk6.place(x=100, y=10)
        self.etkURL.place(x=15, y=23)
    
        self.ent1 = ttk.Entry(master=self.fr3)
        self.ent1.configure(width=17)  
        self.ent1.place(x=60, y=20)

        
        self.txt2 = tk.Text(master=self.fr2, background="black", width=18, height=1, foreground="white", borderwidth=0)
    
        self.etkguar = ttk.Button(master=self.fr2)
        self.etkguar.configure(text="Carpeta de Destino", style="Toolbutton", command=self.destino)
        self.btn1 = ttk.Button(master=self.fr1)
        self.btn1.configure(text="Descargar", style="F.Toolbutton", command=self.descarga)
        self.btn2 = ttk.Button(master=self.fr2)
        self.btn2.configure(text="Descargar", style="F2.Toolbutton", command=self.descarga2)
        self.btn3 = ttk.Button(master=self.fr3)
        self.btn3.configure(text="URL :",style="F3.Toolbutton", command=self.url)
        self.etkguar.place(x=24, y=40)
        self.btn1.place(x=96, y=120)
        


        self.s = ttk.Style()
        self.s.configure("F1.TFrame", background="black", relief="groove")
        self.s.configure("F2.TFrame", background="white")
        self.s.configure("F3.TFrame", background="black", relief="solid")
        self.s.configure("Toolbutton", background="white", foreground="black")
        self.s.map("Toolbutton",\
                   background=[("disabled", "white"), ("active", "white"), ("pressed", "white")])
        self.s.configure("F.Toolbutton", background="black", foreground="black", borderwith="0", relief="solid")
        self.s.map("F.Toolbutton",\
                   background=[("disabled", "black"), ("active", "black")],
                   foreground=[("active", "red"), ("pressed", "white")],
                   relief=[("active", "groove")])
        self.s.configure("F2.Toolbutton", background="white", foreground="white")
        self.s.map("F2.Toolbutton",\
                   background=[("disabled", "white"), ("active", "white")],
                   foreground=[("active", "green")],
                   relief=[("active", "groove")])
        self.s.configure("F3.Toolbutton", background="black", foreground="white")
        self.s.map("F3.Toolbutton",\
                   background=[("disabled", "black")],
                   foregrounf=[("active", "white")])
    def destino(self) :
        self.etkURL.place_forget()
        self.btn1.place_forget()
        self.path = askdirectory()
        self.txt2.place(x=15, y=70)
        self.txt2.insert(tk.END, self.path)
        self.btn2.place(x=50, y=105)
        self.btn3.place(x=15, y=20)

    def descarga(self) :
        os.system("touch links.txt")
        b = os.getcwd()
        c = b + "/links.txt"
        d = self.ent1.get()
        with open(c, "w") as file :
            file.write(d)
        os.system("python3 main.py --urls-file " + c)
        sleep(5)
        os.system("rm links.txt")

    def descarga2(self) :
        os.system("touch links.txt")
        b = os.getcwd()
        c = b + "/links.txt"
        d = self.ent1.get()
        e = self.txt2.get(1.0, tk.END)
        with open(c, "w") as file :
            file.write(d)
        os.system("python3 main.py --urls-file " + c + " --download-dir " + e)
        sleep(5)
        os.system("rm links.txt")  

    def url(self) :
        self.txt2.place_forget()
        self.btn2.place_forget()
        self.btn3.place_forget()
        self.etkURL.place(x=15, y=23)
        self.btn1.place(x=96, y=120) 
        
        

        """d = self.txt2.get(1.0, tk.END)
        url = self.ent1.get()"""
        
    
       

if __name__ == "__main__" :
    app = App()
    app.mainloop()



                                    
















