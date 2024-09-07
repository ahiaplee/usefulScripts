import sys
import os

def decimal_to_reg_dword(decimal_value):
    # Convert decimal to hexadecimal with 8 digits, zero-padded
    hex_value = format(decimal_value, '08x')
    # Return the formatted string
    return f'dword:{hex_value}'

fileContents = '''Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Control Panel\Cursors]
"CursorBaseSize"={}

[HKEY_CURRENT_USER\Control Panel\Cursors\Schemes]
"YaruWindows"="{}"
'''

if __name__ == "__main__":
    cursorPath = os.path.abspath(sys.argv[1]).__str__().replace('\\', '\\\\')
    cursors = f"{cursorPath}\\\\arrow.cur,{cursorPath}\\\\whats_this.cur,{cursorPath}\\\\half-busy.ani,{cursorPath}\\\\wait.ani,{cursorPath}\\\\cross.cur,{cursorPath}\\\\text.cur,{cursorPath}\\\\pencil.cur,{cursorPath}\\\\not-allowed.cur,{cursorPath}\\\\size_ver.cur,{cursorPath}\\\\size_hor.cur,{cursorPath}\\\\size-fdiag.cur,{cursorPath}\\\\size-bdiag.cur,{cursorPath}\\\\move.cur,{cursorPath}\\\\sb_up_arrow.cur,{cursorPath}\\\\hand.cur"
    
    filename = 'AddYaruWindowsCursorTheme.reg'
    fontSize = 32
    with open(filename, 'w') as file:
        file.write(fileContents.format(decimal_to_reg_dword(fontSize), cursors))
        
    print(f"Created {filename}")
