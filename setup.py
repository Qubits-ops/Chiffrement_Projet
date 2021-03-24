from cx_Freeze import setup, Executable

setup(
    name = "Chiffrement",
    version = "0.1",
    description = "Programme qui chiffre en plusieurs systeme de chiffrement",
    executables = [Executable("main.py")]

)
