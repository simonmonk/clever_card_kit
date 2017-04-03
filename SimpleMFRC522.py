import MFRC522
import RPi.GPIO as GPIO
  
class SimpleMFRC522:

  READER = None;
  
  KEY = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
  
  def __init__(self):
    self.READER = MFRC522.MFRC522()
  
  def read(self, sector=8):
      id, text = self.read_no_block(sector)        
      while not id:
          id, text = self.read_no_block(sector)  
      return id, text

  def read_id(self):
    id, text = self.read_no_block(sector)        
    while not tag:
      id, text = self.read_no_block(sector)  
    return id

  def read_id_no_block(self, sector=8):
    id, text = self.read_no_block(sector)
    return id
  
  def read_no_block(self, sector=8):
    (status, TagType) = self.READER.MFRC522_Request(self.READER.PICC_REQIDL)
    if status != self.READER.MI_OK:
        return None, None
    (status, uid) = self.READER.MFRC522_Anticoll()
    if status != self.READER.MI_OK:
        return None, None
    id = self.uid_to_num(uid)
    self.READER.MFRC522_SelectTag(uid)
    status = self.READER.MFRC522_Auth(self.READER.PICC_AUTHENT1A, sector, self.KEY, uid)
    block = ''
    if status == self.READER.MI_OK:
        block_in_1 = self.READER.MFRC522_Read(8) # 1st usable block of 16 bytes
        block_in_2 = self.READER.MFRC522_Read(9) # 2nd
        block_in_3 = self.READER.MFRC522_Read(10) # 3rd
        block = block_in_1 + block_in_2 + block_in_3
        if block:
             text_in = ''.join(chr(i) for i in block)
    self.READER.MFRC522_StopCrypto1()
    return id, text_in
    

    
  def write(self, text, sector=8):
      id, text_in = self.write_no_block(sector, text)        
      while not id:
          id, text_in = self.write_no_block(sector, text)  
      return id, text_in


  def write_no_block(self, sector, text):
      (status, TagType) = self.READER.MFRC522_Request(self.READER.PICC_REQIDL)
      if status != self.READER.MI_OK:
          return None, None
      (status, uid) = self.READER.MFRC522_Anticoll()
      if status != self.READER.MI_OK:
          return None, None
      id = self.uid_to_num(uid)
      self.READER.MFRC522_SelectTag(uid)
      status = self.READER.MFRC522_Auth(self.READER.PICC_AUTHENT1A, 8, self.KEY, uid)
      self.READER.MFRC522_Read(sector)
      text_in = ''
      if status == self.READER.MI_OK:
          data = bytearray()
          data.extend(text.ljust(48))
          self.READER.MFRC522_Write(8, data[0:16])
          self.READER.MFRC522_Write(9, data[16:32])
          self.READER.MFRC522_Write(10, data[32:48])
      self.READER.MFRC522_StopCrypto1()
      return id, text[0:48]
      
  def uid_to_num(self, uid):
      n = 0
      for i in range(0, 5):
          n = n * 256 + uid[i]
      return n
          