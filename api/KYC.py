import cv2
import pytesseract
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def display_img(cvImg):
    cvImg = cv2.cvtColor(cvImg, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(10, 8))
    plt.imshow(cvImg)
    plt.axis('off')
    plt.show()


def cropImageRoi(image, roi):
    roi_cropped = image[roi[1]: roi[3], roi[0]: roi[2]]
    return roi_cropped


def preprocessing_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.multiply(gray, 1.95)


def extractDtaFromID(imgF, imgB):
    rois = {
        "name": (390, 250, 700, 315),
        "dob": (790, 300, 1070, 380),
        "gender": (540, 370, 700, 440),
        "address": (635, 220, 1245, 440)
    }
    data = {}
    for key, roi in rois.items():
        if key != 'address':
            crop_img = cropImageRoi(imgF, roi)
        else:
            crop_img = cropImageRoi(imgB, roi)

        crop_img = preprocessing_image(crop_img)
        if key == 'dob':
            text = pytesseract.image_to_string(crop_img, config='--oem 1 --psm 6')[:-1]
            data[key] = datetime.strptime(text, "%d/%m/%Y").date()
        else:
            data[key] = pytesseract.image_to_string(crop_img, config='--oem 1 --psm 6')[:-1]

    return data


def createFinalImage(img2, baseImg):
    baseH, baseW, baseC = baseImg.shape
    orb = cv2.ORB_create(5000)

    kp, des = orb.detectAndCompute(baseImg, None)

    kp1, des1 = orb.detectAndCompute(img2, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = list(bf.match(des1, des))

    matches.sort(key=lambda x: x.distance)
    best_matches = matches[:int(len(matches) * 0.3)]

    srcPoints = np.float32([kp1[m.queryIdx].pt for m in best_matches]).reshape(-1, 1, 2)
    dstPoints = np.float32([kp[m.trainIdx].pt for m in best_matches]).reshape(-1, 1, 2)

    matrix_relationship, _ = cv2.findHomography(srcPoints, dstPoints, cv2.RANSAC, 5.0)

    imgfinal = cv2.warpPerspective(img2, matrix_relationship, (baseW, baseH))

    return imgfinal


def do_kyc(User):
    baseImgF = cv2.imread('/home/manav/PycharmProjects/djangoAPI/UserID_front/baseFront.jpg')
    baseImgB = cv2.imread('/home/manav/PycharmProjects/djangoAPI/UserID_back/baseBack.jpg')

    idFront = User.idImageFront
    idBack = User.idImageBack

    img2F = cv2.imread('%s' % idFront)
    img2B = cv2.imread('%s' % idBack)

    finalimgF = createFinalImage(img2F, baseImgF)
    finalimgB = createFinalImage(img2B, baseImgB)

    user_data = extractDtaFromID(finalimgF, finalimgB)

    name_verified = False
    dob_verified = False
    gender_verified = False

    name_from_data = user_data['name']
    nameSample = [User.firstName, User.middleName, User.lastName]
    name = []
    for i in nameSample:
        if i != '':
            name.append(i)

    name = ' '.join(name)

    if name.lower() == name_from_data.lower():
        name_verified = True

    print(type(user_data['dob']))
    print(user_data['dob'])
    print(User.dob)
    if User.dob == user_data['dob']:
        dob_verified = True

    if User.gender.lower() == user_data['gender'].lower():
        gender_verified = True

    if name_verified and dob_verified and gender_verified:
        User.kycVerified = True
    return {
        'contactNo': User.contactNo,
        'kycVerified': User.kycVerified,
        'nameVerified': name_verified,
        'genderVerified': gender_verified,
        'dobVerified': dob_verified
    }
