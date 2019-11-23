# Projeto Reconhecimento Facial

### Projeto de Reconhecimento Facial da disciplina de Processamento de Imagem 6º Semestre UNIP - Campus Araçatuba.
Principais Tecnologias Utilizadas:
* Python 3.7.5
* TensorFlow 2.0.0
* OpenCV 4.1.1
* Numpy 1.17.3
* Psycopg2 2.8.4
* Virtualenv 16.7.7
* Tkinter
* PostgreSQL 12
* ElephantSQL

Algumas recomendações antes de rodar o projeto:
* Rode o comando `pip install virtualenv` na sua instalação padrão do Python
* Navegue até o diretório que deseja criar o ambiente virtual;
*  Crie o ambiente virtual, para fazer isso use o comando: `virtualenv nome_do_ambiente_virtual`
* Navegue até a pasta Scripts do ambiente virtual e execute o arquivo *activate.bat*, caso esteja no cmd rode apenas *activate*, isso irá ativar o ambiente virtual
* Navegue até o diretório que se encontra os arquivos do projeto
* Instale as dependências necessárias para o projeto rodando, `pip install -r requirements.txt`

### Rede Neural:
No módulo `intelligence.py`, temos uma rede neural de convolução que diminui as imagens armazenadas na pasta users e suas respectivas sub pastas e aprende com as mesmas. A camada de entrada e de convolução: `Conv2D()` da rede neural recebe como entrada uma matriz 3x3 e tem 128 neurônios, seguida de uma função de ativação `relu` e por fim uma camada de `MaxPooling2D()`, também no formato 3x3. As camadas intermediárias seguem o mesmo modelo, exceto a camada de saída, nela temos uma função `Flatten()` que transforma a entrada em uma matriz 1xn, por fim temos a camada final com a quantidade de saídas e uma função de ativação `sigmoid`.

### Banco de Dados:
No módulo `connector.py` dentro da pasta *db_interaction*, contém os métodos e variáveis necessárias para realizar a conexão com o banco de dados tanto uma instância local quanto na nuvem utilizando o serviço ElephantSQL, basta alterar os valores nesse módulo.

### Interface Gráfica:
Os módulos `aps.py`, `cadastro.py` e `autentica.py` são interfaces gráficas que foram feitas utilizando o Tkinter. O módulo `aps.py` é o menu principal da aplicação, e contém as chamadas para os outros módulos. Em `cadastro.py` temos a tela responsável por fazer o cadastro do usuário, nela podemos colocar o nome, o nível de privilégio e também tirar as fotos, que a rede neural utilizará posteriormente para aprender. E por fim temos módulo `autentica.py`, onde o usuário poderá submeter uma foto para análise na rede neural e a mesma dirá a qual usuário pertence essa foto.

| Integrantes | Github | Papel |
|--|--|--|
| Gustavo Alexandre Moimaz Costa | [https://github.com/gustavoamc](https://github.com/gustavoamc) | Banco de Dados |
| Henler Mendes Pio Soares |  | Documentação da APS |
| José Roberto Adolfo Júnior | [https://github.com/joseadolfodesigner](https://github.com/joseadolfodesigner) | Interface Gráfica |
| Pedro Henrique Correa Mota da Silva | [https://github.com/pedrohcms](https://github.com/pedrohcms) | Rede Neural |