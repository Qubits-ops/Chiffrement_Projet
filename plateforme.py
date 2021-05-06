import platform

def plateforme_detect():
    """
        detecte sur qu'elle plateform se trouve l'utilisateur
    """
    if platform.system() == "linux":
        print("vous etes sur linux")
    elif platform.system() == "Windows":
        print("vous etes sur Windows")
    else:
        print("vous etes sur mac")

