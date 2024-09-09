import os
import sys

import pikepdf

def remove_pdf_password(input_pdf_path, output_pdf_path, password):
    try:
        with pikepdf.open(input_pdf_path, password=password) as pdf:
            pdf.save(output_pdf_path)
        
        print(f"Password removed successfully. Decrypted PDF saved to: {output_pdf_path}")
    
    except pikepdf.PasswordError:
        print("Error: Incorrect password")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inDir = sys.argv[1]
    password = sys.argv[2]
    outDir = sys.argv[3]
    # print(inDir)
    
    if not os.path.exists(inDir):
        print("directory not found")
        exit()
        
        
    for file in os.listdir(inDir):
        if not file.lower().endswith('.pdf'):
            continue
        
        print(inDir + '\\' + file, password, outDir + '\\' + file)
        remove_pdf_password(inDir + '\\' + file, outDir + '\\' + file, password)
        
        
    
    
    
