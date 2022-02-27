#@auto-fold regex /./
#https://muthu.co/instagram-quotes-generator-using-python-pil/
from PIL import Image, ImageDraw, ImageFont,ImageColor
import os,random, colourettu as c, img_gur
from python_helpers import python_helper as ph

def random_colour():
    colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return colour

def create_img(img_path='',size=(1000,1000), colour= random_colour()):
    """Use a folder path if you want a random image or an absolute path for a specfic image.
        If you dont choose a path then you can create a random colour image"""
    if img_path:
        if img_path.endswith('jpg') or img_path.endswith('png'):
            img = Image.open(ph.root_fp+img_path)
        else:
            img = Image.open(os.path.join(ph.root_fp+'IG-content-publisher/backgrounds/'+random.choice(os.listdir(ph.root_fp+'IG-content-publisher/backgrounds/'))))
        if size:
            img = img.resize(size, Image.ANTIALIAS)
    else:
        img = Image.new('RGBA', size, colour)
    return img

def check_contrast(img, txt_colour=''):
    """Check the text contrast of the img"""
    pixels = img.getcolors(img.size[0] * img.size[0])
    sorted_pixels = sorted(pixels, key=lambda t: t[0])     #Sort them by count number(first element of tuple)
    dominant_color = sorted_pixels[-1][1][-3:]     #Get the most frequent color
    txtcolour = random_colour() if not txt_colour else ImageColor.getrgb(txt_colour)
    contra  = c.contrast(dominant_color,txtcolour)
    return [contra,img]

def choose_img(img,txt_colour=''):
    """Check to see if the contrast is above x levels """
    nums = True
    while nums:
        img = check_contrast(img,txt_colour)
        if img[0] >7:
            return img[1]
            nums = False
        else:
            print("Trying again contrast with text very low")

def wrap_text(sentence):
    new_text = ""
    new_sentence = ""
    for word in sentence.split(" "):
        delim = " " if new_sentence != "" else ""
        new_sentence = new_sentence + delim + word
        if len(new_sentence) > 30:
            new_text += "\n" + new_sentence
            new_sentence = ""
    new_text += "\n" + new_sentence
    return new_text

def add_text(img, sentence, font_size=15, font_name=''):
    """Add centered text to image"""
    draw = ImageDraw.Draw(img)
    img_w,img_h = img.size
    font_name = 'Roboto-Bold' if not font_name else font_name
    # font = ImageFont.truetype(os.path.abspath(os.getcwd())+'\\font_list\\{0}.ttf'.format(font_name),size=font_size)
    font = ImageFont.truetype(ph.root_fp+'IG-content-publisher/font_list/{0}.ttf'.format(font_name),size=font_size)
    text_width, text_height = draw.textsize(wrap_text(sentence), font)
    position = ((img_w-text_width)/2, (img_h-text_height) / 2)
    draw.multiline_text(position, wrap_text(sentence), fill=(255,255,255), font=font)
    return img

def save_upload_img(img, file_name, file_type='png',upload='Y'):
    """Save the final image with the text and define size and files type"""
    img.save(ph.root_fp+'working_files/'+file_name+'.'+file_type,quality=100)
    print("Saved img {0}.{1} at {2}".format(file_name,file_type,ph.root_fp+'working_files/'))
    if upload =='Y':
        con  = img_gur.upload_path(ph.root_fp+'working_files/'+'joke'+'.'+file_type)
    return con['link']

def upload_img(sentence,file_name,font_size=15,font_name='',file_type='png',img_path='',size=(1000,1000),colour=random_colour(),upload='Y'):
    """create a new image, save the image, and upload it to img_gur"""
    img = create_img(img_path,size,colour)
    img = add_text(img,sentence,font_size,font_name)
    return save_upload_img(img,file_name,file_type,upload)
