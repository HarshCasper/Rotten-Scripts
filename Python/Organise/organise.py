import os
import shutil

dir_path = os.path.dirname(os.path.realpath(__file__))

try:
    print("Organising your files...")
    for filename in os.listdir(dir_path):
        # Check if files are images
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp", ".pbm", ".pnm")):
            # If images folder doesnt exist then create
            if not os.path.exists("images"):
                os.makedirs("images")
            shutil.copy2(filename, "images")
            os.remove(filename)

        # Check if files are music
        if filename.lower().endswith((".wav", ".mp3", ".flac", ".3gp", ".aa", ".aax", ".aiff", ".raw")):
            # If music folder doesnt exist then create
            if not os.path.exists("music"):
                os.makedirs("music")
            shutil.copy2(filename, "music")
            os.remove(filename)

        # Check if files are executables
        if filename.lower().endswith((".exe", ".tar", ".deb")):
            # If executables folder doesnt exist then create
            if not os.path.exists("executables"):
                os.makedirs("executables")
            shutil.copy2(filename, "executables")
            os.remove(filename)

        # Check if files are documents
        if filename.lower().endswith((".txt", ".pdf", ".docx")):
            # If executables folder doesnt exist then create
            if not os.path.exists("documents"):
                os.makedirs("documents")
            shutil.copy2(filename, "documents")
            os.remove(filename)

except OSError:
    print("Error")
finally:
    # When script is finished clear screen and display message
    os.system("cls" if os.name == "nt" else "clear")
print("Finished organising your files")