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
        self.file      = self.open_file(file_name, folder)
   


    def open_file(self : json_file, file_name : str, folder : str):
        if folder != "": 
            file_path = f"{folder}\\{file_name}"
        else:
            file_path = f"{file_name}"

        with open(file_path, "r+",encoding = "utf-8") as file:
            return file


    def read(self : json_file) -> dict:
        
        file = self.file
        return json.load(file)
    

    def write(self : json_file, message : str) -> dict:
        """
        Writes (not appends) a message to a specified JSON file
        """
        file = self.file
        return json.dump(message, file)