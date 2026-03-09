import json

class json_file():
    """
    A class designed to streamline writing and reading from json files

    **Paramaters:**
    
    file_name: str

    folder : str, deafults to "" if no argument is provided. 

    **Properties:**

    file_name : str, given by the 'file_name' paramter


    """

    def __init__(self : json_file, file_name : str, folder : str = "")->None:
        self.filepath      = self.set_file_path(file_name, folder)

   


    def set_file_path(self : json_file, file_name : str, folder : str):
        if folder != "": 
            self.file_path = f"{folder}\\{file_name}"
        else:
            self.file_path = f"{file_name}"
        
        


    def read(self : json_file) -> dict:
        
        with open(self.file_path,"rt",encoding="utf-8") as file:
            return json.load(file)
    

    def write(self : json_file, message : str, mode : str = "w"):
        """
        Writes (by deafult is set to the write mode) a message to a specified JSON file

        Pamaters : 
        """
        with open(self.file_path, mode.lower(), encoding="utf-8") as file:
            json.dump(message, file)
    


