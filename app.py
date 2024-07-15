from modelos.restaurante import Restaurante

restaurante_outback = Restaurante('Outback', 'Costelinha')
restaurante_outback.receber_avaliacao('Deek', 9)
restaurante_outback.receber_avaliacao('Valdomiro', 10)
restaurante_outback.receber_avaliacao('Luis', 10)



def main():
    Restaurante.listar_restaurantes()



if __name__ == '__main__':
    main()