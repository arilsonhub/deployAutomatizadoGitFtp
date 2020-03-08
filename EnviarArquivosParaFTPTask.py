from FtpManager import FtpManager

class EnviarArquivosParaFTPTask:

    def __init__(self, filesToSend, configData):
        self.filesToSend = filesToSend
        self.configData =  configData     

    def run(self):
        try:            
            self.sendFilesToFtpServer(self.configData)
            
        except Exception as e:
            print(e)   

    def sendFilesToFtpServer(self, configData):
        ftpConfig = configData['ftpConfig']
        ftpManager = FtpManager(ftpConfig['host'], ftpConfig['username'], ftpConfig['password'], ftpConfig['port'], ftpConfig['debugMode'])        
        ftpManager.sendFiles(configData, self.filesToSend)                