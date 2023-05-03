from classe import AssinaturaTv
tv = AssinaturaTv()
print(tv)
print('Canais Disponíveis')
print(tv.canaisDisponiveis)
print('---')
print('Canal Ativo')
print(tv.canalAtivo)
print('---')
tv.canalAtivo = 15
print(tv.canalAtivo)
print("---")
tv.canalAtivo = 25
print("Canal ativo:")
print(tv.canalAtivo)
print("---")