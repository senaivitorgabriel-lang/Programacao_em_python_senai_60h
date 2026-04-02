import sqlite3
import tkinter as tk


def salvar():
    conn = sqlite3.connect('agencia.db')
    cursor = conn.cursor()

    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS leads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER,
        email TEXT,
        endereco TEXT,
        trabalho TEXT,
        graduacao TEXT
    )
    ''')

 
    cursor.execute('''
    INSERT INTO leads (nome, idade, email, endereco, trabalho, graduacao)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        entrada_nome.get(),
        entrada_idade.get(),
        entrada_email.get(),
        entrada_endereco.get(),
        entrada_trabalho.get(),
        entrada_graduacao.get()
    ))

    conn.commit()
    conn.close()

    
    entrada_nome.delete(0, tk.END)
    entrada_idade.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_endereco.delete(0, tk.END)
    entrada_trabalho.delete(0, tk.END)
    entrada_graduacao.delete(0, tk.END)


janela = tk.Tk()
janela.title("Cadastro de Leads")
janela.geometry('400x500')


tk.Label(janela, text="Nome").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text="Idade").pack()
entrada_idade = tk.Entry(janela)
entrada_idade.pack()

tk.Label(janela, text="Email").pack()
entrada_email = tk.Entry(janela)
entrada_email.pack()

tk.Label(janela, text="Endereço").pack()
entrada_endereco = tk.Entry(janela)
entrada_endereco.pack()

tk.Label(janela, text="Trabalho").pack()
entrada_trabalho = tk.Entry(janela)
entrada_trabalho.pack()

tk.Label(janela, text="Graduação").pack()
entrada_graduacao = tk.Entry(janela)
entrada_graduacao.pack()


btn = tk.Button(janela, text='Salvar Lead', command=salvar)
btn.pack(pady=10)


janela.mainloop()