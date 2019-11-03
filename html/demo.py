from lxml import html
import requests


page = requests.get('http://coveme.cn/dyfilm-hb-hbb-elecrical-grade-film')
# page = requests.get('http://coveme.cn/dyfilm-hb-hbb-elecrical-grade-films')
tree = html.fromstring(page.content)
#This will create a list of buyers:
# buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# #This will create a list of prices
# prices = tree.xpath('//span[@class="item-price"]/text()')


titlenme = tree.xpath('//h1[@class="titleH2"]/text()')
#This will create a list of prices
# prices = tree.xpath('//span[@class="item-price"]/text()')



print(titlenme)