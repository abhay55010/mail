import smtplib
content='this is mail from python'
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('#############@gmail.com','###################')
mail.sendmail('################@gmail.com','#################@gmail.com',content)
mail.close()
