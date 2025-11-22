# Projeto Agenda digital

Uma agenda digital simples construída com Flask para criar, listar, editar e excluir compromissos. Este repositório contém a aplicação e os templates necessários para rodar o sistema localmente.

## Público-Alvo
Qualquer pessoa que precise de uma ferramenta simples para organizar sua rotina diária, especialmente:
- Estudantes
- Pessoas com muitos compromissos
- Usuários que desejam uma solução mínima e eficiente

## Funcionalidades

- Criar compromissos
- Listar compromissos
- Editar compromissos
- Excluir compromissos
- Marcar como concluído
- Desfazer conclusão

## Tecnologias Utilizadas

- Python 3
- Flask
- Jinja2 (templates)
- HTML + CSS
- Estrutura MVC

## Instalação

1. Clonar o repositório (ou abrir a pasta do projeto):

```sh
git clone https://github.com/FranbryloB/Projeto-Agenda
cd Projeto-Agenda
```

2. Criar e ativar um ambiente virtual (Windows PowerShell):

```sh
python -m venv env
.\env\scripts\activate
```

3. Instalar dependências

```sh
pip install -r requirements.txt
```
## Executando a aplicação

```sh
python app.py ou flask run --debug
```

Abra o navegador em http://localhost:5000 para ver a aplicação em execução.

## Reflexão Crítica

1. Sobre o problema

A desorganização de compromissos é um problema comum no cotidiano, especialmente entre estudantes que lidam com diferentes atividades, prazos e tarefas. Uma agenda digital centraliza tudo em um só lugar e evita esquecimentos.

2. Por que um sistema web?

- Pode ser acessado em qualquer computador com navegador.
- Não requer instalação complexa.
- Layout simples e direto facilita o uso.

Outras soluções possíveis:

- Agenda física
- Apps de celular
- Planilhas

Mas a versão web é mais acessível e multiplataforma.

3. Limites da solução

- Os dados ficam apenas na memória.
- Usuários sem acesso constante à internet podem ter dificuldade.
- Não possui autenticação, então não há separação por usuário.
- Acessibilidade visual ainda é limitada.

4. Aprendizados

Durante o desenvolvimento, aprendemos:

- Como funciona a estrutura MVC no Flask
- Uso de rotas, métodos GET/POST e formulários
- Herança de templates com Jinja2
- Organização do código em partes reutilizáveis
- Importância de pensar em quem realmente usa o sistema
- Como uma solução simples já pode ajudar no cotidiano

## Integrantes do Grupo

- Emanoelly Francinny Brito Tavares
- Isabele Fernanda da Silva Albano
- Lívia Tainá de Medeiros Oliveira
- Tamíris dos Santos Medeiros
