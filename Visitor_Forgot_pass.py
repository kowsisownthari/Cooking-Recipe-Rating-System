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
    <title>Visitor Forgot Password</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</head>
<style>
    .title{
        text-align: center;
        padding: 50px 0 20px;
    }
    .title h2{
        margin: 0;
        padding: 0;
        color: #262626;
        font-size: 36px;
    }
    .navbar {
        background-color:#004c4c;
        padding: 1rem;
    }
    .navbar-brand {
        color: #fff;
        font-size: 1.8rem;
        font-weight: bold;
    }
    .navbar-nav .nav-link {
        color: white;
        font-size: 1.1rem;
        padding: 0.75rem 1.25rem;
        transition: color 0.3s;
    }
    .navbar-nav .nav-link:hover {
       color:blue;
    }
    .dropdown-menu li a {
        color: black;
        padding: 12px 16px;
        text-decoration: none;
        display: block;
    }
    .dropdown-menu li a:hover {
        background-color: darkslategrey;
        color: white;
    }
    .logo {
        color: black;
        font-size: 35px;
        padding-left: 5px;
        float: left;
        padding-top: 20px;
    }
    ul li a {
        text-decoration: none;
        color: white;
        font-weight: bold;
    }
    ul li a:hover {
        color: darkslategrey;
    }
    .content {
        width: 100%;
        height: auto;
        color: black;
        position: relative;
        text-align: center;
    }
    .content h3 {
        font-size: 50px;
        margin-top: 20%;
        letter-spacing: 2px;
        color: white;
    }
    .cn, .cn1 {
        width: 160px;
        height: 40px;
        border: none;
        margin-bottom: 10px;
        font-size: 18px;
        border-radius: 10px;
        cursor: pointer;
        display: inline-block;
        text-align: center;
        line-height: 40px;
        background-color: darkslategrey;
        text-decoration: none;
        color: white;
    }
    .content a {
        text-decoration: none;
        color: white;
        transition: .4s ease;
    }
    .cn:hover {
        background-color: black;
        color: white;
    }
    .cn1:hover {
        background-color: black;
        color: white;
        text-decoration: none;
    }
    .img-container {
        display: flex;
        justify-content: space-around;
    }
    .img, .img1 {
        position: relative;
        width: 48%;
    }
    .image {
        display: block;
        width: 100%;
        height: auto;
    }
    .overlay {
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        height: 100%;
        width: 100%;
        opacity: 0;
        transition: .5s ease;
        background-color: grey;
    }
    .img:hover .overlay, .img1:hover .overlay {
        opacity: 1;
    }
    .text {
        color: white;
        font-size: 20px;
        position: absolute;
        top: 50%;
        left: 50%;
        text-align: center;
    }
    .btn-container {
        display: flex;
        justify-content: space-between;
    }
    .btn-container .btn {
        margin: 0 10px;
    }
    .box-form a {
        text-decoration: none;
        color: black;
        text-transform: uppercase;
    }
    .box-form p {
        text-decoration: none;
        color: black;
    }
    .form-container {
        background-color: #81b8e8;  
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
        max-width: 400px;
        margin: 0 auto;
    }
</style>

<body>
<nav class="navbar navbar-expand-lg">
    <img src="download (10).jpeg" style="width:75px;height:75px;border-radius:50px;">
    <a class="navbar-brand" href="#">TasteRate</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
            <li class="nav-item">
                <a class="nav-link" href="home.py">Home</a>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="registerDropdown" data-bs-toggle="dropdown">Register</a>
                <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="Student_Register.py">Student</a></li>
                    <li><a class="dropdown-item" href="Visitor_Register.py">Visitor</a></li>
                    <li><a class="dropdown-item" href="Chef_Register.py">Chef</a></li>
                </ul>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="loginDropdown" data-bs-toggle="dropdown">Login</a>
                <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="Student_Login.py">Student</a></li>
                    <li><a class="dropdown-item" href="Visitor_Login.py">Visitor</a></li>
                    <li><a class="dropdown-item" href="Chef_Login.py">Chef</a></li>
                    <li><a class="dropdown-item" href="Admin_Login.py">Admin</a></li>
                </ul>
            </li>
        </ul>
    </div>
</nav>
    <div class="form-container" style="margin-top:100px;">

<div class="container mt-5">
    <center><h4>Forgot Password</h4></center>
""")

if "submit" in form:
    email = form.getvalue("email")

    cur.execute("SELECT id, admin_status FROM visitor_register WHERE Email = %s", (email,))
    result = cur.fetchone()

    if result:
        student_id, admin_status = result
        if admin_status == 'passchanged':
            print("<p class='alert alert-warning'>Your password has been changed by the admin. Please contact the admin for further instructions.</p>")
        else:
            new_password = generate_password()

            cur.execute("UPDATE visitor_register SET password = %s WHERE id = %s", (new_password, student_id))
            con.commit()

            if cur.rowcount > 0:
                subject = "Password Reset"
                body = f"Your new password is: {new_password}\nPlease change this password after logging in."
                try:
                    send_email(email, subject, body)
                    print("<p class='alert alert-success'>A new password has been sent to your email.</p>")
                except Exception as e:
                    print(f"<p class='alert alert-danger'>Failed to send email. Error: {str(e)}</p>")
            else:
                print("<p class='alert alert-danger'>Failed to update password in the database.</p>")
    else:
        print("<p class='alert alert-danger'>Email not found in our records.</p>")

print("""
        <form method="post" enctype="multipart/form-data">
            <div class="mb-3">
                <input type="email" class="form-control" id="email" name="email" required placeholder="EMAIL" style="width:100%">
            </div>
            <center><button type="submit" name="submit" class="btn btn-primary">Reset Password</button></center>
        </form>
    </div>
</div>
<footer style="margin-top:180px;">
    <footer class="bg-dark text-light py-4">
        <div class="row">
            <div class="col-md-4 mb-4 mb-md-0">
                <center><img src="download (10).jpeg" style="width:75px;height:75px;border-radius:50px;"></center>
            </div>
            <div class="col-md-4 mb-4 mb-md-0">
                <h5>TasteRate</h5>
                <p>Discover, share, and rate the best recipes from around the world.</p>
            </div>
            <div class="col-md-4">
                <center>
                    <script>
                        var a = new Date();
                        var year = a.getFullYear();
                        document.write("Copyright claimed @ " + year + ". All rights reserved.");
                    </script>
                </center>
            </div>
        </div>
    </footer>
</footer>
</body>
</html>
""")

cur.close()
con.close()