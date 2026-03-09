import json
from file_class import json_file, text_file





#global variables

commands_folder = "json_files"
commands_path = "commands.json"
commands_file = json_file(f"{commands_folder}\\{commands_path}")


user_folder = "user_files"
user_path = "user_text.txt"
writeable_code_file = text_file(f"{user_folder}\\{user_path}")

code_path = "compiled_code.txt"
compiled_code_file = text_file(f"{user_folder}\\{code_path}")



def split_code():
    code = writeable_code_file.read()
    new_code = code.split("\n")
    return new_code

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



def format_byte_code(byte_code : int, ammount_of_bits : int) -> str:
    
    return format(byte_code, f"0{ammount_of_bits}b")





def compile_code():
    code = split_code()
    new_code = ""
    ammount_of_bits = 16


    for line in code:
        if instruction_exists(line):
            byte_code = get_specified_byte_code(line)
            formated_byte_code = format_byte_code(byte_code, ammount_of_bits)
            new_code += formated_byte_code + "\n"
        else:
            pass #I HAVE NO IDEA

    compiled_code_file.write(new_code)