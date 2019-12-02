import requests
from bs4 import BeautifulSoup
from PIL import Image
from pytesseract import image_to_string

#pega no nome da empresa
nome = input("Digite o nome da empresa: ")
urlimg = 'https://www.jucesponline.sp.gov.br/'
url = 'https://www.jucesponline.sp.gov.br/ResultadoBusca.aspx?ppe='+str(nome)
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all('img')
#Pega o link do captcha
for row in text:
    if not row['src'].find('CaptchaImage'):
        img = row['src']

captcha = urlimg +str(img)
print(captcha)
#pegar imagem do captcha e passar para texto
response = requests.get(captcha)
response = requests.get(captcha, stream=True)
response.raw.decode_content = True
image = Image.open(response.raw)
text = image_to_string(image)
print(text)
#Executa a rotina para fazer a requisição com o captcha 
cookies = {"cookie" : "ASP.NET_SessionId=4f50nzjl3ybynbmyg0z05crg; _ga=GA1.4.442213336.1575301155; _gid=GA1.4.1567590173.1575301155; _gat_gtag_UA_129106988_4=1"}
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.9 Safari/537.36", "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3", "Content-Type": "application/x-www-form-urlencoded"}
params = {'ctl00$ajaxMaster': 'ctl00$cphContent$ajaxGrid|ctl00$cphContent$gdvResultadoBusca$btEntrar','ctl00$cphContent$frmBuscaSimples$txtPalavraChave:':nome,'ctl00$cphContent$gdvResultadoBusca$CaptchaControl1':text,'__ASYNCPOST': 'true','ctl00$cphContent$gdvResultadoBusca$btEntrar': 'Continuar'}

session = requests.Session()
req = session.post(url = 'https://www.jucesponline.sp.gov.br/ResultadoBusca.aspx?ppe='+str(nome), data = params, cookies = cookies, headers = headers)
soup2 = BeautifulSoup(req.content, 'html.parser')
print(soup2)