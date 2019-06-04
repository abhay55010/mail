print("Do you want to take ur video: ")
a=int(input("press 1 for yes and 2 for no"))
if a==1:
    
    import cv2
    import numpy as np
    cap=cv2.VideoCapture(0)
    fourcc=cv2.VideoWriter_fourcc(*'XVid')
    out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
    while True:
        ret,frame=cap.read()
        gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        out.write(frame)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    out.release()
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

    EMAIL_ADDRESS=os.environ.get('###############@gmail.com')
    EMAIL_PASSWORD=os.environ.get('##################')
    msg=EmailMessage()
    msg['Subjecct']='this is for image'
    msg['From']=EMAIL_ADDRESS
    msg['To']='##################@gmail.com'
    msg.set_content('image attached')
    with open('output.avi','rb')as f:
              file_data=f.read()
              file_type=imghdr.what(f.name)
              file_name=f.name
              
    msg.add_attachment(file_data,maintype='video',subtype='file_type',filename=file_name)
    with smtplib.SMTP_SSL('smtp.gmail.com',465)as smtp:
        smtp.login('###################@gmail.com','##############')
        smtp.send_message(msg)

else:
    print("exit")

print('mail has sent')        



