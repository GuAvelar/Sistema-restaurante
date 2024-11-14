from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_praca.receber_avaliacao('Gustavo', 5)
restaurante_praca.receber_avaliacao('Cloves', 4)

restaurante_mexicano = Restaurante('mexican food', 'Mexicana')
restaurante_mexicano.receber_avaliacao('Raul', 4)
restaurante_mexicano.receber_avaliacao('Maria', 4)

restaurante_Japones = Restaurante('Japa', 'Japonesa')
restaurante_Japones.receber_avaliacao('Natan', 2)
restaurante_Japones.receber_avaliacao('Paulo', 4)

restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':  
    main()