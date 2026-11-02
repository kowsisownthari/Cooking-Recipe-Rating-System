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
<title>Share Recipe</title>
 <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/js/all.min.js"></script>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<style>
    .image-row {
        display: flex;
        overflow-x: auto;
        padding-bottom: 40px;
        margin-top: 100px;
        margin-left: 100px;
    }
    .image-box {
        width: 400px;
        height: 450px; 
        position: relative;
        overflow: hidden;
        margin-right: 20px;
        flex-shrink: 0;
        border: 2px solid #ddd;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1); 
    }
    .image-box:last-child {
        margin-right: 0;
    }
    .image-box img {
        width: 100%;
        height: 400px;  
        object-fit: cover;
        transition: transform 0.3s ease;
    }
   
    .hover-button {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    .image-box:hover .hover-button {
        opacity: 1;
    }
    .image-title {
        padding: 10px;
        text-align: center;
        background-color: #f8f9fa;
        border-top: 1px solid #ddd;
    }
          .dropdown-menu li a {
        color: black;
        padding: 12px 16px;
        text-decoration: none;
        display: block;
    }
    .dropdown-menu li a:hover {
        background-color: purple;
        color: white;
    }


    .navbar {
        background: purple;
        backdrop-filter: blur(10px);
    }
</style>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark fixed-top">
    <div class="container">
  <img src="download (10).jpeg" style="width:75px;height:75px;border-radius:50px;">
    
        <a class="navbar-brand" href="#">TasteRate</a>        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link" href="home.py">Home</a>
                </li>
               <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="" id="loginDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Register
                    </a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="Visitor_Register.py">Visitor</a></li>
                        <li><a class="dropdown-item" href="Student_Register.py">Cookery Student</a></li>
                        <li><a class="dropdown-item" href="Chef_Register.py">Chef</a></li>
                    </ul>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="" id="loginDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Login
                    </a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="Visitor_Login.py">Visitor</a></li>
                        <li><a class="dropdown-item" href="Student_Login.py">Cookery Student</a></li>
                        <li><a class="dropdown-item" href="Chef_login.py">Chef</a></li>
                        <li><a class="dropdown-item" href="Admin_Login.py">Login</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</nav><br><br>
    <div class="container-fluid py-5">
           <center> <h2 >Post Your Recipe as</h2></center>

        <div class="image-row">
            <div class="image-box">
                <img src="istockphoto-2048177034-612x612.jpg" alt="Image 1">
                <div class="image-title">
                    <h5>Chef</h5>
                </div>
                <a href="Chef_Register.py" class="btn btn-primary hover-button">Get Started</a>
            </div>
            <div class="image-box">
                <img src="istockphoto-1457611456-612x612.jpg" alt="Image 2">
                <div class="image-title">
                    <h5>Visitor</h5>
                </div>
                <a href="Visitor_Register.py" class="btn btn-primary hover-button">Get Started</a>
            </div>
            <div class="image-box">
                <img src="istockphoto-1386397019-612x612.jpg" alt="Image 3">
                <div class="image-title">
                    <h5>Cookery Student</h5>
                </div>
                <a href="Student_Register.py" class="btn btn-primary hover-button">Get Started</a>
            </div>
        </div>
    </div>   
<footer class="bg-dark text-light py-4">
    <div class="container">
        <div class="row">
            <div class="col-md-4 mb-4 mb-md-0">
                <img src="download (10).jpeg" style="width:75px;height:75px;border-radius:50px;">
            </div>
            <div class="col-md-4 mb-4 mb-md-0">
               <center><h5>TasteRate</h5>
                <p>Discover, share, and rate the best recipes from around the world.</p>
                </div></center>
                <div class="col-md-4">
                      <center> <script>
                var a = new Date();
                var year = a.getFullYear();
                document.write("Copyright claimed @ " + year + ". All rights reserved.");
              </script></center>
                </div>
        </div>
    </footer>

</body>
</html>""")