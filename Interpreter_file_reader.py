import json
from file_class import json_file





#global variables

folder = "json_files"
commands_file = json_file(f"{folder}\\commands.json")


def DEBUG_read_files():
    return format_byte_code(get_specified_byte_code("add"),8)

def get_specified_byte_code(instruction_name : str):
    """
    Gets the byte code (the binary represnetatrion of the instruction) from the specified insturction name.
    
    NOTE: All instructions are written as a string.
    
    NOTE: The variable name should be checked before running this instruction.
    """
    
    all_instructions   = commands_file.read()
    byte_code = all_instructions[instruction_name]
    return byte_code



def instruction_exists(instruction_name : str) -> bool:
    all_instructions   = commands_file.read()
    return instruction_name in all_instructions.keys()



def format_byte_code(byte_code : int, ammount_of_bytes : int) -> str:
    
    return format(byte_code, f"0{ammount_of_bytes}b")

print(DEBUG_read_files())