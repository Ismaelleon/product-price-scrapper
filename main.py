from bs4 import BeautifulSoup
import requests, json

websites_data = {}

with open('data.json') as json_file:
	websites_data = json.load(json_file)


def main ():
	product = input('Product to search: ')

	for website, data in websites_data.items():
		response = requests.get(data['url'].format(product.lower()))
			
		soup = BeautifulSoup(response.text, 'html.parser')
		
		product_name = soup.find(class_=data['name_class'])
		product_price = soup.find(class_=data['price_class'])

		if product_name != None and product_price != None:
			product_name = product_name.get_text().replace('\n', '')
			product_price = product_price.get_text()
			

			print('{}: {}, ${}'.format(website, product_name, product_price))
		else:
			print('{}: Product not found.'.format(website))


if __name__ == '__main__':
	main()
