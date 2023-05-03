from classe import Produtos

pc = Produtos("Notebook acer", 2500)
print(f"O Preço de custo do {pc.descricao} é R$ {pc.precoCusto}")

pc.precoVenda=float(input("Insira um valor para o preço de venda: "))

print(pc.precoVenda)