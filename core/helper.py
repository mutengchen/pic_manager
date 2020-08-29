import os

import cv2
import numpy as np
from PIL.Image import Image
from flask import url_for
from core.settings import Setting as ST
BASEDIR = 'tmp'

def save_tmp_img(buf,cameraname):
    img = cv2.imdecode(np.asarray(bytearray(buf),dtype='uint8'),cv2.IMREAD_COLOR)
    imgname = f"{cameraname}.jpg"
    path = os.path.join(ST.SERVERSTATICROOT, BASEDIR, imgname)
    cv2.imwrite(path,img,[cv2.IMWRITE_JPEG_QUALITY,60])
    return url_for('static', filename=f"{BASEDIR}/{imgname}")

