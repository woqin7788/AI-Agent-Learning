import json



class CustomerSaver:

    #保存数据到file_path地址
    def save(self,data,file_path:str):


        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:


            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )