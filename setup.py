from cx_Freeze import setup, Executable#importe bibliotheque cxFreeze pour creer un executable
#creer un executable
setup(
    name = "Chiffrement",
    version = "0.1",
    description = "Programme qui chiffre en plusieurs systeme de chiffrement",
    executables = [Executable("main.py")]

)
