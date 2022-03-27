from email.mime.text import MIMEText
import smtplib





print("[1] Option 1 MailSpammer")
print("[2] Option 2 Not available")
print("[0] Exit the script.")

option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        user = input("Enter your email address: ")
        password = input('Enter the password of your email address: ')
        receiver = input("Enter the email address of your victim: ")
        smtb = input("Specify the SMTP server: ")
        port = input("Enter the port: ")
        text = input("Enter the text of your email: ")
        amount = int(input("How many emails should be sent: "))





        for element in range(amount):
            sender = user
            receiver = receiver

            msg = MIMEText(text)

            msg['From'] = user
            msg['To'] = receiver


            with smtplib.SMTP(smtb, port) as server:
                server.starttls()

                server.login(user, password)
                server.sendmail(sender, receiver, msg.as_string())
            print("mail successfully sent")

    elif option == 2:
        print("Not available")
    else:
        print("quit")
    print()
    menu()
    option = int(input("Enter your option: "))
print("Thanks for using the script")
