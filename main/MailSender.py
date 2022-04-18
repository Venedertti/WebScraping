import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

class MailSender():

    # FINALS VARIABLES FOR TEXT
    INFO_MSG = '[INFO] ==> '

    def __init__(self, ):

        # Constants
        self._SENDER_EMAIL= 'venedertti.python@gmail.com'
        self._SENDER_PASS= 'Python@2022'
        self._DATE_TIME= datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self._REPORT_DEFAULT= 'ramos.oliveira.thi@gmail.com' # Default email to report 
        self._TIPOS_RELATORIOS = {'COT': 'COTAÇÃO DO DOLAR'}

        # Class variables
        self._report_email= self._REPORT_DEFAULT
        self._cotacao = ''

    def setEmailToReciveReport(self, email:str): # Update email to recive
        self._report_email= email

    def getCotacaoMessageAndSubjectCotacao(self, cotacao):
        html= """\
        <html>
            <body>
                <h2>Relatório Cotação</h2>
                <p>Relatório gerado em:.....{}</p>
                <p>Valor do dolar cotado:...{}</p>
                <a href="https://www.remessaonline.com.br/cotacao/cotacao-dolar">Para mais informações acessar</a>
            </body>
        </html>
        """.format(self._DATE_TIME, cotacao)
        
        subject= "[PYTHON] > Relatório de Cotação de Dólar."

        return html, subject
    
    def sendMail(self, TIPO_RELATORIO):    
        receiver_email= self._report_email
        html, subject=  '', ''
        
        if(TIPO_RELATORIO == self._TIPOS_RELATORIOS['COT']):
            html, subject= self.getCotacaoMessageAndSubjectCotacao(self._cotacao)
        
        msgText = 'Enviando relário de Cotação para o endereço: [{}].'.format(receiver_email)
        print(self.INFO_MSG + 'Relatório gerado com a seguinte data: {}'.format(self._DATE_TIME))
        print(self.INFO_MSG + msgText)
        print(self.INFO_MSG + 'Favor verificar caixa de spam.')

        message = MIMEMultipart("alternative")
        message["Subject"]= subject
        message["From"]= 'Venedertti'
        message["To"]= receiver_email

        htmlMsg= MIMEText(html, "html")
        message.attach(htmlMsg)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context= context) as server:
            server.login(self._SENDER_EMAIL, self._SENDER_PASS)
            server.sendmail( self._SENDER_EMAIL, receiver_email, message.as_string() )

        print(self.INFO_MSG + 'Email de Report enviado!')

    def gerarRelatorioCotacao(self, cotacao ):
        self._cotacao= cotacao
        self.sendMail(self._TIPOS_RELATORIOS['COT'])