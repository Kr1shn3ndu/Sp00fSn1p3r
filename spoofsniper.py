
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


file_path = input("Enter file path: ")

extension_spoofing = ""
png_manipulation = ""
double_extension = ""

if "." in file_path:
    ext = file_path.split('.')[-1].lower()

else:
    print("no file extension found")


with open(file_path,"rb") as f:
    data = f.read(69000)


detected_type = None

for filetype, signatures in magic_numbers.items():
    for sig in signatures:
        if data.startswith(sig):
            detected_type = filetype
            break
    if detected_type:
        break


if detected_type:
    
    if detected_type != ext:
        extension_spoofing = "detected"
    else:
        extension_spoofing = "not detected"
else:
    extension_spoofing = "unknown file type"


if detected_type == "png":
    if b'IHDR' not in data:
        png_manipulation = "missing IHDR"
    elif b'IEND' not in data:
        png_manipulation = "missing IEND"
    else:
        png_manipulation = "valid png"

        
parts = file_path.lower().split('.')

if len(parts) > 2 : 
    fake_extension = parts[-2]
    real_extension = parts[-1]

    keywords = ["exe","bat","scr","vbs"]

    if real_extension in keywords:
        double_extension = "detected" 
    else:
        double_extension = "not detected"


print("\nfinal summary output: ")
print(f"detected extension: {detected_type}")
print(f"file extension: {ext}")
print(f"extension spoofing: {extension_spoofing}")
print(f"png status: {png_manipulation}")
print(f"double extension: {double_extension}")