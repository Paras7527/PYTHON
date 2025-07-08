import smtplib

mymail = "wildateam123@gmail.com"
passcode = "vlqh ypff vgcn zrvm"  # This must be your actual App Password from Google

# Use correct SMTP server address (typo in your code)
connection = smtplib.SMTP("smtp.gmail.com", 587)  # Use 587 for TLS
connection.starttls()

try:
    connection.login(user=mymail, password=passcode)

    mail_content = "Subject: Trip on this weekend?\n"
    

    connection.sendmail(from_addr=mymail, to_addrs="paraskulkarni123@gmail.com", msg=mail_content)
    print("Email sent successfully!")

except Exception as e:
    print("Something went wrong!!!")
    print("Error:", e)

finally:
    connection.quit()
