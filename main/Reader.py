class Reader():
    
    def readDolarResponse(self, FILE_PATH):
        file_dolar= open(FILE_PATH, 'r') 
        response_dolar= file_dolar.read()

        index_inicio= response_dolar.index('Reais') - 5
        index_fim= response_dolar.index('Reais') 
        result_dolar= response_dolar[index_inicio:index_fim] + 'R$'

        return result_dolar