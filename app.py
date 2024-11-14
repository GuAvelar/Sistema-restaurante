from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_praca.receber_avaliacao('Gustavo', 5)
restaurante_praca.receber_avaliacao('Cloves', 4)

restaurante_mexicano = Restaurante('mexican food', 'Mexicana')
restaurante_mexicano.receber_avaliacao('Raul', 4)
restaurante_mexicano.receber_avaliacao('Maria', 4)
restaurante_mexicano.alternar_estado()


restaurante_Japones = Restaurante('Japa', 'Japonesa')
restaurante_Japones.receber_avaliacao('Natan', 2)
restaurante_Japones.receber_avaliacao('Paulo', 4)

bebida_suco = Bebida ('Suco de laranja', 15 ,'Grande')
bebida_suco.aplicar_desconto()
prato_parmegiana = Prato ('Parmegiana', 60, 'Uma parmegiana deliciosa, com filé empanado, coberto de molho de tomate caseiro, queijo derretido e temperos frescos.')
prato_parmegiana.aplicar_desconto()

restaurante_praca.adiconar_no_cardapio(bebida_suco)
restaurante_praca.adiconar_no_cardapio(prato_parmegiana)


def main():
    Restaurante.listar_restaurantes()
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':  
    main()