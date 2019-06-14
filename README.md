# clever_card_kit
This is where you will find the source code for the Python programs used in the [MonkMakes Clever Card Kit for Raspberry Pi] (https://monkmakes.com/cck)

![MonkMakes Clever Card Kit for Raspberry Pi](https://www.monkmakes.com/wp-content/uploads/2017/04/kit-copy.jpg)

Feel free to make use of this code with any project that uses an RC-522 tag reader/writer. The class SimpleMFRC522 reduces the process of reading from and writing to a card to just two functions called read and write! Actually its a little more complicated than that, because read and write both block and wait for a card to be presented, and sometimes you need to be doing other stuff in your program while you wait for a tag to be scanned. So, there are also two extra functions read_no_block and write_no_block.

# Prerequisites

This library requires the SPI-Py library to be installed. I have made a clone of the original project here: https://github.com/lthiery/SPI-Py

This fork of SPI-Py made to change the line cs_change to 0 not 1 in spi.c to allow the RC522 RFID tag readers to work correctly. This issue is described here: https://github.com/raspberrypi/linux/issues/1547

So, you will either need to get the original and modify spi.c yourself, or use my fork here: https://github.com/simonmonk/SPI-Py

# Installation
Type the following commands from your Raspberry Pi's terminal.

```
$ cd /home/pi
$ git clone https://github.com/simonmonk/clever_card_kit.git
$ cd clever_card_kit
```

This isn't a proper Python library, so you can't install it. But within this directory, you will find test programs to try out the reader.


# Connecting up your Reader

This library assumes that the reader is connected to your Raspberry Pi in what seems to be the standard configuration of:

|Lead color|Smartcard Reader|Raspberry Pi pin|
|----------|----------------|----------------|
|Purple|SDA|8|
|Orange|SCK|11|
|Yellow|MOSI|10|
|White|MISO|9|
|Green|IRQ|Not connected|
|Black|GND|GND|
|Gray|RST|25|
|Red|3.3V|3.3V|


# API

## Import and Create an Instance

```
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()
```

## read()

This function takes no parameters and waits for a card to be presented to the reader. It then returns two values: id (the card id) and text (the 48 characters stored in sector 8 of the card)

```
id, text = reader.read()
print(id)
print(text)
```


## read_id()

This function is like 'read' but only returns the id, ignoring any text stored on the card.

```
id = reader.read_id()
print(id)
```


## write(text)

This function takes a text string and just waits for a card to be presented to the reader. It then writes the first 48 characters of text (padding if needed) to sector 8 of the card. It then returns the id and text that were just written.


```
text = raw_input('New Text: ')
print("Now scan a tag to write")
id, text = reader.write(text) 
print("written")
print(id)
print(text)
```


## read_no_block()

This function takes no parameters and if no card is being presented to the reader immediately returns two values None and None, indicating that no id or text were read. If a card is on the reader, then it returns two values: id (the card id) and text (the 48 characters stored in sector 8 of the card)

The code example below would normally be in a loop.

```
id, text = reader.read_no_block()
if id:
    print(id)
```




## read_id_no_block()

This function is like 'read_no_block' but only returns the id, ignoring any text stored on the card. If there is no card present, None is returned.

```
id = reader.read_id_no_block()
print(id)
```


## write_no_block(text)

This function takes a text string and if no card is being presented to the reader immediately returns None, None. If a card is on the reader, then it writes the text string to sector 8 of the card and returns two values: id (the card id) and text (the 48 characters stored in sector 8 of the card)

The code example below would normally be in a loop.

```
id, text = reader.write_no_block('hello')
if id:
    print(id)
    print(text)
```

