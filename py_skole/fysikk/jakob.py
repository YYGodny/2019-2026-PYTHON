
import tkinter as tk

class LiggApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ligg-veiviser")

        self.label = tk.Label(root, text="Vil du ligge?", font=("Arial", 16))
        self.label.pack(pady=20)

        self.ja_knapp = tk.Button(root, text="Ja", width=10, command=self.ja)
        self.ja_knapp.pack(side="left", padx=20, pady=20)

        self.nei_knapp = tk.Button(root, text="Nei", width=10, command=self.nei)
        self.nei_knapp.pack(side="right", padx=20, pady=20)

        self.steg = 0

    def ja(self):
        if self.steg == 0:
            self.label.config(text="Vil den andre ligge?")
            self.steg = 1
        elif self.steg == 1:
            self.label.config(text="Er alle våkne?")
            self.steg = 2
        elif self.steg == 2:
            self.label.config(text="Er noen fulle eller rusa?")
            self.steg = 3
        elif self.steg == 3:
            self.label.config(text="Endrer noen mening underveis?")
            self.steg = 4
        elif self.steg == 4:
            self.label.config(text="Ikke ligg!", fg="red")
            self.deaktiver()

    def nei(self):
        if self.steg == 0:
            self.vis_resultat("Ikke ligg!")
        elif self.steg == 1:
            self.vis_resultat("Ikke ligg!")
        elif self.steg == 2:
            self.vis_resultat("Ikke ligg!")
        elif self.steg == 3:
            self.label.config(text="Ligg! (Husk kondom!)", fg="green")
            self.deaktiver()
        elif self.steg == 4:
            self.label.config(text="Ligg! (Husk kondom!)", fg="green")
            self.deaktiver()

    def vis_resultat(self, tekst):
        self.label.config(text=tekst, fg="red")
        self.deaktiver()

    def deaktiver(self):
        self.ja_knapp.config(state="disabled")
        self.nei_knapp.config(state="disabled")


# Start appen
root = tk.Tk()
app = LiggApp(root)
root.mainloop()
