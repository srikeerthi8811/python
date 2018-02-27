import smtplib
S=smtplib.SMTP("smtp.gmail.com",587)
S.starttls()
S.login("srikeerthi8811@gmail.com","9986663774")
msg="hai how are you"
S.sendmail("srikeerthi8811@gmail.com","srikeerthi8811@gmail.com",msg)
print("sucess")
S.quit()
