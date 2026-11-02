#!C:/Users/Home/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb
import cgi
import pymysql
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

cgitb.enable()
form = cgi.FieldStorage()
con = pymysql.connect(host="localhost", user="root", password="", database="rating_system")
cur = con.cursor()

def generate_password():
    return '{:04d}'.format(random.randint(0, 9999))

def send_email(recipient, subject, body):
    sender_email = "kowsisowthari@gmail.com"
    sender_password = "tmvo oloy yner hgbl"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forgot Password</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>
    <div class="container mt-5">
        <h2>Forgot Password</h2>
""")

if "submit" in form:
    email = form.getvalue("email")

    cur.execute("SELECT chefid, admin_status FROM visitor_register WHERE Email = %s", (email,))
    result = cur.fetchone()

    if result:
       chefid_id, admin_status = result
       if admin_status == 'passchanged':
            print("<p class='alert alert-warning'>Your password has been changed by the admin. Please contact the admin for further instructions.</p>")
        else:
            new_password = generate_password()

            cur.execute("UPDATE visitor_register SET password = %s WHERE chefid = %s", (new_password, chefid))
            con.commit()

            if cur.rowcount > 0:
                subject = "Password Reset"
                body = f"Your new password is: {new_password}\nPlease change this password after logging in."
                try:
                    send_email(email, subject, body)
                    print("<p class='alert alert-success'>A new  password has been sent to your email.</p>")
                except Exception as e:
                    print(f"<p class='alert alert-danger'>Failed to send email. Error: {str(e)}</p>")
            else:
                print("<p class='alert alert-danger'>Failed to update password in the database.</p>")
    else:
        print("<p class='alert alert-danger'>Email not found in our records.</p>")

print("""
        <form method="post" enctype="multipart/form-data">
            <div class="mb-3">
                <label for="email" class="form-label">Email address</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            <button type="submit" name="submit" class="btn btn-primary">Reset Password</button>
        </form>
    </div>
</body>
</html>
""")

cur.close()
con.close()