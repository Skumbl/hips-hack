![banner](https://github.com/Skumbl/hips-hack/blob/main/Screenshot%202023-02-04%20at%2020-19-31%20Modern%20Minimal%20Technology%20Background%20Banner.png)
# H.I.P.S
HIPS or Hidden In Plain Sight is a command line utility that takes in a string and the pathway to a image in order to hide it inside the image bit by bit hidden in random pixels
It is also a web application linked bellow

# Web App (using Flask)
check out the web app here
> nojjktotvrgotyomnz.tech
##### the website name is above, try cracking the cypher to see what it means (not including .tech)

# Install

HIPS is both a web application as well as a pip install terminal package

#### install using pip

    pip3 install hips-hack

this will download the hips utility to your local machine
see **how to use** for the syntax and parameters for the terminal utility

#### download from github
if any of the other methods have gone down for some reason then you can always click this link to install the python package

[download here](https://github.com/Skumbl/hips-hack/blob/main/src/hips_hack/stenography.py)



# How to Use

###  syntax 

(-e )encrypts the message to an image

(-d )decrypts a message from image

( -t )denotes the start of the string being encrypted

< image path > is the local path to the image you are trying to encrypt or decrypt

to encrypt

    python3 -m hips_hack.stenograpghy -e <image path> -t <string to encode>

to decrypt

    python3 -m hips_hack.stenograpghy -d <image path>

the new image with the encryption will be placed 
# How it Works

One primary challenge of encoding text into images is making sure the image doesn't look different after being encoded. We accomplished this by taking each individual, red, green, blue value, and changing the last, or least significant bit, to represent a bit in ASCII text.

We started by doing this on the first X RGB values in the image, X being the number of binary bits required to represent the ASCII message typed in. However, this makes it pretty easy to figure out the encoded text, making the encoding useless. We needed a way to make it much more difficult to decipher the message (without using the decode method), and make the message more secure.

In order to solve this, we encrypted parts of the message throughout the message by indexing all the R, G, B values and randomly choosing which ones to write parts of the message to. So how will the decode message identify where these randomly chosen locations are (and how much text is stored starting at each one)? Well, after each piece of text (starting at a randomly chosen location), we include 8 zeroes, representing the null terminator string. This tells the decoder to stop reading the current set of encoded bits. But how does it know where these locations actually are? Well, in reverse order at the end of the file we encode the locations of the bits. When decoding, this information is pulled to start decoding the image.

This stenography tool was packaged into a pip package, which can be installed by any user into their python installation. We used a flask server, running on AWS, as flask is python and can natively run our stenography package. 


# Development Team

Dev Team Name - SWMG

Jan Arvik - Team Lead / Website Lead

Truman DeWelch- Command line/ PIP developer

Michael Peters - Flask / AWS developer 

Jack Savage - CSS / Typescript Developer
