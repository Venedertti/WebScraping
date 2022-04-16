from bs4 import BeautifulSoup
import requests
import os

class WebScraping():

    # VARIABLES FOR SYSTEM
    _URL_REQUEST:str = ''
    _RESPONSE_FILE_NAME:str = 'src/response'

    # FINALS VARIABLES FOR TEXT
    INFO_MSG = '[INFO] ==> '
    ERRO_MSG = '[ERRO] ==> '
    EXIT_MSG = '[EXIT] ==> '

    def __init__(self, END_POINT, FILE_DESC, FILE_FORMAT):
        file_name = '_{}.{}'.format(FILE_DESC.lower(), FILE_FORMAT.lower())    
        self._RESPONSE_FILE_NAME = self._RESPONSE_FILE_NAME + file_name
        self._URL_REQUEST = END_POINT

    def getFileName(self, ):
        return str(self._RESPONSE_FILE_NAME)

    def request(self, ):
        print(self.INFO_MSG + "Enviando request para site: " + self._URL_REQUEST)
        response = requests.get(self._URL_REQUEST)
        
        if(response.status_code == 200):
            html = response.content
            soup = BeautifulSoup(html, 'html.parser') # Parsed to html
            print(self.INFO_MSG + "Resposta Recebida!")

        else:
            print(self.INFO_MSG + "Resposta não recebida. URL inexistente ou indisponivel")
            print(self.ERRO_MSG + 'Fechado programa.')

        return soup;

    def deleteFile(self, ):
        os.remove(self._RESPONSE_FILE_NAME)

    def checkIfFileExists(self, delete):
        file_exists = os.path.exists(self._RESPONSE_FILE_NAME)
        
        if(delete == True):
            if(file_exists == True):
                self.deleteFile()
                return False;
        
        else:
            if(file_exists == True):
                response = open(self._RESPONSE_FILE_NAME, 'r')

                if(response == ''):
                    return False
                else: 
                    return True


    def writeHtml(self, html):
        file = open(self._RESPONSE_FILE_NAME, 'x')
        file.write(html)
        
        print(self.INFO_MSG + 'Novo arquivo de response gerado.')
        
        file.close()

    def generateResponse(self, ):

        # Get response
        html = self.request().prettify().encode('cp1252', errors='ignore')
        
        # Delete response if exists
        self.checkIfFileExists(delete= True)
        
        # Creante and write a new response
        self.writeHtml(html=str(html))

        # Check if response exist and is valid 
        file_is_valid = self.checkIfFileExists(delete= False)
        
        if(file_is_valid == True):
            print(self.INFO_MSG + 'Arquivo de response criado e válido.')

        else:
            print(self.ERRO_MSG + 'Response gerado em arquivo inválido. Favor verificar.')
            
        return file_is_valid

