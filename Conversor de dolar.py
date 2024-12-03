import requests
from bs4 import BeautifulSoup, NavigableString

headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (HTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36"}  # campo obtido em network dentro do inspecionar página
link = "https://www.google.com.br/search?q=cota%C3%A7%C3%A3o+dolar"
requisition = requests.get(link, headers=headers)  # formatação padrão para leitura do site sem ter problemas com permissão
print(requisition)  #<Response [200]> = acesso permitido
#  print(requisition.text) me fornece o código fonte do site linkado
site = BeautifulSoup(requisition.text, "html.parser")  # formatação básica para beautifulsoup
# print(site.prettify())  #  ferramenta para fornecer o código de uma maneira mais bonita

titulo = site.find('title')  #usando a função site.find para procurar o título do site
# print(titulo) #me fornece o título do site(O nome que fica na aba)
pesquisa = site.find_all("input")  #pesquisa todos os "input" no site (locais em que o usuário digita algo a ser informado ou desejado
print(pesquisa[2])  # O comando site.find_all('input") me gerou uma lista com todos os inputs encontrados no site. Entretanto, apenas queria o campo de buscar do Google, que era o terceiro input na lista
#outra forma de pesquisar com o coman site.find() é: site.find_all("input", clas_="xxx"), onde pesquisarei dentro de todos os inputs os que tenham a classe indicada por "xxx".


busca = site.find_all("input", class_="gLFyf")
print(busca)

cot_dollar: BeautifulSoup | NavigableString | None = site.find("span", class_="SwHCTb")
print(cot_dollar["data-value"])
valor_dollar = cot_dollar["data-value"]
real = float(input(" quantos reais deseja converter: "))
x = float(valor_dollar)
y = real/x
print(f"{real} reais são {y} dólares")
