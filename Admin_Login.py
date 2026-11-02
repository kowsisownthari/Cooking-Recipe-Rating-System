#!C:/Users/Home/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb
import cgi
import pymysql
cgitb.enable()
form = cgi.FieldStorage()
con = pymysql.connect(host="localhost", user="root", password="", database="loan")
cur = con.cursor()
print("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Admin Login</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<style>
 body {
    margin: 0;
    padding: 0;
    font-family: 'Roboto condensed', sans-serif;
}
section {
    width: 100%;
    min-height: 100vh;  
    background-image: url('istockphoto-1366800794-612x612.jpg');
    background-size: cover;
    background-position: center; 
    display: flex;  
    align-items: center;  
    justify-content: center; 
}
.login-container {
    width: 100%; 
    max-width: 400px;
    margin: 0 auto;   
    padding: 0 15px;  
}
.login-form {
    width: 100%;     
    background-color: rgba(255, 255, 255, .1);
    padding: 2rem;  
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0, 0, 0, .2);
    backdrop-filter: blur(10px); 
}
    .login-form h1 {
        margin: 0 0 20px;
        color: #fff;
        font-size: 30px;
        text-transform: uppercase;
    }
    .login-form input {
        display: block;
        width: 100%;
        padding: 10px 20px;
        box-sizing: border-box;
        margin-bottom: 20px;
        border-radius: 25px;
        outline: none;
        font-size: 14px;
        letter-spacing: 1px;
        color: #fff;
        border: none;
        background: rgba(255, 255, 255, .1);
        font-family: 'Roboto condensed', sans-serif;
        letter-spacing: 1px;
    }
    .login-form input::placeholder {
        color: white;
    }
    .login-form input[type="submit"] {
        color:white;
        background:#0072ff;
        border:none;
        font-size:16px;
        cursor:pointer;
    }
    .login-form input[type="submit"]:hover {
        background: #005aca;
    }
    .login-form input[type="sub"] {
        color: white;
        background: #0072ff;
        border: none;
        font-size: 16px;
        cursor: pointer;
    }
    .login-form input[type="sub"]:hover {
        background: #005aca;
    }
    .login-form a {
        text-decoration: none;
        color: black;
        text-transform: uppercase;
    }
    .login-form p {
        text-decoration:none;
        color:black;
    }
    .logo {
        color:black;
        font-size:35px;
        padding-left:5px;
        float:left;
        padding-top:20px;
    }
    ul li a {
        text-decoration: none;
        color: white;
        font-weight: bold;
    }
    ul li a:hover {
        color: darkslategrey;
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
</style>
</head>
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
                              <li><a class="dropdown-item" href="Chef_Register.py">Chef</a></li>
                               <li><a class="dropdown-item" href="User_Register.py">User</a></li>
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
<section>
        <div class="login-container">
            <div class="login-form">
                <h1>Admin Sign in</h1>
                <form method="post">
                    <input type="text" name="uname" placeholder="ADMIN ID">
                    <input type="password" name="pass" placeholder="PASSWORD">
                    <input type="submit" name="sub" value="login">
                    <button class="btn btn-primary" onclick="window.location.href='home.py'" style="background-color:red;color:white;width:300px;height:45px;border-radius:25px;">
                    Cancel</button>
                    </form>
            </div>
        </div>
        </section>
<footer class="bg-dark text-light py-4">
    <div class="container">
        <div class="row">
            <div class="col-md-4 mb-4 mb-md-0">
                <img src="download (10).jpeg" style="width:75px;height:75px;border-radius:50px;">
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
        </div>
    </footer>
</body>
</html>""")
Submit = form.getvalue("sub")
if Submit:
    username = form.getvalue("uname")
    password = form.getvalue("pass")
    if (username=="admin@123"):
        if (password =="20010"):
            print("""
                    <script>
                    alert("login success");
                    location.href="admin_dashboard.py"
                    </script>
                    """ )
        else:
            print("""
            </script>
            alert(" wrong password")
            </script>
            """)
    else:
        print("""
        </script>
        alert(" wrong username")
        </script>""")
