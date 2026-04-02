import sqlite3


doc = sqlite3.connect('banco.db')
cs = doc.cursor()

cs.execute('''
                CREATE TABLE IF NOT EXISTS dados(

            nome TEXT,
           idade INTEGER,
           email TEXT
           

            )''')

nome = input('nome: ')
idade = input('idade: ')
email = input('E-mail: ')

cs.execute('INSERT INTO dados VALUE(?,?,?)', (nome, idade, email))

doc.commit()

