import cv2
from cv2 import imwrite
from cv2 import VideoCapture
import face_recognition
import pickle
from os import listdir
from os.path import isfile, join

def saveface(person_name, person_image):
    imgelon = face_recognition.load_image_file(person_image)
    imgelon = cv2.cvtColor(imgelon,cv2.COLOR_BGR2RGB)
    all_face_encodings = {}
    all_face_encodings[person_name] = face_recognition.face_encodings(imgelon)[0]

    with open('Faces/'+ str(person_name) + ".dat", 'wb') as f:
        pickle.dump(all_face_encodings, f)

def compareface(firstperson, secondpersonimage):
    with open('Faces/'+ str(firstperson) + ".dat", 'rb') as f:
        all_face_encodings = pickle.load(f)

    compsec = face_recognition.load_image_file(secondpersonimage)
    compsec = cv2.cvtColor(compsec, cv2.COLOR_BGR2RGB)
    try:
        compsec_encode = face_recognition.face_encodings(compsec)[0]
        x = face_recognition.compare_faces([all_face_encodings[firstperson]],compsec_encode)
        if x[0] == True:
            return firstperson
        else:
            return "Unknown"
    except IndexError:
        return "Unknown"

def loadfaces(person):
    with open('Faces/' + str(person) + ".dat", 'rb') as f:
        all_face_encodings = pickle.load(f)
    
    return all_face_encodings

def createlistoffaces():
    files = [f for f in listdir("Faces/") if isfile(join("Faces/", f))]
    faces = []
    for file in files:
        file = file[:-4]
        faces.append(file)
    return faces

def takephhoto():
    cam = VideoCapture(0)
    result, image = cam.read()
    if result:
        imwrite("camoutput.png", image)
        return "Captured"
    else:
        return "Not captured"

def detectfaces():
    photo = takephhoto()
    if photo == "Captured":
        faces = createlistoffaces()
        for face in faces:
            thatface = compareface(face, "camoutput.png")
            if thatface == face:
                print("This is", thatface)
                return thatface
                break
        if thatface == "Unknown":
            print("This face is not recognized. If you want to save this face, say Save my face as your name")
            return "Unknown"
    if photo == "Not captured":
        print("cannot detect")
