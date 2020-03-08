from pydriller import RepositoryMining

class GitManager:
    def __init__(self,repositoryURL,commitHash, gitRootDir):
        self.repositoryURL = repositoryURL
        self.commitHash = commitHash
        self.gitRootDir = gitRootDir.strip()

    def getListOfModifiedFiles(self):        
        commitList = RepositoryMining(self.repositoryURL,only_commits=[self.commitHash]).traverse_commits()

        miningFileList = []
        gitModifiedFileList = []

        for commitObject in commitList:
            miningFileList = commitObject.modifications
            
        isGitRootDirSpecified = len(self.gitRootDir) > 0  

        for modifiedFile in miningFileList:
            modifiedFilePath = modifiedFile.new_path
            
            if isGitRootDirSpecified:
                if modifiedFilePath.rfind(self.gitRootDir) is not -1:
                    modifiedFilePath = modifiedFilePath.replace(self.gitRootDir+'/', '')
                    gitModifiedFileList.append({'path': modifiedFilePath})
            else:
                gitModifiedFileList.append({'path': modifiedFilePath})

        return gitModifiedFileList