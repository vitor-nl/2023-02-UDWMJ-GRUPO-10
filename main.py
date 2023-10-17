from client import Client
from category import Category
from product import Product
from order import Order
from orderitem import Orderitem
from socialnetwork import Socialnetwork
from client_socialnetwork import Client_socialnetwork

#Cliente
print("-----------------------------------------")
cliente = Client("Francisco", "Silva", "Rua Nilo Peçanha", "(51) 99999999", "franciscosilva1990@gmail.com", "M")
print(f"{cliente.first_name} {cliente.last_name}, se cadastrou na loja.")

cliente2 = Client("Maria", "Ribeiro", "Rua Maranhao", "(51) 99999999", "Mariaribeiro0@gmail.com", "F")
print(f"\n{cliente2.first_name} {cliente2.last_name}, se cadastrou na loja.")
print("-----------------------------------------")

#Categorias dos produtos
eletronico = Category("0001", "Eletronicos", "Categoria de Eletronicos")
print(f"Categoria {eletronico.name} foi cadastrada!\n")

moveis = Category("0002", "Moveis", "Categoria de Moveis")
print(f"Categoria {moveis.name} foi cadastrada!")
print("-----------------------------------------")

#Produtos
celular = Product("Celular", "Celular Eletronico, Muito rapido!", "01/01/1960",1, eletronico)  #1 = Ativo, #2 Inativo
print(f"Produto {celular.name} foi cadastrado!\n")

mesa = Product("Mesa", "Mesa de Madeira, Excelente estado!", "01/05/1930",1, moveis)  #1 = Ativo, #2 Inativo
print(f"Produto {mesa.name} foi cadastrado!")
print("-----------------------------------------")

#Ordem de compra
cliente_compra = Order(1, cliente)  #1 = Ativo, #2 Inativo
print(f"Cliente: {cliente_compra.client.first_name}, realizou uma ordem de compra de um produto produto no valor de {cliente_compra.total_price}\n")
cliente_compra2 = Order(1, cliente2)  #1 = Ativo, #2 Inativo
print(f"Cliente: {cliente_compra2.client.first_name}, realizou uma ordem de compra de um produto produto no valor de {cliente_compra.total_price}")
print("-----------------------------------------")


#Comprando item
cliente_comprando = Orderitem(1, 1400, cliente_compra, celular)
cliente_comprando2 = Orderitem(2, 300, cliente_compra2, mesa)
print(f"{cliente.first_name} esta comprando o produto: {cliente_comprando.product.name}\n")
print(f"{cliente2.first_name} esta comprando o produto: {cliente_comprando2.product.name}")
print("-----------------------------------------")

# Adicione o valor da compra ao cliente e exiba individualmente
cliente_compra.add_total_price(cliente_comprando)
cliente_compra2.add_total_price(cliente_comprando2)

print(f"O valor total da compra do cliente {cliente.first_name} custou: R${cliente_compra.total_price}")
print(f"O valor total da compra do cliente {cliente2.first_name} custou: R${cliente_compra2.total_price}")
print("-----------------------------------------")


instagram = Socialnetwork("instagram", "instagram é uma rede social incrivel!.")

cliente_no_face = Client_socialnetwork(cliente, instagram, "1234cliente")