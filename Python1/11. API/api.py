


# import requests
# import json


# # GET (URL)

# # Sattus kod
#     # Om ok --> konvertera svar till JSON
#     # Om ej ok --> error


# # Get request för att hämta produkterna
# response = requests.get('https://fakestoreapi.com/products')


# if response.status_code == 200: 
#     products = response.json()         # Konvertera till JSON
#     print('All products:', products)   # Visa alla  producter

# else:
#     print(f'Error fetching products. Status code:{response.status_code}')

# products = response.json() 

# def visa_products(): 
#     # 使用 enumerate() 来给每个产品加上序号
#     for index, product in enumerate(products, start=1):
#         print(f"{index}. {product['title']}")   

# def products_detal():
#     val = int(input("Ange produkt-ID du vill se:"))
#     print("Produktnamn:", products[val-1]["title"])
#     print("Pris:", products[val-1]["price"])
#     print("Beskrivning:", products[val-1]["description"])
#     print("Kategori:", products[val-1]["category"])
        


# def add_newproduct():

#     # 创建一个新的产品
#     new_product = {
#         "id": 21,
#         "title": input("Ange Produktnamn:"),
#         "price": input("Ange pris:"),
#         "description": input("Ange produktbeskrivning:"),
#         "category": input("Ange kategori")
#     }
#     products.append(new_product)
#     print("Produkt tilllagd:", products[-1])


# # post  ?
# products = products.post('https')



# def main():
#     while True:
#         print("Meny:")
#         print("1. Visa alla produkter")
#         print("2. Visa produktdetaljer")
#         print("3. Lägg till en ny produkt")
#         print("4. Avluta ")

#         menyval = int(input("Gör ett val 1-4: "))
#         if menyval == 1:
#             visa_products()
#         elif menyval == 2:
#             products_detal()
#         elif menyval == 3:
#             add_newproduct()
#         elif menyval == 4:
#             break
#         else:
#             print("Ogiltigt val, försök igen.")


# if __name__ == "__main__":
#     main()


# 老师的

import requests
import json

# Funktion för att hämta och visa alla produkter
def show_all_products():
    response = requests.get('https://fakestoreapi.com/products')
    if response.status_code == 200:
        products = response.json()
        for product in products:
            print(f"{product['id']}.{product['title']}")

    else:
        print(f"Error fetching products. Status code: {response.status_code}")
        return []

# Funktion för att visa detaljer om en specifik produkt
# {product_id} 是一个变量，表示要插入到字符串中的值，它将被替换为具体的产品 ID
def show_product_details(product_id):
    response = requests.get(f'https://fakestoreapi.com/products/{product_id}')
    if response.status_code == 200:
        product = response.json()
        print(f"Produktnamn: {product['title']}")
        print(f"Pris: {product['price']}")
        print(f"Beskrivning: {product['description']}")
        print(f"Kategori: {product['category']}")

    else:
        print(f"Error fetching products. Status code: {response.status_code}")

# Funktion för att lägga till en ny produkt
def add_product():
    new_product = {
        "title": input("Ange produktnamn: "),
        "price": float(input("Ange pris: ")),
        "description": input("Ange produktbeskrivning: "),
        "category": input("Ange kategori: "),
        "image": "https://fakestoreapi.com/img/placeholder.png"
    }

    # headers={'Content-Type': 'application/json'}:
    # headers 参数用于设置 HTTP 请求头（headers）。
    # Content-Type: application/json 告诉服务器，发送的数据是以 JSON 格式传递的。
    # json.dumps(new_product) 将 Python 的字典（或对象） new_product 转换为 JSON 字符串，因为 POST 请求需要发送 JSON 数据格式。
    response = requests.post("https://fakestoreapi.com/products",
                             headers={'Content-Type': 'application/json'},
                             data=json.dumps(new_product)
                             )

    if response.status_code == 200 or response.status_code == 201:
        product = response.json()
        print('Produkt tillagd:', product)
        # 只显示新加的商品

    else:
        print(f'Error adding product. Status code: {response.status_code}')

# Huvudprogrammet med meny
def main():
    while True:
        print("\nMeny:")
        print("1. Visa alla produkter")
        print("2. Visa produktdetaljer")
        print("3. Lägg till en ny produkt")
        print("4. Avsluta")
        
        choice = input("Välj ett alternativ (1-4): ")
        
        if choice == '1':
            products = show_all_products()
        elif choice == '2':
            product_id = input("Ange produkt-ID du vill se: ")
            show_product_details(product_id)
        elif choice == '3':
            add_product()
        elif choice == '4':
            print("Avslutar...")
            break
        else:
            print("Ogiltigt val, försök igen.")

# Kör huvudprogrammet
if __name__ == '__main__':
    main()













