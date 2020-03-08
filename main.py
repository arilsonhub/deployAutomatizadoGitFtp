from EnviarArquivosParaFTPTask import EnviarArquivosParaFTPTask
from GitManager import GitManager
from ConfigManager import ConfigManager

configManager = ConfigManager()
configData = configManager.getConfigData()

repositoryURL = configData['gitConfig']['repositoryURL']
commitHash = configData['gitConfig']['commitHash']
gitRootDir = configData['gitConfig']['gitRootDir']

gitManager = GitManager(repositoryURL, commitHash, gitRootDir)
filesToSend = gitManager.getListOfModifiedFiles()

task = EnviarArquivosParaFTPTask(filesToSend,configData)
task.run()