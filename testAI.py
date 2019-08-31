# Test AI CatNotCat libraries

import AICatNotCat

from PIL import Image
imageName = "AITraining/cat.1332.jpg"

pil_img = Image.open(imageName)
pil_img.load()
pil_img = pil_img.resize((150,150),Image.ANTIALIAS)
print("size=", pil_img.size)
print("imname=", imageName)
AICatNotCat.AnalyzeCatNotCat(pil_img)

imageName = "AITraining/ukbench09941.jpg"

pil_img = Image.open(imageName)
pil_img.load()
pil_img = pil_img.resize((150,150), Image.ANTIALIAS)
print("size=", pil_img.size)
print("imname=", imageName)
AICatNotCat.AnalyzeCatNotCat(pil_img)

