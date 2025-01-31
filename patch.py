import re
import os

# Path to the file
CURRENT_PATH: str = os.path.dirname(os.path.abspath(__file__))
FILE_PATH: str = os.path.join(CURRENT_PATH, "lib", "micropython", "ports", "esp32", "modules", "inisetup.py")
OBO_CAR_BOOT_PATH: str = os.path.join(CURRENT_PATH, "src", "obo-car", "boot.py")

# Regex pattern to match the f.write() content inside the block
pattern: re.Pattern = re.compile(
    r'with\s*open\s*\(\"boot.py\"\s*,\s*\"w[a-z]*"\)\s*as\s*f\s*:\s*f.write\(\s*"+\\*\s*[a-zA-Z\s#\(\-\)\.]+"+\s*\)', 
    re.DOTALL
)

# Replacement content for boot.py
replacement: str

# Read the file to modify
with open(FILE_PATH, "r") as file:
    data = file.read()

with open(OBO_CAR_BOOT_PATH, "r",encoding="utf-8") as file:
    replacement = f'''
    with open("boot.py", "w") as f:
        f.write(
            """{file.read().strip()}"""
        )
    '''

print(replacement)
# Substitute the content inside the f.write() block
new_data = re.sub(pattern, replacement, data)

# Write the modified content back to the file
with open(FILE_PATH, "w") as file:
    file.write(new_data)

print("File patched successfully!")
