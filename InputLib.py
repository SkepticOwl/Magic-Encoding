from tkinter import filedialog, Tk  
from sys import stdout

last_message_length = 0 
def display_message(text: str):
    global last_message_length 
    stdout.write("\b"*last_message_length+text+" "*(last_message_length-len(text)))
    last_message_length = len(text)

def sanitize_input(prompt: str): return input(prompt).strip().lower() 

def read_mode(prompt: str): 
    response = sanitize_input(prompt) 
    if response == "1" or response == "encode": return True 
    elif response == "2" or response == "decode": return False 
    else: 
        print("Invalid mode!")
        return read_mode(prompt) 

def ask(prompt: str):
    response = sanitize_input(prompt) 
    while response != "no" and response != "yes":
        print("Invalid response!")
        response = sanitize_input(prompt) 
    return response == "yes"

def check_path(path: str): 
    if path == "": 
        print("No filepath given!") 
        exit() 

def chose_input(extension: str):
    tk_ui = Tk() 
    types = [extension == "" and ("All types", "") or ("Magic encoded", "*."+extension)]
    path = filedialog.askopenfilename(title = "Open", filetypes = types)
    tk_ui.destroy() 
    check_path(path)
    return path 

def chose_output(output_name: str, extension: str = ""):
    tk_ui = Tk() 
    ext = "*."+extension 
    path = filedialog.asksaveasfilename(title = "Save As", initialfile = output_name, defaultextension = ext, filetypes = [(extension, ext)])
    tk_ui.destroy() 
    check_path(path) 
    return path
