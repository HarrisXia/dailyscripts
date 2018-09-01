import Image

infile = './ttt.jpg'
outfile = './ttt.jpg'
im = Image.open(infile)
(x,y) = im.size #read image size
x_s = 592 #define standard width
y_s = y * x_s / x #calc height based on standard width
out = im.resize((x_s,y_s),Image.ANTIALIAS) #resize image with high-quality
out.save(outfile)

print 'original size: ',x,y
print 'adjust size: ',x_s,y_s

'''
OUTPUT:
original size:  500 358
adjust size:  250 179
'''

