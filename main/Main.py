from WebScraping import WebScraping
from Reader import Reader

class Main():
    
    # FINALS VARIABLES FOR TEXT
    INFO_MSG = '[INFO] ==> '
    ERRO_MSG = '[ERRO] ==> '
    EXIT_MSG = '[EXIT] ==> Fechando programa'
    
    def __init__(self, ):
        self._reader = Reader()

    def apresentacao(self, ):
            print('====================================================')
            print('===========         WEB-SCRAPING         ===========')
            print('===========       By: Thiago Ramos       ===========')
            print('====================================================')
    
    def getDolar(self, ):
        print('\n' + self.INFO_MSG + 'Iniciando Web Scraping da cotação do Dolar em Rais')

        webScrap = WebScraping(
            END_POINT= 'https://www.remessaonline.com.br/cotacao/cotacao-dolar',
            FILE_DESC= 'cotacao',
            FILE_FORMAT= 'txt'
        )

        isOk= webScrap.generateResponse()

        if(isOk == True):
            filePathName= webScrap.getFileName() 
            fileName= filePathName[filePathName.index('/') + 1: len(filePathName)]
            print(self.INFO_MSG + 'Response em arquivo: ' + fileName)

            dolar= self._reader.readDolarResponse(filePathName)
            result= self.INFO_MSG + 'A cotação do Dolar está em ' + dolar
            print(result)
        
        else:
            print(self.ERRO_MSG + 'Response não gerado.')

        webScrap.deleteFile() # Remove for see the response
        print(self.EXIT_MSG)
        exit
        

# Inicialize
main = Main()

# Presentation and credits
main.apresentacao()

# Process Dolar
main.getDolar()