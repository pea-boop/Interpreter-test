import json



class json_file():
    def __init__(self : json_file, path : str)->None:
        self.file_path = path

    def read(self : json_file) -> dict:
        path = self.file_path
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    
    def write(self : json_file, message : str) -> dict:
        """
        Writes (not appends) a message to a specified JSON file
        """

        path = self.file_path
        with open(path, "w", encoding="utf-8") as file:
            return json.dump(message, file)




commands_file = json_file("commands.json")



def get_specified_byte_code(instruction_name : str):
    """
    Gets the byte code (the binary represnetatrion of the instruction) from the specified insturction name.
    
    NOTE: All instructions are written as a string.
    """
    
    all_instructions = commands_file.read()
    specific_byte_code = 