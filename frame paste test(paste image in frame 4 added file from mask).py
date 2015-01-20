import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
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
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list
    
def put_image_in_frame(original_image, directory=None):
    directory = os.path.dirname(os.path.abspath(__file__))
    frame1 = os.path.join(directory, 'triangleframe.jpg')
    #given_pic_file= os.path.join(directory)
    #given_pic = PIL.Image.open(original_image)
    given_pic_resize = original_image.resize((310, 42))
    frame1_img = PIL.Image.open(frame1)
    fig, axes = plt.subplots(1, 2)
    #axes[0].imshow(frame1_img, interpolation='none')
    
    frame1_img.paste(given_pic_resize, (310, 42), mask=given_pic_resize)
    fig2, axes2 =plt.subplots(1,2)
    #axes2[0].imshow(frame1_img.paste, interpolation = 'none')
    fig2.show()
    
def put_all_images_in_frames(directory=None):
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    #load all the images
    image_list, file_list = get_images(directory)  

    #go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = file_list[n].split('.')
        
        # Round the corners with radius = 30% of short side
        new_image = put_image_in_frame(image_list[n])
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    