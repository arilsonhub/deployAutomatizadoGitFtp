from ftplib import FTP 
import os
import fileinput

class FtpManager:

    def __init__(self,host,username,password,port,debugMode):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.debugMode = debugMode

    def getFtpConnectionInstance(self): 
        ftp = FTP()
        ftp.set_debuglevel(self.debugMode)
        ftp.connect(self.host, self.port)
        ftp.login(self.username,self.password)

        return ftp

    def sendFiles(self, configData, fileList):
        ftpConnection = self.getFtpConnectionInstance()      

        pathToLocalFiles = configData['localConfig']['pathToFiles']        

        for localFile in fileList:
            
            localFilePath = ""            
            try:
            
                localFilePath = pathToLocalFiles + "/" + localFile['path']
                
                if os.path.isfile(localFilePath):
                        
                    pathToStoreInFtp = localFile['path']
                    localFileDirectory = localFile['path']
                    slashLastIndex = localFile['path'].rfind('/')
                    
                    if slashLastIndex is not -1:                    
                        localFileDirectory = localFileDirectory.split('/')
                        localFileDirectory.pop()
                        localFileDirectory = "/".join(localFileDirectory)
                    else:     
                        localFileDirectory = localFile['path']
                    
                    ftpDirectory = localFileDirectory    
                    localFileDirectory = pathToLocalFiles + "/" + localFileDirectory
                    self.createDirectoryIfNotExistsInFtp(ftpConnection, localFileDirectory, ftpDirectory)
                    
                    filePointer = open(localFilePath, 'rb')
                    ftpConnection.storbinary('STOR %s' % pathToStoreInFtp, filePointer)
                    filePointer.close()
                    
                else:
                    raise Exception('Arquivo inválido: ' + localFilePath)
                
            except Exception as e:
                print('Erro ao tentar enviar arquivo: ' + localFilePath + ' mensagem: ' + str(e))

        ftpConnection.quit()

    def createDirectoryIfNotExistsInFtp(self, ftpConnection, localDirectory, ftpDirectory):        
        isDirectory = os.path.isdir(localDirectory)        
        if isDirectory:
            try:
                ftpExistingDirList = ftpConnection.nlst()
                ftpDirectoryParts = ftpDirectory.split("/")                
                ftpDirectoryFullPath = ""
                       
                count = 0
                for directoryPart in ftpDirectoryParts:           
                    ftpDirectoryFullPath = ftpDirectoryFullPath + ("/" if count > 0 else "") + directoryPart
                    if ftpDirectoryFullPath not in ftpExistingDirList:
                        try:
                            ftpConnection.mkd(ftpDirectoryFullPath)
                        except Exception as e:
                            print('Criação do diretório: ' + ftpDirectoryFullPath + ' no FTP, mensagem: ' + str(e))
                    count = count + 1
                    
            except Exception as e:
                print('Não foi possível criar o diretório: ' + localDirectory + ' Mensagem: ' + str(e))