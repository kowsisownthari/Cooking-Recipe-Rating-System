#!C:/Users/Home/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb
import cgi
import pymysql, os

cgitb.enable()
form = cgi.FieldStorage()
con = pymysql.connect(host="localhost", user="root", password="", database="rating_system")
cur = con.cursor()
print("""

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Visitor Login</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<style>
    body {

       margin:0;
       padding: 0;
       background-image: url('istockphoto-1463371608-612x612.jpg');

       background-size: cover;
       font-family: sans-serif;
    }
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
 .container {
    width: 400px; 
    height: 20px; 
    background: #fff;
    margin: 0 auto;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 60vh; 
    box-shadow: 0 15px 40px rgba(0,0,0,.5);
}
.box {
    width: 90%;
    max-width: 550px; 
    box-sizing: border-box;
}
  .box-form input{
        margin-bottom: 20px;
        width:100%;
    }
    .box-form input[type="text"], .box-form input[type="password"]{
border: none;
border-bottom: 2px solid #a6af13;
outline:none;
height:40px;
    }
    .box-form input[type="text"]:hover, .box-form input[type="password"]:hover{
        color: #262626;
    }
    .box-form input[type="submit"]{
        border: none;
        outline: none;
height: 40px;
color: #fff;
background: blue;
cursor:pointer;
    }
    .

    .box-form a{
        text-decoration: none;
        font-size: 12px;
        color: #262626;
        font-weight: bold;
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
</style>
</head>
<body>
<nav class="navbar navbar-expand-lg">

  <img src="download (10).jpeg" style="width:75px;height:75px;border-radius:50px;">
    
        <a class="navbar-brand" href="#">TasteRate</a>             <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
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
        </div>
    </nav>
<div class="title"><h2>Visitor Sign in</h2></div>
<div class="container">

<div class="box">
    <div class="box-form">
        <form method="post" enctype="multipart/form-data">
            <input type="text" name="Email" placeholder="EMAIL">
            <input type="password" name="pass" placeholder="PASSWORD"><br>
            <input type="submit" name="sub" value="sign in">
    <input type="button" value="Cancel" onclick="window.location.href='home.py'" style="background-color:red;color:white;width:335px;height:40px;border:none;">
     <p>Don't have an account? <a href="Visitor_Register.py" style="color:blue">Register</a><br>
                  <center>  <a href="Visitor_Forgot_pass.py">Forgot password</a></center>
    </div>
</div>

</div><br><<br>
<footer>
<footer class="bg-dark text-light py-4">
        <div class="row">
            <div class="col-md-4 mb-4 mb-md-0">
               <center> <img src="download (10).jpeg" style="width:75px;height:75px;border-radius:50px;">

                </center>
            </div>
            <div class="col-md-4 mb-4 mb-md-0">
               <h5>TasteRate</h5>
                <p>Discover, share, and rate the best recipes from around the world.</p>
                </div>
                <div class="col-md-4">
                      <center>  <script>
                var a = new Date();
                var year = a.getFullYear();
                document.write("Copyright claimed @ " + year + ". All rights reserved.");
              </script>   </center>
                </div>
            </div>
           
        </div>
    </footer>

</body>
</html>
      """)

submit = form.getvalue("sub")
if submit is not None:
    Email = form.getvalue("Email")
    password = form.getvalue("pass")
    q = """SELECT id, admin_status FROM visitor_register WHERE Email=%s AND password=%s"""
    cur.execute(q, (Email, password))
    det = cur.fetchone()
    if det is not None:
        if det[1] == 'passchanged':
            print("""
            <script>
            alert("Your password has been changed by the admin. Please contact the admin for further instructions.");
            </script>
            """)
        else:
            print("""  
            <script>
            alert("Login successful");
            location.href ="Visitor_Dashboard.py?id=%s";
            </script>
            """ % (det[0]))
    else:
        print("""
        <script>
        alert("Incorrect username or password");
        </script>
        """)
