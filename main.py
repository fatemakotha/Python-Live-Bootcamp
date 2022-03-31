import pyqrcode
def qr_code():
  s='This is POWER python class'
  d=pyqrcode.create(s)#d is a qr code object
  d.png('m9y_img.png',scale=6)
  print('Code Executed properly')
  
