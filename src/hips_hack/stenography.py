import cv2
import numpy as np
import os
import re
import sys


def encode(imagePath:str, dataToEncrypt:str, outputImagePath:str) -> None:
    """Encodes data into an image
    
    Args:
        imagePath (str): Path to image
        dataToEncrypt (str): Data to encrypt
        outputImagePath (str): Path to output image
        
        Returns:
            None"""
    
    findSlash = [m.start() for m in re.finditer('/', outputImagePath)]
    
    if len(findSlash) != 0:
        imgName       = outputImagePath[findSlash[-1]+1:]
        pathBeforeImg = outputImagePath[:findSlash[-1]+1]
        if not os.path.isdir(pathBeforeImg):
            print('Output directory not found')
            exit()

    # check if image exists
    if not os.path.isfile(imagePath):
        print('Image not found')
        exit()

    imageData    = cv2.imread(imagePath)
    imgArea      = imageData.shape[0] * imageData.shape[1]
    numBytesPic  = int(np.floor(imgArea * 3))
    numLocations = int(np.ceil(np.log2(imgArea)))
    imgDatFlat   = imageData.flatten()

    splitData  = list(_split(dataToEncrypt, numLocations))   # split data into 10 parts
    temp       = []
    for d in splitData:
        temp.append(''.join(format(ord(i), '08b') for i in d))
    splitData = temp
    for i,d in enumerate(splitData):
        splitData[i] = d + '00000000'
    splitMergedData = ''.join(splitData)
    maxDataLen = max([len(d) for d in splitData])

    maxNumBits       = int(np.ceil(np.log2(numBytesPic)))
    numBytesReserved = numLocations * (8 + maxNumBits)
    numBytesUsable   = numBytesPic-numBytesReserved

    indices, indicesEnds = _getIndices(numBytesUsable, numLocations, maxDataLen, splitData)
    print(np.max(indices), numBytesUsable, len(imgDatFlat))
    try:
        assert np.max(indices) < numBytesUsable
    except:
        indices, indicesEnds = _getIndices(numBytesUsable, numLocations, maxDataLen, splitData)
        try:
            assert np.max(indices) < numBytesUsable
        except:
            indices, indicesEnds = _getIndices(numBytesUsable, numLocations, maxDataLen, splitData)
            try:
                assert np.max(indices) < numBytesUsable
            except:
                indices, indicesEnds = _getIndices(numBytesUsable, numLocations, maxDataLen, splitData)
                try:
                    assert np.max(indices) < numBytesUsable
                except:
                    indices, indicesEnds = _getIndices(numBytesUsable, numLocations, maxDataLen, splitData)
                    try:
                        assert np.max(indices) < numBytesUsable
                    except:
                        print('Could not find enough space to encode data')
                        exit()

    

    maxNum  = len(format(numBytesPic, 'b'))
    allIndicesEnds = ''
    for i,num in enumerate(indicesEnds):
        num = format(num, 'b')
        num = num.zfill(maxNum)
        allIndicesEnds += num

    for i,indx in enumerate(indices):
        rgb = imgDatFlat[indx]
        rgb = format(rgb, '08b')
        rgb = rgb[:-1] + str(splitMergedData[i])
        imgDatFlat[indx] = int(rgb, 2)


    curRGBIdx = 0
    imgDatFlat = imgDatFlat[::-1]
    for i,rgb in enumerate(imgDatFlat):
        rgb = format(rgb, '08b')
        rgb = rgb[:-1] + str(allIndicesEnds[curRGBIdx])
        curRGBIdx += 1
        imgDatFlat[i] = int(rgb, 2)
        if curRGBIdx == len(allIndicesEnds):
            break
    imgDatFlat = imgDatFlat[::-1]
    imageData  = imgDatFlat.reshape(imageData.shape)
          
    cv2.imwrite(outputImagePath, imageData)
    print('Image encrypted successfully, saved as to ', outputImagePath)
    return


