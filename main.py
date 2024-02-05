import tkinter as tk
from tkinter import messagebox
import mysql.connector

class GestionStock:
    def __init__(self, root):
        self.root = root
        self.root.title("StockControl - Gestionnaire de Stockage")
        self.root.geometry("900x600")

        # Connexion à la base de données MySQL
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="F1m13I12l5*",
            database="store"
        )
        self.cursor = self.conn.cursor()

        # Liste des produits
        self.listbox_produits = tk.Listbox(root, selectmode=tk.SINGLE, height=15, width=80)
        self.listbox_produits.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.listbox_produits.bind('<<ListboxSelect>>', self.selection_produit)

        # Interface utilisateur
        self.label_produit = tk.Label(root, text="Produit:")
        self.label_produit.grid(row=1, column=0, padx=10, pady=5)
        self.entry_produit = tk.Entry(root)
        self.entry_produit.grid(row=1, column=1, padx=10, pady=5)

        self.label_description = tk.Label(root, text="Description:")
        self.label_description.grid(row=2, column=0, padx=10, pady=5)
        self.entry_description = tk.Entry(root)
        self.entry_description.grid(row=2, column=1, padx=10, pady=5)

        self.label_price = tk.Label(root, text="Prix:")
        self.label_price.grid(row=3, column=0, padx=10, pady=5)
        self.entry_price = tk.Entry(root)
        self.entry_price.grid(row=3, column=1, padx=10, pady=5)

        self.label_quantity = tk.Label(root, text="Quantité:")
        self.label_quantity.grid(row=4, column=0, padx=10, pady=5)
        self.entry_quantity = tk.Entry(root)
        self.entry_quantity.grid(row=4, column=1, padx=10, pady=5)

        self.label_category = tk.Label(root, text="Catégorie:")
        self.label_category.grid(row=5, column=0, padx=10, pady=5)
        self.entry_category = tk.Entry(root)
        self.entry_category.grid(row=5, column=1, padx=10, pady=5)

        self.button_ajouter = tk.Button(root, text="Ajouter", command=self.ajouter_produit)
        self.button_ajouter.grid(row=6, column=0, columnspan=2, pady=10)

        self.button_supprimer = tk.Button(root, text="Supprimer", command=self.supprimer_produit, state=tk.DISABLED)
        self.button_supprimer.grid(row=7, column=0, columnspan=2, pady=10)

        # Remplir la liste des produits
        self.afficher_produits()

    def afficher_produits(self):
        self.listbox_produits.delete(0, tk.END)
        self.cursor.execute('SELECT name FROM product')
        produits = self.cursor.fetchall()
        for produit in produits:
            self.listbox_produits.insert(tk.END, produit[0])

    def selection_produit(self, event):
        selected_index = self.listbox_produits.curselection()
        if selected_index:
            selected_produit = self.listbox_produits.get(selected_index)
            self.remplir_champs_produit(selected_produit)
            self.button_supprimer["state"] = tk.NORMAL
        else:
            self.button_supprimer["state"] = tk.DISABLED

    def remplir_champs_produit(self, produit):
        self.cursor.execute('SELECT * FROM product WHERE name = %s', (produit,))
        produit_info = self.cursor.fetchone()
        self.entry_produit.delete(0, tk.END)
        self.entry_produit.insert(0, produit_info[1])
        self.entry_description.delete(0, tk.END)
        self.entry_description.insert(0, produit_info[2])
        self.entry_price.delete(0, tk.END)
        self.entry_price.insert(0, produit_info[3])
        self.entry_quantity.delete(0, tk.END)
        self.entry_quantity.insert(0, produit_info[4])
        self.entry_category.delete(0, tk.END)
        self.entry_category.insert(0, produit_info[5])

    def ajouter_produit(self):
        name = self.entry_produit.get()
        description = self.entry_description.get()
        price = self.entry_price.get()
        quantity = self.entry_quantity.get()
        category = self.entry_category.get()

        if name and description and price and quantity and category:
            try:
                price = int(price)
                quantity = int(quantity)
                # Vérifier si la catégorie existe, sinon l'ajouter
                self.cursor.execute('SELECT id FROM category WHERE name = %s', (category,))
                category_id = self.cursor.fetchone()
                if not category_id:
                    self.cursor.execute('INSERT INTO category (name) VALUES (%s)', (category,))
                    self.conn.commit()
                    self.cursor.execute('SELECT id FROM category WHERE name = %s', (category,))
                    category_id = self.cursor.fetchone()
                else:
                    category_id = category_id[0]

                self.cursor.execute('INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)',
                                    (name, description, price, quantity, category_id))
                self.conn.commit()
                messagebox.showinfo("Succès", "Produit ajouté avec succès.")
                self.afficher_produits()
            except (ValueError, mysql.connector.Error) as e:
                messagebox.showerror("Erreur", f"Erreur lors de l'ajout du produit : {str(e)}")
        else:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

    def supprimer_produit(self):
        produit = self.listbox_produits.get(self.listbox_produits.curselection())
        if produit:
            confirmation = messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer ce produit?")
            if confirmation:
                self.cursor.execute('DELETE FROM product WHERE name = %s', (produit,))
                self.conn.commit()
                messagebox.showinfo("Succès", "Produit supprimé avec succès.")
                self.afficher_produits()
                self.reset_champs_produit()
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un produit à supprimer.")

    def reset_champs_produit(self):
        self.entry_produit.delete(0, tk.END)
        self.entry_description.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)
        self.entry_category.delete(0, tk.END)
        self.button_supprimer["state"] = tk.DISABLED

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionStock(root)
    root.mainloop()
