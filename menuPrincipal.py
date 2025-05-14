import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style

app = ttk.Window("Cadastrar Aluno")
app.geometry("1000x800")
style = Style(theme="cyborg")

espAltura = 18
espLargura = 10

label = ttk.Label(app, text="Cadastrar Aluno")
label.pack(pady=35)
label.config(font=("Arial", 20, "bold"))

nome = ttk.Frame(app)
nome.pack(pady=espAltura, padx=espLargura, fill="x")
ttk.Label(nome, text="Nome").pack(side=LEFT, padx=5)
ttk.Entry(nome).pack(side=LEFT, fill="x", expand=True, padx=5)

address = ttk.Frame(app)
address.pack(pady=espAltura, padx=espLargura, fill="x")
ttk.Label(address, text="Endereço").pack(side=LEFT, padx=5)
ttk.Entry(address).pack(side=LEFT, fill="x", expand=True, padx=5)

linha = ttk.Frame(app)
linha.pack(pady=espAltura, padx=espLargura, fill="x")

# Cidade
ttk.Label(linha, text="Cidade").pack(side=LEFT, padx=5)
ttk.Entry(linha, width=20).pack(side=LEFT, padx=5)

# UF
ttk.Label(linha, text="UF").pack(side=LEFT, padx=5)
ttk.Entry(linha, width=5).pack(side=LEFT, padx=5)

# CEP
ttk.Label(linha, text="CEP").pack(side=LEFT, padx=5)
ttk.Entry(linha, width=10).pack(side=LEFT, padx=5)

telefone = ttk.Frame(app)
telefone.pack(pady=espAltura, padx=espLargura, fill="x")

# Residencial
ttk.Label(telefone, text="Residencial").pack(side=LEFT, padx=5)
ttk.Entry(telefone, width=20).pack(side=LEFT, padx=5)

# Celular
ttk.Label(telefone, text="Celular").pack(side=LEFT, padx=5)
ttk.Entry(telefone, width=5).pack(side=LEFT, padx=5)

email = ttk.Frame(app)
email.pack(pady=espAltura, padx=espLargura, fill="x")
ttk.Label(email, text="Email").pack(side=LEFT, padx=5)
ttk.Entry(email).pack(side=LEFT, fill="x", expand=True, padx=5)

botao = ttk.Frame(app)
botao.pack(pady=30, padx=10, fill="x")
ttk.Button(botao, text="Cadastrar", bootstyle=SUCCESS).pack(side=LEFT, padx=15)
ttk.Button(botao, text="Cancelar", bootstyle=DANGER).pack(side=LEFT, padx=15)


# Definir colunas
columns = ("curso", "professor", "data_inicio", "data_termino", "nota_final", "frequencia")

# Criar Treeview
tree = ttk.Treeview(app, columns=columns, show="headings", bootstyle="info")

# Definir cabeçalhos
tree.heading("curso", text="Nome do Curso")
tree.heading("professor", text="Professor")
tree.heading("data_inicio", text="Data Início")
tree.heading("data_termino", text="Data Término")
tree.heading("nota_final", text="Nota Final")
tree.heading("frequencia", text="Frequência")

tree.pack(fill="both", expand=True, padx=10, pady=10)
app.mainloop()