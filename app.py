from Modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_praca.receber_avaliacao('João', 10)
restaurante_praca.receber_avaliacao('Maria', 2)
restaurante_praca.receber_avaliacao('Pedro', 5)
restaurante_mexicano = Restaurante('Mexican food', 'mexicano')
restaurante_mexicano.receber_avaliacao('Ana', 4)
restaurante_mexicano.receber_avaliacao('Carlos', 3)
restaurante_japones = Restaurante('Sushi express', 'japones')
restaurante_japones.receber_avaliacao('Lucas', 5)
restaurante_japones.receber_avaliacao('Fernanda', 4)
restaurante_tianeide = Restaurante('Tia neide', 'Brasileira')
restaurante_tianeide.receber_avaliacao('Rafael', 5)
restaurante_tianeide.receber_avaliacao('Juliana', 2)

restaurante_praca.alternar_estado()
restaurante_tianeide.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()