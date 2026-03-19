import os


magic_numbers = {"jpg": [b'\xff\xd8\xff'], 
                "png": [b'\x89\x50\x4e\x47'],
                "gif": [b'GIF87a', b'GIF89a'],
                "bmp": [b'BM'],
                "tiff": [b'II*\x00', b'MM\x00*'],    
                "pdf": [b'%PDF'],  
                "zip": [b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08'],
                "rar": [b'Rar!\x1a\x07\x00'],
                "7z": [b'7z\xBC\xAF\x27\x1C'],
                "exe": [b'MZ'],       
                "mp3": [b'ID3'],
                "wav": [b'RIFF'],    
                "mp4": [b'\x00\x00\x00\x18ftyp', b'\x00\x00\x00\x20ftyp'],
                "avi": [b'RIFF'],   
                "html": [b'<!DOCTYP', b'<html', b'<HTML'],
                "xml": [b'<?xml'],    
                "elf": [b'\x7fELF'],  
                "ps": [b'%!PS'],     
                "sqlite": [b'SQLite format 3\x00']}

#--------------------------- Extension spoofing check -------------------------------#

file_path = input("Enter file path: ")

# Get extension --->

ext = os.path.splitext(file_path)[1][1:].lower()

if not ext:
    print("no file extension found")

# Reading the magic number of the file --->

with open(file_path,"rb") as f:
    data = f.read(1024)


detected_type = None

for filetype, signatures in magic_numbers.items():
    for sig in signatures:
        if data.startswith(sig):
            detected_type = filetype
            break
    if detected_type:
        break


if detected_type:
    print(f"1. detected type: {detected_type}")
    print(f"2. file extension: {ext}")
    
    if detected_type != ext:
        print("3. extension spoofing detected")
    else:
        print("3. extension spoofing not detected")
else:
    print("3. unknown file type")

