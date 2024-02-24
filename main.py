from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox, Treeview, Scrollbar, Style
from tkinter.messagebox import showinfo
from mesClasses.personne import *
# -------- gestion des evenements
def charger():
    tv.delete(*tv.get_children())
    lst = bdClients.getClients()
    for cl in lst:
        tv.insert("", END, values=(cl.num, cl.nom, cl.sexe, cl.ville))

def init():
    txt1.set("")
    txt2.set("")
    sexe.set("f")
    cbVilles.current(3)

def action01():
    t1 = int(txtNum.get())
    t2 = txtNom.get()
    s = sexe.get()
    vl = cbVilles.get()
    bdClients.addClient(Client(t1, t2, s, vl))
    charger()
    init()
   # showinfo(title="Infos Clients", message=f"Numéro : {t1}, Nom : {t2}, Sexe : {s}, Ville : {vl}")
   #  tv.insert("",END, values=(t1, t2, s, vl))

def action02(event):
    cl = tv.item(tv.selection())["values"]
    txt1.set(cl[0])
    txt2.set(cl[1])
    sexe.set(cl[2])
    p = lstVilles.index(cl[3])
    cbVilles.current(p)

def action03():
    t1 = int(txtNum.get())
    t2 = txtNom.get()
    s = sexe.get()
    vl = cbVilles.get()
    bdClients.updateClient(Client(t1, t2, s, vl))
    charger()
    init()

def action04():
    num = int(txtNum.get())
    bdClients.deleteClient(num)
    charger()
    init()

def action05():
    fichier = filedialog.asksaveasfilename(title="Enregistrer", initialdir="C:\\xxx", filetypes=(("Fichier Text", "*.txt"), ("Fichier Word", "*.doc"),("Tous les fichiers","*.*")))
    if fichier !="":
        bdClients.enregistrer(fichier)


def chargerFile():
    fichier = filedialog.askopenfilename(title="Enregistrer", initialdir="C:\\xxx", filetypes=(("Fichier Text", "*.txt"), ("Fichier Word", "*.doc"), ("Tous les fichiers", "*.*")))
    if fichier !="":
        bdClients.charger(fichier)
    charger()
# --------------------------------showinfo(title="Infos Clients", message=f"*************{cl}**************")

bdClients = Clients()


# form
frm = Tk()
frm.title("Gestion Clients")
frm.geometry("700x600")
frm.config(bg="lightblue")
# groupBox
pl = LabelFrame(frm,text="Infos Clients", font=11, bg="lightblue")
pl.place(x=20,y=40,width=400, height=260 )
#label
l1 = Label(pl, text="Numéro:", font=11, bg="lightblue")
l1.place(x=20,y=20)
l2 = Label(pl, text="Nom:", font=11, bg="lightblue")
l2.place(x=20,y=60)
l3 = Label(pl, text="Sexe:", font=11, bg="lightblue")
l3.place(x=20,y=100)
l4 = Label(pl, text="Ville:", font=11, bg="lightblue")
l4.place(x=20,y=140)

#entry
txt1 = StringVar()
#txt1.set("bonjour")
txtNum = Entry(pl, textvariable=txt1, font=11)
txtNum.place(x=120,y=20)
txt2 = StringVar()
txtNom = Entry(pl, textvariable=txt2, font=11)
txtNom.place(x=120,y=60)
#RadionButton
sexe= StringVar()
sexe.set("f")
r1 = Radiobutton(pl, text="F", value="f", variable=sexe, font=11, bg="lightblue")
r2 = Radiobutton(pl, text="M", value="m", variable=sexe, font=11, bg="lightblue")
r1.place(x=120,y=100)
r2.place(x=180,y=100)
# combobox
lstVilles=["Fes", "Rabat", "Casa", "Agadir"]
cbVilles = Combobox(pl, values=lstVilles,font=11)
cbVilles.current(3)
cbVilles.place(x=120,y=140)
# panel
plB = LabelFrame(frm,text="", font=11, bg="lightblue")
plB.place(x=450,y=50,width=150, height=250 )

#Button
b1 = Button(plB, text="Ajouter",font=11, command=action01)
b1.place(x=20,y=40, width=100)
b2 = Button(plB, text="Modifier",font=11, command=action03)
b2.place(x=20,y=90, width=100)
b3 = Button(plB, text="Supprimer",font=11, command=action04)
b3.place(x=20,y=140, width=100)
b4 = Button(plB, text="Enregistrer",font=11, command=action05)
b4.place(x=20,y=190, width=110)

# TreeView
# style = Style()
# style.configure("xxx", highlightthickness=0, bd=0, font=('Calibri', 13,'bold')) # Modify the font of the body
# style.configure("xxx.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
# style.layout("xxx", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

tv = Treeview(frm, columns=("num", "nom","sexe", "ville"), show="headings")
tv.heading("num", text="Numéro")
tv.heading("nom", text="Nom")
tv.heading("sexe", text="Sexe")
tv.heading("ville", text="Ville")
tv.column("num", width=60, anchor=CENTER)
tv.column("sexe", width=60, anchor=CENTER)
tv.place(x=20,y=340,width=600, height=220)

#SCROLLBar
scrol = Scrollbar(frm, orient=VERTICAL, command=tv.yview)
tv.configure(yscroll=scrol.set)
scrol.place(x=600, y=355 , height=200)
tv.bind("<Double-1>",action02)
chargerFile()
mainloop()
