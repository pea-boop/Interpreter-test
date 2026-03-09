import json


class base_file():
    """
    A class designed to streamline writing and reading from files

    **Paramaters:**
    
    file_name: str

    folder : str, deafults to "" if no argument is provided. 

    **Properties:**

    file_name : str, given by the 'file_name' paramter


    """


    def __init__(self, file_name : str, folder : str = "")->None:
        self.filepath      = self.set_file_path(file_name, folder)

   


    def set_file_path(self, file_name : str, folder : str):
        if folder != "": 
            self.file_path = f"{folder}\\{file_name}"
        else:
            self.file_path = f"{file_name}"


class json_file(base_file):


    def read(self : json_file) -> dict:
        
        with open(self.file_path,"rt",encoding="utf-8") as file:
            return json.load(file)
    

    def write(self : json_file, message : str, mode : str = "w") -> None:
        """
        Writes (by deafult is set to the write mode) a message to a specified JSON file

        Pamaters : 
        """
        with open(self.file_path, mode.lower(), encoding="utf-8") as file:
            json.dump(message, file)
    


class text_file(base_file):

    def read(self : text_file) -> str:
        
        with open(self.file_path,"rt",encoding="utf-8") as file:
            return file.read()
    

    def write(self : text_file, message : str, mode : str = "w") -> None:
        """
        Writes (by deafult is set to the write mode) a message to a specified JSON file

        Pamaters : 
        """
        with open(self.file_path, mode.lower(), encoding="utf-8") as file:
            file.write(message)