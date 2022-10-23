from os.path import basename, splitext 
from random import getrandbits
import InputLib

def random_hash(length: int): return f"%0{length}x" % getrandbits(length*4)

BYTES_PER_PRINT = 10**5*2 #200k bytes per print
FILE_EXTENSION = "mgenc"

def compute(data: bytes, mode: bool): 
    result = bytearray() 
    size = len(data)-1 
    for index, byte in enumerate(data): 
        if (index % BYTES_PER_PRINT == 0 or index == size) and size > BYTES_PER_PRINT: 
            percentage = index/size 
            bar_length = 50
            current = round(percentage*bar_length)
            formatted = "%.2f" % (round(percentage*10000)/100)
            InputLib.display_message(f"{mode and 'Encoded' or 'Decoded'}: [{'#'*current}{'-'*(bar_length-current)}] {formatted}%")
        if mode: result.extend([byte//16, byte%16]) 
        else: 
            if index % 2 == 0: multiplier = byte
            else: result.append(multiplier*16+byte)
    return bytes(result)

def encrypt(data: bytes): return compute(data, True) 
def decrypt(data: bytes): return compute(data, False) 

def encrypt_file(name: str, data: bytes):
    result = bytearray() 
    result.extend(encrypt(name.encode()))
    result.append(17)  
    result.extend(encrypt(data))
    return bytes(result) 

def decrypt_file(data: bytes): 
    enc_name, enc_data = data.split(b"\x11") 
    return decrypt(enc_name).decode(), decrypt(enc_data)

def main():
    print("[MODES]:")
    print("[1]: Encode")
    print("[2]: Decode\n")
    mode = InputLib.read_mode("Mode: ") 
    filepath = InputLib.chose_input(not mode and FILE_EXTENSION or "")  
    with open(filepath, "rb") as file: 
        if mode:
            data = encrypt_file(basename(file.name), file.read()) 
            name = random_hash(25)
            extension = FILE_EXTENSION 
        else: 
            filename, data = decrypt_file(file.read()) 
            name = splitext(filename)[0] 
            extension = splitext(filename)[1][1:]
        filename = InputLib.chose_output(name, extension) 
        with open(filename, "wb") as file: file.write(data) 
        if InputLib.ask("\nContinue? yes/no: "): main() 

if __name__ == "__main__": 
    main()
