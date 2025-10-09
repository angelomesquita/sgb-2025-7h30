# SGB - Sistema Gerenciador de Biblioteca

Projeto em desenvolvimento com os alunos do 3º ano do Técnico em Desenvolvimento de Sistemas - EPTEC Paraná

## 🎯  Objetivo
Desenvolver um sistema de gerenciamento para biblioteca escolar utilizando os conceitos da disciplina de **Programação no Desenvolvimento de Sistemas**

## 🚀 Tecnologias utilizadas
- Python 3.8

## 📝 Conceitos aplicados
- funções e métodos
- listagens
- orientação a objetos

## ✅ Requisitos implementados
- [x] **RF001 - Cadastro de Funcionarios:** Permitir o registro de funcionários responsáveis pela biblioteca com dados como nome, cpf, cargo, login e senha.
- [x] **RF002 - Cadastro de Usuários:** Possibilitar o cadastro de usuários da biblioteca com nome, CPF, contato e categoria (exemplo: estudante, professor, visitante).
- [x] **RF003 - Cadastro de Livros:** Registrar os livros no sistema com informações como título, autor, editora, ano de publicação, ISBN e quantidade disponível.
- [x] **RF004 - Consulta e Pesquisa de Livros:** Permitir busca por livros com filtros como título, autor e disponibilidade.
- [x] **RF005 - Empréstimo de Livros:** Registrar o empréstimo de um livro, vinculando-o a um usuário e a uma data de retirada e devolução prevista.
- [x] **RF006 - Devolução de Livros:** Registrar a devolução de um livro, atualizando seu status no sistema e calculando possíveis multas.

## 📁 Estrutura do projeto
```bash
sgb-2025-7h30/
├── controller/
│ └── employee_controller.py
├── model/
│ └── employee.py
├── view/
│ └── employee_view.py
├── main.py
```
## 📝 Como executar
```bash
python main.py
```
