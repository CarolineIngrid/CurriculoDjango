<img src="https://rollingstone.uol.com.br/media/uploads/miranda-cosgrove-meme-drake-and-josh-foto-reproducao-nickelodeon.jpg">

 # Currículo Django
 ## Sobre o projeto!

Projeto desenvolvido com a intenção de criar do zero uma aplicação Django com templates, que utilize banco de dados ao final no footer para guardar as mensagens de contato;

# Como rodar
Descrevo isso me baseando no sistema que uso, Linux
> Tenha em sua máquina python e virtualev
- pip install python
- pip install virtualenv

> Crie um ambiente virtual(não queremos que dependências sejam instaladas em sua máquina, vá por mim)

- virtualenv .venv

> Ative o virtualenv

- source .venv/bin/activated


> Utilize pip, para baixar essas dependencias do requierements.txt (com o ambiente virtual ativo)

- pip install -r requirements.txt

E então:
- ./manage.py runserver

## Decisões e funcionalidades

- Dados principais no main;
- Forms com banco de dados;
- Footer;
- Comecei com as configurações do Django;
- Depois front-end, usando html e css, dentro de um template 🔫
- Olhei alguns projetos no behance para me inspirar.

# Visualizar banco de dados

Com o ambiente virtual ativo vá no terminal e use os seguintes comandos:

- python manage.py shell
- from principal.models import Contato
- contato = Contato.objects.all()
- print(contato)

# Future Code

- Melhorar front-end