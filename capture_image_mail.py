print("Do you want to take ur photo: ")
a=int(input("press 1 for yes and 2 for no"))
if a==1:
    
    import numpy as np
    import cv2
    cam=cv2.VideoCapture(0)
    print('press q to capture photo')
    while True:
        return_value,img=cam.read()
        gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imshow("cam-test",gray)
        if cv2.waitKey(1) & 0XFF ==ord('q'):
            cv2.imwrite('image.jpg',img)
            break
    cam.release()
    cv2.destroyAllWindows()
else:
    print("exit")

print("Do you want to send  ur photo using mail : ")
b=int(input("press 1 for yes and 2 for no"))
if b==1:
    import smtplib
    import imghdr
    import os
    from email.message import EmailMessage

    EMAIL_ADDRESS=os.environ.get('#############@gmail.com')
    EMAIL_PASSWORD=os.environ.get('##############')
    msg=EmailMessage()
    msg['Subjecct']='this is for image'
    msg['From']=EMAIL_ADDRESS
    msg['To']='##############@gmail.com'
    msg.set_content('image attached')
    with open('image.jpg','rb')as f:
              file_data=f.read()
              file_type=imghdr.what(f.name)
              file_name=f.name
              
    msg.add_attachment(file_data,maintype='image',subtype='file_type',filename=file_name)
    with smtplib.SMTP_SSL('smtp.gmail.com',465)as smtp:
        smtp.login('###################@gmail.com','######################')
        smtp.send_message(msg)

else:
    print("exit")

print('mail has sent')        



