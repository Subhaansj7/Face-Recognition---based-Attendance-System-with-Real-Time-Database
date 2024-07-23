import os
import cv2
import face_recognition
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("D:/Firebase/ServiceAccountKey.json")
firebase_admin.initialize_app(cred,{
    "databaseURL":"------------------------------------------",
    "storageBucket":"----------------------------------"
})

#Importing the students images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentsIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    studentsIds.append(os.path.splitext(path)[0] )

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    #print([path])
    #print(os.path.splitext(path)[0])
print(studentsIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList
print("Encoding Started ... ")
encodeListKnown = findEncodings(imgList)
encodeListKownWithIds = [encodeListKnown,studentsIds]
print(encodeListKnown)
print("Encoding Complete")

file = open("EncodeFile.p",'wb')
pickle.dump(encodeListKownWithIds,file)
file.close()
print("File Saved")
