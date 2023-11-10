from flask import Blueprint, redirect, render_template,render_template, request, url_for, flash
from sqlalchemy import select
from conexao import db 
from model import Aluno 

bp = Blueprint("Inscricao", __name__)

@bp.route("/alunos/lista")
def lista():
    lista = db.session.scalars(select(Aluno))


    return render_template("alunos/lista.html", lista=lista)

@bp.route("/inscricao", methods=("GET", "POST"))
def add():
    erros = []

    if request.method=="POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        cep = request.form.get("cep")
        senha = request.form.get("senha")
        cidade = request.form.get("cidade")
        estado = request.form.get("estado")
        telefone = request.form.get("telefone")
        funcao = request.form.get("funcao")
        


        # Validações
        if not nome: erros.append("Nome é um campo obrigatório")
        if not email: erros.append("Email é um campo obrigatório")
        if not cep: erros.append("Cep é um campo obrigatório")
        if not senha: erros.append("Senha é um campo obrigatório")
        if not cidade: erros.append("Cidade é um campo obrigatório")
        if not estado: erros.append("Estado é um campo obrigatório")
        if not telefone: erros.append("Telefone é um campo obrigatório")
        if not funcao: erros.append("Função é um campo obrigatório")
        


        if len(erros) == 0:
            # salva usuário no banco de dados
            aluno = Aluno(**{"nome": nome, "email": email, "cep": cep, "senha": senha, "cidade": cidade, "estado": estado, "telefone": telefone, "funcao": funcao,})
            db.session.add(aluno)
            db.session.commit() # persiste no banco 
            
            flash(f"Usuário {nome}, salvo com sucesso!")
            

    return render_template("inscricao.html", erros=erros)