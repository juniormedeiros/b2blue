# TMdb Pesquisa de Séries de TV

## Introdução

O TMdb Séries de TV foi desenvolvido utilizando o módulo **Django** que torna mais fácil para os desenvolvedores codificarem aplicações Web.

Está página foi criada com o intuito de pesquisar Séries de TV.

Este documento descreve como executar e utilizar a aplicação.


## Como Instalar

Para executar o projeto primeiro é necessário instalar o [Python](https://www.python.org/downloads/).


## Pacotes Utilizados

Na construção da aplicação foi necessário instalar alguns pacotes e utilitários.
Através da ferramenta **pip** presente junto ao Python é possível instalar os pacotes.

Na pasta do projeto execute o seguinte comando: 

``` python
    pip install requirements.txt
```

Após executar o comando acima será instalado todos as dependências do projeto.

No arquivo **requirements.txt** é possível verificar todas as dependências do projeto.


Abaixo segue lista dos principais pacotes utilizados:

| Pacote | Versão | Descrição |
| :--- | :--- | :--- |
| `Django` | `^3.2` | Django Framework |
| `tmdbsimple` | `^2.8.0` | Utilitário para consumir API TMdb |

**OBS:** Na pasta .b2blue existe um ambiente virtual python com todas as dependências instaladas,
caso prefira basta ativar o ambiente virtual com o comando abaixo:

``` shell
  {path}\onidata-api\.onidata\Scripts>activate.bat
```

{path} = Caminho da aplicação até chegar ao arquivo activate.bat

## Criando base de dados

Nesse projeto não utilizamos base de dados, todos os dados são provenientes da API do TMdb.


## Executando o projeto

Após instalado todas as dependência basta execute o comando abaixo para
executar o projeto.

``` python
    python manage.py runserver
```

Em seguida acesse o [link](http://127.0.0.1:8000/) para verificar a página de pesquisa.

## Como utilizar

Na página inicial aparecerá os top 20 títulos mais bem avaliados dentro do TMdb.

É possível ainda utilizar três típos de pesquisa 

- Nome da Série de TV
- Ano em que o primeiro episódio foi ao ar.
- Popularidade do título a partir do valor 1.0 (Obrigatório informar as casas decimais).

Para pesquisar basta digitar o nome, ano ou a quantidade da popularidade e pressionar o botão **Enter** do teclado.

Após pesquisar o título é possível ver outras informações, clicando no botão **detalhes** sobre a 
imagem do título. 

Ainda dentro da página de detalhes é possível realizar a votação do título entre 0,5 até 10 estrelas,
basta escolher a sua nota e clicar no botão **VOTAR** .


![Tela Inicial](https://github.com/juniormedeiros/django/blob/dev/Picture1.JPG)

![Tela de Pesquisa](https://github.com/juniormedeiros/django/blob/dev/Picture2.JPG)

**Created By Junior Medeiros 27 April 2021**
