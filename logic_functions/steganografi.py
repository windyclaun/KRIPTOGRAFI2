from PIL import Image

def genData(data):
    newd = []
    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd

# Modify pixels according to the 8-bit binary data
def modPix(pix, data):
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):
        pix = [value for value in imdata.__next__()[:3] +
                            imdata.__next__()[:3] +
                            imdata.__next__()[:3]]
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j] % 2 != 0):
                pix[j] -= 1
            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if pix[j] != 0:
                    pix[j] -= 1
                else:
                    pix[j] += 1
        if i == lendata - 1:
            if pix[-1] % 2 == 0:
                if pix[-1] != 0:
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
        else:
            if pix[-1] % 2 != 0:
                pix[-1] -= 1
        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]

# Encode the data into the image
def embed_msg(image_data, output_image_path, message):
    img = Image.open(image_data)
    newimg = img.copy()
    if len(message) == 0:
        raise ValueError("Data to be encoded is empty")
    x, y = 0, 0
    for pixel in modPix(newimg.getdata(), message + '###'):  # Append delimiter
        newimg.putpixel((x, y), pixel)
        if (x == newimg.width - 1):
            x = 0
            y += 1
        else:
            x += 1
    newimg.save(output_image_path)
    return output_image_path

# Decode the hidden data from the image
def extract_msg(input_image_path):
    img = Image.open(input_image_path)
    imgdata = iter(img.getdata())
    data = ''
    while True:
        pixels = [value for value in imgdata.__next__()[:3] +
                                imgdata.__next__()[:3] +
                                imgdata.__next__()[:3]]
        binstr = ''
        for i in pixels[:8]:
            binstr += '0' if i % 2 == 0 else '1'
        data += chr(int(binstr, 2))
        if pixels[-1] % 2 != 0:
            return data.rstrip('###')

