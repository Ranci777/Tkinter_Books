import tkinter as tk
from tkinter import messagebox, simpledialog
import webbrowser


class GerenciadorLinks:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Links de Livros")
        self.root.geometry("500x500")

        # Lista de livros com links
        self.livros = []

        # Interface
        self.label = tk.Label(root, text="Gerenciar Links de Livros", font=("Arial", 16))
        self.label.pack(pady=10)

        self.listbox = tk.Listbox(root, width=60, height=15)
        self.listbox.pack(pady=10)

        self.btn_adicionar = tk.Button(root, text="Adicionar Livro com Link", command=self.adicionar_livro)
        self.btn_adicionar.pack(pady=5)

        self.btn_visualizar = tk.Button(root, text="Abrir Link do Livro", command=self.abrir_link)
        self.btn_visualizar.pack(pady=5)

        self.btn_remover = tk.Button(root, text="Remover Livro", command=self.remover_livro)
        self.btn_remover.pack(pady=5)

    def adicionar_livro(self):
        # Solicitar dados do livro
        titulo = simpledialog.askstring("Adicionar Livro", "Digite o título do livro:")
        autor = simpledialog.askstring("Adicionar Livro", "Digite o autor do livro:")
        link_compra = simpledialog.askstring("Adicionar Livro", "Digite o link para comprar o livro:")

        if titulo and autor and link_compra:
            self.livros.append({"Título": titulo, "Autor": autor, "Link": link_compra})
            self.atualizar_lista()
            messagebox.showinfo("Sucesso", "Livro com link adicionado com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Todos os campos são obrigatórios!")

    def abrir_link(self):
        selecionado = self.listbox.curselection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um livro para abrir o link!")
            return

        indice = selecionado[0]
        link = self.livros[indice]["Link"]

        try:
            webbrowser.open(link)
            messagebox.showinfo("Sucesso", f"Abrindo link: {link}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir o link: {e}")

    def remover_livro(self):
        selecionado = self.listbox.curselection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um livro para remover!")
            return

        indice = selecionado[0]
        del self.livros[indice]
        self.atualizar_lista()
        messagebox.showinfo("Sucesso", "Livro removido com sucesso!")

    def atualizar_lista(self):
        self.listbox.delete(0, tk.END)
        for livro in self.livros:
            self.listbox.insert(tk.END, f"{livro['Título']} - {livro['Autor']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorLinks(root)
    root.mainloop()
