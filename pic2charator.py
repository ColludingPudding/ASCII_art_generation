import cv2.cv2 as cv2

# ASCII interpreter
ASCII_CHARS=list("@$B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`'. ")
def pixelsToASCII(img):
    characters = []
    for i in img:
        temp = []
        for j in i:
            temp.append(ASCII_CHARS[j//4])
        characters.append(temp)
    return(characters)
    

# Resize function
def resize(img, new_width = 200):
    width,height = img.shape
    ratio = width/height
    new_height = int(new_width * ratio)
    dim = (new_width,new_height)
    resized_image = cv2.resize(img, dim)
    resized_image = cv2.addWeighted( resized_image, 3, resized_image, 0, 1) # Contrast
    return(resized_image)

# Array -> string
def arrayToString(arr):
    ascii = ''
    for i in arr:
        ascii+= ' '.join(i)
        ascii+='\n'
    return ascii

def picToCharactor(img):
    img = cv2.imread(img,0)
    ASCII_converted = arrayToString(pixelsToASCII(resize(img)))
    with open("results2.txt", 'w') as f:
        f.write(ASCII_converted)

pic = "C:/Users/Dell/Desktop/special/test.png"
picToCharactor(pic)
