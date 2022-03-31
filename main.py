import pyqrcode#imported the pyqrcode package
def qr_code():#def is a keyword for cuntion, qr_code is the name of the function
  s='This is POWER python class'
  d=pyqrcode.create(s)#d is a qr code object, here qr code is in object form
  d.png('my_img.png',scale=6)#converting the qr to an image form #scale is for sixe of image
  #when you scan the code using camera, you see "his is POWER python class"
  print('Code Executed properly')

if __name__ == '__main__':
  qr_code()
  