def decode(imagePath:str) -> str:
    """Decodes data from an image
    
    Args:
        imagePath (str): Path to image
        
        Returns:
            str: Decrypted data"""
    
    imageData    = cv2.imread(imagePath)
    imgArea      = imageData.shape[0] * imageData.shape[1]
    numBytesPic  = int(np.floor(imgArea * 3))
    numLocations = int(np.ceil(np.log2(imgArea)))
    maxNum       = len(format(numBytesPic, 'b'))
    reverseData  = imageData.flatten()[::-1]
    locations    = _getLocations(reverseData, numLocations, maxNum)

    flattened    = imageData.flatten()

    binaryData  = ''
    unencrypted = ''
    for k,loc in enumerate(locations):
        curSearchArea = flattened[loc:]
        for rgb in curSearchArea:
            rgb   = format(rgb, '08b')
            rgb   = rgb[-1]
            binaryData += rgb
            if len(binaryData) == 8:
                newchar      = chr(int(binaryData, 2))
                if newchar == '\0':
                    binaryData   = ''
                    break
                unencrypted += newchar
                binaryData   = ''
    return unencrypted


def _getLocations(reverseData, numLocations, maxNum):
    locations     = []
    locationCount = 0
    temp          = ''
    for k, rgb in enumerate(reverseData):
        rgb   = format(rgb, '08b')
        rgb   = rgb[-1]
        temp += rgb
        if len(temp) == maxNum:
            locations.append(int(temp, 2))
            locationCount += 1
            temp = ''
            if locationCount == numLocations:
                return locations
    return locations


def _split(a, n):
    k, m = divmod(len(a), n)
    splitted = (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))
    return splitted


def _getIndices(numBytesUsable, numLocations, maxDataLen, splitData):
    indices = np.random.randint(0, numBytesUsable, numLocations) #[location1, location2];
    indices = np.sort(indices)
    for c in range(numLocations):
        for i,idx in enumerate(indices):
            if i == len(indices)-1:
                break
            if indices[i+1] - idx < maxDataLen:
                indices[i] = idx - maxDataLen
                if indices[i] < 0:
                    indices[i] = 0
                    indices[i+1] = maxDataLen
            if idx + maxDataLen > numBytesUsable:
                indices[i]   = numBytesUsable - maxDataLen
                indices[i+1] = numBytesUsable
    
    indicesEnds = indices.copy()
    idxs2       = np.array([], dtype=int)
    for i,idx in enumerate(indices):
        idxs2 = np.append(idxs2, np.arange(idx, idx+len(splitData[i])))
    idxs2   = np.array(idxs2, dtype=int)
    indices = idxs2
    return indices, indicesEnds



if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Stenography tool to encode and decode text into images")
    parser.add_argument("-e", "--encode", help="Encode text into the following image")
    parser.add_argument("-d", "--decode", help="Decode text from the following image")
    parser.add_argument("-t", "--text",   help="Text to encode into the given image")
    # parse the args
    args = parser.parse_args()
    hasRun = False
    if args.encode:
        secret_data = args.text
        input_image = args.encode
        path, file  = os.path.split(input_image)
        filename, ext = file.split(".")
        output_image = os.path.join(path, f"{filename}_encoded.{ext}")
        print(f"[+] Encoding {secret_data} into {input_image} and saving it as {output_image} ...")
        # encode the data into the image
        encode(imagePath=input_image, dataToEncrypt=secret_data, outputImagePath=output_image)
        print("[+] Saved encoded image.")
        hasRun = True
    if args.decode:
        input_image = args.decode
        # decode the secret data from the image and print it in the console
        decoded_data = decode(input_image)
        print("[+] Decoded data:", decoded_data)
        hasRun = True
    if not hasRun:
        print()
        print("[-] No arguments provided. Use -h or --help for help.")
        print()
        print("[-] Example: python stenography.py -e tests/stockimage.png -t 'testing'")
        print()
        print("[-] Example: python stenography.py -d tests/stockimage_encoded.png")
        print()
        print("[-] Example: python stenography.py -e tests/stockimage.png -t 'testing' -d tests/stockimage_encoded.png")
        print()
