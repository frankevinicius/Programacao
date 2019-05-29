class Produto:

    def __init__(self,cod_produto,nome,preco):
        self.cod_produto = cod_produto
        self.nome = nome
        self.preco = preco

class Item:

    def __init__(self,produto,qtd):
        self.produto = produto
        self.qtd = qtd

class Carrinho:

    def __init__(self, data, hora):
        self.data = data
        self.hora = hora
        self.items = []

    def adicionar_item(self, item):
        self.items.append(item)

    def calcular_valor_total(self):
        valor = 0
        for item in self.items:
            valor += (item.produto.preco * item.qtd) 

        return valor

if __name__ == "__main__":

    biscoito = Produto(1,"Biscoito", 1.25)
    achocolatado = Produto(2,"Achocolatado", 4.00)
    batata = Produto(3, "Batata", 1.98)
    cenoura = Produto(4, 'Cenoura', 1.60)

    item1 = Item(biscoito, 2)
    item2 = Item(achocolatado, 1)
    item3 = Item(batata, 4)
    item4 = Item(cenoura, 6)

    carrinho = Carrinho("24/5/2028", "15:06:43")
    carrinho.adicionar_item(item1)
    carrinho.adicionar_item(item2)
    carrinho.adicionar_item(item3)
    carrinho.adicionar_item(item4)
    print(carrinho.calcular_valor_total())