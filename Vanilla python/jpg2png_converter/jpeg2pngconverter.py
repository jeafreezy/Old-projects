import sys
import os
from PIL import Image
#grab the first and second argument
image_folder=sys.argv[1]
output=sys.argv[2]

#check if folder exists

"""while True:

    try:
        if os.path.isdir(output):
            print('Folder already exists')
        else:
            os.makedirs('Output')
    except FileExistsError as err:
        print(err)
        raise err

    for images in os.listdir(image_folder):
            if images.endswith('.jpg','r'):
                file=Image.open(images)
                converted_images = file.save(f'{output}\'filenames.png', 'png')
                continue
            else:
                continue
    else:
        break
"""



"""import sys
import os
from PIL import Image

path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(path):
  clean_name = os.path.splitext(filename)[0]
  img = Image.open(f'{path}{filename}')
  #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
  img.save(f'{directory}/{clean_name}.png', 'png')
  print('all done!')"""