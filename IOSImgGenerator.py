import cairosvg
import json
import os
from multiprocessing.pool import ThreadPool
from os.path import splitext, join
from PIL import Image

INPUT_FORMATS = ['svg', 'png', 'jpg']
EXT_OUT = '.png'
OUTPUT_BASE = 'output'
THREADS = 4


def getExt(file_name):
    name, ext = splitext(file_name)
    return ext.replace('.', '')


def saveResults(files, results):
    result_dict = dict()
    result_dict['results'] = dict()
    i = 0
    for file in files:
        result_dict['results'][file] = results[i]
        i += 1

    result_dict["total_processed"] = i

    with open("results.txt", 'w') as file_results:
        file_results.write(
            json.dumps(result_dict, indent=4)
        )


def process_images():
    list_dir = os.listdir('.')
    dir_files = [f for f in list_dir if os.path.isfile(f)]
    files_to_process = list()
    for f in dir_files:
        ext = getExt(f)
        if ext in INPUT_FORMATS:
            files_to_process.append(f)

    pool = ThreadPool(THREADS)
    results = pool.map(create_multiple_sizes, files_to_process)

    saveResults(files_to_process, results)

    pool.close()
    pool.join()


def create_multiple_sizes(file_name):
    name, ext = splitext(file_name)
    IMG_BASE_DIR = join(OUTPUT_BASE, name)
    os.makedirs(IMG_BASE_DIR)
    pdf_generated = False
    img_pdf_path = join(IMG_BASE_DIR, name + '_Global.pdf')

    if ext == '.svg':
        cairosvg.svg2png(url=file_name, write_to=name + '.png')
        cairosvg.svg2pdf(url=file_name, write_to=img_pdf_path)
        file_name = name + '.png'
        pdf_generated = True

    image = Image.open(file_name)

    name_3x = join(IMG_BASE_DIR, name + '_3x' + EXT_OUT)
    image.save(name_3x, 'PNG')

    if not pdf_generated:
        image_rgb = Image.new('RGB', image.size, (255, 255, 255))
        image_rgb.paste(image, mask=image.split()[3])
        image_rgb.save(img_pdf_path, 'PDF', resolution=100.0)

    # Get Images sizes
    width, height = image.size

    width_1x = int(width / 3)
    height_1x = int(height / 3)

    width_2x = int(width_1x * 2)
    height_2x = int(height_1x * 2)

    # Save with new sizes
    name_2x = join(IMG_BASE_DIR, name + '_2x' + EXT_OUT)
    img_2x = image.resize((width_2x, height_2x))
    img_2x.save(name_2x, 'PNG')

    name_1x = join(IMG_BASE_DIR, name + '_1x' + EXT_OUT)
    img_1x = image.resize((width_1x, height_1x))
    img_1x.save(name_1x, 'PNG')

    return name_1x, name_2x, name_3x, img_pdf_path


def main():
    process_images()


if __name__ == "__main__":
    main()
