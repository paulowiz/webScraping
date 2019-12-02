## 📚  Descrição 

WebScraping para pegar infromações de empresas no site da prefeitura de São Paulo

## 🚀 Tecnologias Usadas 

<img src="https://user-images.githubusercontent.com/18649504/66262823-725cd600-e7be-11e9-9cea-ea14305079db.png" width = "100">

## 📌 Estrutura do Projeto 
    |-- main.py
    |-- requiriments.txt
    
main.py -> Arquivo que  faz a rotina principal.
<br>
requiriments.txt -> bibliotecas utilizadas no python 
<br>

## 📢 Como executar

Requisitos:

Python 3.7.4<br>

Instalar todas as depedências do python usando o arquivo requiriments.txt que está no projeto:  

```bash 
pip install  -r requiriments.txt
 ```  
 Executar o main.py no cmd com o comando:

```bash 
python main.py
 ```  
Após isso o robo irá executar as seguintes rotinas pelo backend:

- Pega por input o nome da empresa

- Faz a primeira requisição no link ttps://www.jucesponline.sp.gov.br/ResultadoBusca.aspx?ppe="NomedaEmpresa"

- Percorre o html do resultado acima e retorna o link da imagem do captcha

- Com a biblioteca pytesseract ele pega o texto da imagem e retorna o mesmo

- Faz um request session com as informações do captcha e da empresa para pegar os dados principais sobre a consulta.

- O codigo retorna apenas o html de retorno que obtive do site onde não localizei a tabela referente com os nomes.


- Nõa foi possivel resolver o captcha e fazer a requisição para a pagina que retorna a table. 
## 🔓 Licença 
MIT © [Paulo Mota](https://www.linkedin.com/in/paulo-mota-955218a2/)
