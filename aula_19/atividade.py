import tkinter as tk
from tkinter import messagebox

def salvar_dados():
    dados = {
        "Nome": nome.get(),
        "Idade": idade.get(),
        "Email": email.get(),
        "Endereço": endereco.get(),
        "Celular": celular.get(),
        "CEP": cep.get(),
        "Cidade": cidade.get(),
        "Cursos": cursos.get()
    }
    print(dados)


   
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("400x500")


tk.Label(janela, text="Nome").pack()
nome = tk.Entry(janela, width=40)
nome.pack()

tk.Label(janela, text="Idade").pack()
idade = tk.Entry(janela, width=40)
idade.pack()

tk.Label(janela, text="E-mail").pack()
email = tk.Entry(janela, width=40)
email.pack()

tk.Label(janela, text="Endereço").pack()
endereco = tk.Entry(janela, width=40)
endereco.pack()

tk.Label(janela, text="Celular").pack()
celular = tk.Entry(janela, width=40)
celular.pack()

tk.Label(janela, text="CEP").pack()
cep = tk.Entry(janela, width=40)
cep.pack()

tk.Label(janela, text="Cidade").pack()
cidade = tk.Entry(janela, width=40)
cidade.pack()

tk.Label(janela, text="Cursos").pack()
cursos = tk.Entry(janela, width=40)
cursos.pack()


tk.Button(janela, text="Cadastrar", command=salvar_dados).pack(pady=10)


janela.mainloop()

