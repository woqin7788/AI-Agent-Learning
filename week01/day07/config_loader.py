import json
from logger import logger

class ConfigLoader:
    #加载config配置
    def load(self,file_path):
        try:
            with open(file_path,'r',encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            logger.info("加载config配置出错，文件不存在")
