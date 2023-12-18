<h1 align="center">Deploy FastAPI</h1>

<p align="center">Este é o projeto que consiste em uma API que contem um metodo POST que recebe os parametros do iris dataset, essa API retorna a predição através de um modelo de RandomForest</p>

### OS ARQUIVOS :file_folder:

* app
    - [IrisData.py](https://github.com/pedrocarvalho-git/deploy_modelo_fastapi/blob/main/app/IrisData.py) -> _Arquivo que recebe os valores inputados no metodo POST da API_
    - [main.py](https://github.com/pedrocarvalho-git/deploy_modelo_fastapi/blob/main/app/main.py) -> _Onde a mágica acontece, onde a API é criada, o metodo POST é definido e onde temos a predição do modelo_
    - randomforest.pkl -> _Pickle File que contem o treino do nosso modelo_
* notebook
    - [consumo_api.ipynb](https://github.com/pedrocarvalho-git/deploy_modelo_fastapi/blob/main/notebook/consumo_api.ipynb) -> _Notebook que utilizaremos para consumir a API_
* src
    - [IrisTraining.py](https://github.com/pedrocarvalho-git/deploy_modelo_fastapi/blob/main/src/IrisTraining.py) -> _Onde o nosso modelo foi treinado e a partir desse arquivo obtivemos o randomforest.pkl_
    - [iris.csv](https://github.com/pedrocarvalho-git/deploy_modelo_fastapi/blob/main/src/iris.csv) -> _A nossa fonte de dados para treinarmos o nosso modelo_
* [Dockerfile](https://github.com/pedrocarvalho-git/deploy_modelo_fastapi/blob/main/Dockerfile) -> _O Dockerfile que irá criar a nossa imagem docker da nossa API_
* [requirements.txt](https://github.com/pedrocarvalho-git/deploy_modelo_fastapi/blob/main/requirements.txt) -> _A lista de pacotes que intalaremos na nossa imagem Docker_

### O MODELO :chart_with_upwards_trend:

O modelo é um modelo de classificação que da a predição de qual tipo de Iris temos de acordo com o tamanho e comprimento da petala e da sepala da flor, o modelo utilizado foi o [RandomForest](https://towardsdatascience.com/understanding-random-forest-58381e0602d2) que foi treinado no arquivo [IrisTraining.py](https://github.com/pedrocarvalho-git/deploy_modelo_fastapi/blob/main/src/IrisTraining.py) e consumo no arquivo [main.py](https://github.com/pedrocarvalho-git/deploy_modelo_fastapi/blob/main/app/main.py) atráves do Pickle File 'randomforest.pkl', a predição é o output do método POST do endpoint '/predict'

### A API :computer: 

A API foi feita através do framework [Fast API](https://fastapi.tiangolo.com/), a API aceita requisições HTTP para o ip 35.175.141.255, a API apenas tem um método POST na porta 80 para o endpoint '/predict', então nossa url final é 'http://35.175.141.255:80/predict', esse metodo post recebe um json no seu body, esse json deve conter as seguintes chaves: 'sepal_length', 'sepal_width', 'petal_length', 'petal_width', todas recebendo seus devidos valores, esses valores são extraidos através do BaseModel no arquivo [IrisData.py](https://github.com/pedrocarvalho-git/deploy_modelo_fastapi/blob/main/app/IrisData.py). A parte de como passar os valores no Body será mostrado melhor quando fizermos o teste de chamar a API através do notebook.


### O DEPLOY :whale:

O Deploy deste desafio foi feito pelo [Docker](https://www.docker.com) atráves de uma instancia [EC2](https://aws.amazon.com/pt/ec2/) da AWS, a imagem escolhida do Dockerfile é baseada na imagem do [Python3:9](https://hub.docker.com/_/python), fazemos a copia dos arquivos para o container e depois instalamos as dependencias do nosso 'main.py', após isso executamos a nossa API e abrimos ela para receber requisições através do [Uvicorn](https://www.uvicorn.org/), para assim ativarmos o nosso servidor web.

* Para iniciar esse esse Dockerfile em qualquer instancia você só precisa seguir esses passos:

    1. Garantir esses pontos de rede na sua instancia.
        
        ![Inbound Rules](https://i.imgur.com/YUisWqA.png)

    2. Garantir que a sua instancia contem o git e o docker instalados.

    3. Rodar os comandos abaixo 
        ```
        git clone https://github.com/pedrocarvalho-git/deploy_modelo_fastapi.git

        cd deploy_modelo_fastapi

        docker build . -t mlapi

        docker run -t -i -p 80:80 mlapi:latest
        ```
Para você fazer requisições à sua API você só ira precisar passar o IP ou o DNS da sua instancia com a porta 80 e o endpoint '/predict', para esse exemplo iremos utilizar a url: 'http://35.175.141.255:80/predict' ou 'http://ec2-35-175-141-255.compute-1.amazonaws.com:80/predict'

### VERIFICANDO A FUNCIONALIDADE DA API :heavy_check_mark:

Como foi dito acima a API aceita requisições HTTP, então a partir disso podemos fazer a nossa requisição. Iremos seguir o notebook [consumo_api.ipynb](https://github.com/pedrocarvalho-git/deploy_modelo_fastapi/blob/main/notebook/consumo_api.ipynb) que está na pasta notebook/, nele podemos mudar os valores referentes a petalas e sepalas, para ver qual seria o tipo de Iris para os valores que passamos.
