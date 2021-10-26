import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("Snapshot was taken!!")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_to_db(img_name):
    access_token="sl.A7F-MMvQjl_-e1GK_Q0WIJtXm5qcKaUd7bpG2mLw3RHSRaqfl5qtRO9qQ7doow-3oaNzk6EXWOrHglb_nyvBl_N2evdD8W_mfm809M8ms1RpckYRfuGj_cWhuEuogIU3UVQOjOo"
    file=img_name
    file_from=file
    file_to="/pics/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name=take_snapshot()
            upload_to_db(name)


main()

