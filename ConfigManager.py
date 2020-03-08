import json

class ConfigManager:

    def getConfigData(self):
        data = None
        try:
            with open('config.json') as jsonFile:
                data = json.load(jsonFile)

            if data is not None:
                return data
        except Exception as e:
            raise Exception("Não foi possível ler o arquivo de configuração: " + str(e))