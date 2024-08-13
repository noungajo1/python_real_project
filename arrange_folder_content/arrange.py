"""
This project is for arrange all files in one folder
"""

import os
import shutil

# Répertoire où les images seront sauvegardées
save_dir = "/home/fre/Documents/folder"

# Répertoire courant
current_dir = os.path.dirname(os.path.realpath(__file__))
print("Current directory:", current_dir)


# Parcourir les fichiers du répertoire courant
for filename in os.listdir(current_dir):
    if filename.endswith((".jpg", ".png", ".gif")):
        # Créer le répertoire Images dans save_dir s'il n'existe pas déjà
        images_dir = os.path.join(save_dir, "Images")
        os.makedirs(images_dir, exist_ok=True)
        # Chemin complet du fichier source
        file_path = os.path.join(current_dir, filename)
        
        # Chemin complet du fichier de destination
        dest_path = os.path.join(images_dir, filename)
        
        # Copier le fichier dans le dossier Images
        shutil.copy(file_path, dest_path)
        
        # Supprimer le fichier source après la copie
        os.remove(file_path)
        
        print(f"{filename} moved to Images folder")

    if filename.endswith((".pdf", ".docx")):
        # Créer le répertoire Images dans save_dir s'il n'existe pas déjà
        images_dir = os.path.join(save_dir, "Documents")
        os.makedirs(images_dir, exist_ok=True)
        # Chemin complet du fichier source
        file_path = os.path.join(current_dir, filename)
        
        # Chemin complet du fichier de destination
        dest_path = os.path.join(images_dir, filename)
        
        # Copier le fichier dans le dossier Images
        shutil.copy(file_path, dest_path)
        
        # Supprimer le fichier source après la copie
        os.remove(file_path)
        
        print(f"{filename} moved to Documents folder")

    if filename.endswith((".mp4", ".wmv")):
        # Créer le répertoire Images dans save_dir s'il n'existe pas déjà
        images_dir = os.path.join(save_dir, "Videos")
        os.makedirs(images_dir, exist_ok=True)
        # Chemin complet du fichier source
        file_path = os.path.join(current_dir, filename)
        
        # Chemin complet du fichier de destination
        dest_path = os.path.join(images_dir, filename)
        
        # Copier le fichier dans le dossier Images
        shutil.copy(file_path, dest_path)
        
        # Supprimer le fichier source après la copie
        os.remove(file_path)
        
        print(f"{filename} moved to Videos folder")

print("All done")
