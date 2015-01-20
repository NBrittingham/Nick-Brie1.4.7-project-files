import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import Image, ImageOps
import os.path  
import PIL.ImageDraw  

def get_images(directory=None):
    
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    directory = os.path.dirname(os.path.abspath(__file__)) 
    directory_list = os.listdir(directory) # Get list of files
    return file  
    
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list
    
def put_image_in_frame(directory=None):
    '''directory = os.path.dirname(os.path.abspath(__file__))
    frame1 = os.path.join(directory, 'triangleframe.jpg')
    given_pic_file= os.path.join(directory, given_pic)
    frame1_img = PIL.Image.open(frame1)
    fig, axes = plt.subplots(1, 2)
    axes[0].imshow(frame1_img, interpolation='none')
    
    frame1_img.paste(given_pic_file, (31, 449), mask=given_pic_file)
    #display
    fig2, axes2 =plt.subplots(1,2)
    axes2[0].imshow(frame1_img, interpolation = 'none')
    axes2[1].imshow(frame1_img, imterpolation = 'none')
    axes2[1].set_xlim(31,312)
    axes2[1].set_ylim(447,29)
    fig2.show()'''
    #for i in directory_list:
    img = Image.open('earth.png')
    img_with_border = ImageOps.expand(img,border=75,fill='black')
    img_with_border.save('bordered-%s'% 'earth.png')
