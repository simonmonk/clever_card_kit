import MFRC522
import RPi.GPIO as GPIO
  
class SimpleMFRC522:

  READER = None;
  TAG = { 'id' : None, 'text' : ''};
  KEY = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
  
  def __init__(self):
    self.READER = MFRC522.MFRC522()
  
  def read(self):
      tag = self.read_no_block()        
      while not tag:
          tag = self.read_no_block()  
      return tag
  
  def read_no_block(self):
    (status, TagType) = self.READER.MFRC522_Request(self.READER.PICC_REQIDL)
    if status != self.READER.MI_OK:
        return None
    (status, uid) = self.READER.MFRC522_Anticoll()
    if status != self.READER.MI_OK:
        return None
    self.TAG['id'] = self.uid_to_num(uid)
    self.READER.MFRC522_SelectTag(uid)
    status = self.READER.MFRC522_Auth(self.READER.PICC_AUTHENT1A, 8, self.KEY, uid)
    if status == self.READER.MI_OK:
         text = self.READER.MFRC522_Read(8)
         if text:
             self.TAG['text'] = ''.join(chr(i) for i in text)
    self.READER.MFRC522_StopCrypto1()
    return self.TAG
    

    
  def write(self, sector, text):
      tag = self.write_no_block(8, text)        
      while not tag:
          tag = self.write_no_block(8, text)  
      return tag


  def write_no_block(self, sector, text):
      (status, TagType) = self.READER.MFRC522_Request(self.READER.PICC_REQIDL)
      if status != self.READER.MI_OK:
          return None
      (status, uid) = self.READER.MFRC522_Anticoll()
      if status != self.READER.MI_OK:
          return None
      self.TAG['id'] = self.uid_to_num(uid)
      self.READER.MFRC522_SelectTag(uid)
      status = self.READER.MFRC522_Auth(self.READER.PICC_AUTHENT1A, 8, self.KEY, uid)
      self.READER.MFRC522_Read(8)
      if status == self.READER.MI_OK:
          data = bytearray()
          data.extend(text.ljust(16))
          self.READER.MFRC522_Write(8, data)
          text = self.READER.MFRC522_Read(8)
          if text:
              self.TAG['text'] = ''.join(chr(i) for i in text)
      self.READER.MFRC522_StopCrypto1()
      return self.TAG
      
  def uid_to_num(self, uid):
      n = 0
      for i in range(0, 5):
          n = n * 256 + uid[i]
      return n
          