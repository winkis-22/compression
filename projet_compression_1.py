# creation d'un programme de compression et de decompression

# étape une importaion des differents modules

import gzip    # pour la compression
import os 

# etape intermediaire de declaration de variable

extention = {
    '.gz','.zip','.rar','.7z','.tar'
    '.bz2','.xz'
}

# étape deux creation des fonction principale

# création de la fontion de compression

def compression(fichier:str):
    try:
        _,ext = os.path.splitext(fichier)
        if ext.lower() in extention:
            print("le fichier",{fichier},"est déja compressé")
            return False
        else:
            with open(fichier,'rb') as f :
                contenue = f.read()
                fiche = fichier  + '.gz' 
                with gzip.open(fiche,'wb') as f_c:
                    f_c.write(contenue)
                    print("le fichier",{fichier},"a bien été compresser")
                    return fiche
    except FileNotFoundError:
        print("desolé le fichier",{fichier},"n'a pas été trouvé")
    except Exception as e:
        print("une erreur c'est produite",e)



# création de la fonction de décompression

def décompréssion(decompresse:str):
    try:
        if not decompresse.endswith('.gz'):
            print("le fichier n'a pas été compresser avec l'extention '.gz'")
            return False

        _,ext = os.path.splitext(decompresse)
        if ext.lower() != '.gz':
            print("le fichier",{decompresse},"est déja compressé")
            return False
        nom_fiche = os.path.splitext(decompresse)[0]
        nom , ext_orig = os.path.splitext(nom_fiche)
        with gzip.open(decompresse,'rb') as f :
            contenu = f.read()
            decompresse = nom + ext_orig 
        with open(decompresse,'wb') as f_c:
            f_c.write(contenu)
            print("le fichier" ,{decompresse},"a bien été decompressé") 
            return decompresse
    except FileNotFoundError:
        print("le fichier n'a pas été trouver")
    except Exception as e :
        print("le fichier n'a pas été trouvé par cause de:",e)   

compression("Korean_food.rar")