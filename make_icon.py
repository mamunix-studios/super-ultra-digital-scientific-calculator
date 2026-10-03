import os
from PIL import Image

def create_ico():
    png_path = os.path.join("assets", "logo_m.png")
    output_dir = "assets"
    icon_path = os.path.join(output_dir, "mamunix_app.ico")
    
    if os.path.exists(png_path):
        img = Image.open(png_path)
        icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        img.save(icon_path, format="ICO", sizes=icon_sizes)
        print("\n===================================================")
        print("✅ Success: mamunix_app.ico successfully generated!")
        print("===================================================\n")
    else:
                print(f"❌ Error: {png_path}")

if __name__ == "__main__":
    create_ico()

