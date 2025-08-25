from PIL import Image
import os
import sys
from pathlib import Path

current_dir = Path(__file__).parent

if __name__ == '__main__':
    TARGET_BOUNDS = (800, 800)

    # Load the EPS at 10 times whatever size Pillow thinks it should be
    # (Experimentaton suggests that scale=1 means 72 DPI but that would
    #  make 600 DPI scale=8⅓ and Pillow requires an integer)
    seed_name = "seed"
    folder_path = f"{current_dir}/results/{seed_name}"
    directory = os.fsencode(folder_path)

    new_folder_path = f"{current_dir}/results/{seed_name}_Final"

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(f"filename: {filename}")
        if filename.endswith(".eps"):
            image_path = f"{folder_path}/{filename}"
            pic = Image.open(image_path)
            pic.load(scale=10)

            # Ensure scaling can anti-alias by converting 1-bit or paletted images
            if pic.mode in ('P', '1'):
                pic = pic.convert("RGB")

            # Calculate the new size, preserving the aspect ratio
            ratio = min(TARGET_BOUNDS[0] / pic.size[0],
                        TARGET_BOUNDS[1] / pic.size[1])
            new_size = (int(pic.size[0] * ratio), int(pic.size[1] * ratio))

            # Resize to fit the target size
            pic = pic.resize(new_size, Image.LANCZOS)

            # Save to PNG
            pic.save(f"{new_folder_path}/{filename.replace('.eps', '.png')}")
