# Starting environment

Antes de mais nada precisamos criar nosso virtual enviroment,  para isso dentro do terminal, navegamos ateh o diretorio raiz de nosso projeto e colocamos o seguinte comando (cuidado: python3 e pip precisam ter sido previamente instalados):

`python -m venv env`

> Comando usado para criar a ambiente virtual

`. env/bin/activate`

> Comando usado para ativar o ambiente virtual 

`pip install -r requirements.txt`

> Comando usado para installar os pacotes que vamos utilizar em nosso projeto

`python manage.py runserver`

> Comando usado para rodar nossa aplicacao, Agora se entrar http://127.0.0.1:8000 em seu browser, voce deveria ver nossa aplicacao rodando.