# 🔒✨ Magic Encoding ✨🔒

Magic Encoding is a method of encoding files only using the first 17 bytes. The purpose of the encoding is to encode the file using bytes that represent special/magic characters to confuse the file readers trying to open it. Any file encoded with this method will be seen as a "binary file" and will most likely cause errors to code and programs that try to read it as text. 

### How is the file encoded? 
The data encoding is very simple, for every byte in the original file, a div and mod of 16 is stored in the new file, then to decode the new file the very simple ```byte = div*16 + mod``` formula is applied. The encoding also stores the filename making the final form ```encoded_name + byte 17 + encoded_data```. Due to this, the encoded file **will be double in size**. 

### This was a small project of mine, however if anyone wants to take it seriously here are a few ideas to try:
**• encoding depth**: encode the file multiple times(however it can be bruteforced by checking for bytes values above 17 and it will keep increasing the file size, probably useful for small text files)

**• file compression**: compress the file without using bytes above 17(this may not be possible due to loss of information, but you're welcome to try it)

**• parallel processing**: utilize parallel programming to encode/decode files to increase speed. 

**• non-python implementation**: rewrite the project in a much faster programming language such as c/c++. 
