#!C:/Users/Home/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type: text/html\r\n\r\n")
import cgitb, os
import cgi
import pymysql

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="rating_system")
cur = con.cursor()
form = cgi.FieldStorage()
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Login</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <style>
       body {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    justify-content: space-between;
    margin: 0;
    background-color: #f4f4f9;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.container {
    flex-grow: 1;
    display: flex;
    flex-wrap: wrap;
    width: min(900px, 95%);
    background-color: transparent;
    box-shadow: none;
    border-radius: 15px;
    margin: 100px auto;
    gap: 20px;
    padding: 10px;
}

.left-img {
    flex: 1 1 300px;
    min-width: 300px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
    border-radius: 15px;
    overflow: hidden;
    background-color: #fff;
}

.left-img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.login-card {
    flex: 1 1 300px;
    min-width: 300px;
    padding: 40px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-shadow: 0px 0px 10px grey;
    background-color: #fff;
    border-radius: 15px;
}       
        .login-card h2 {
            text-align: center;
            margin-bottom: 20px;
            color: #333;
        }
        .input-group {
            margin-bottom: 20px;
        }
        .input-group label {
            display: block;
            font-weight: bold;
            color: #555;
        }
        .input-group input {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 8px;
            margin-top: 5px;
            font-size: 16px;
        }
        .login-btn {
            width: 100%;
            padding: 12px;
            border: none;
            border-radius: 8px;
            background-color: #5a67d8;
            color: white;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .login-btn:hover {
            background-color: #4c51bf;
        }
       
    
            .navbar img {
    width: 60px;
   background-color: transparent;
    border-radius: 25px;
    padding: 5px;
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
     .login-card a {
        text-decoration: none;
        color: black;
        text-transform: uppercase;
    }
    .login-card p {
        text-decoration: none;
        color: black;
    }
    </style>
</head>
<body>
 <nav class="navbar navbar-expand-lg">

  <img src="download (10).jpeg" style="width:75px;height:75px;border-radius:50px;">
    
        <a class="navbar-brand" href="#">TasteRate</a>            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
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
<div class="container">
    <div class="login-card">
        <h2>Student Login</h2>
        <form action="" method="post">
            <div class="input-group">
                <input type="text" id="student_id" name="student_id" placeholder="StudentId" required>
            </div>
            <div class="input-group">
                <input type="password" id="pass" name="pass" placeholder="Password" required>
            </div>
            <input type="submit" class="login-btn" value="Login" name="sub"><center><br>
                                <button class="btn btn-primary" onclick="window.location.href='home.py'" style="background-color:red;color:white;width:350px;height:45px;">
Cancel</button>
            <br>
             <p>Don't have an account? <a href="Student_Register.py" style="color:blue">Register</a><br><br>
                    <a href="Student_Forgot_pass.py">Forgot password</a></center>
        </form>
    </div>
     <div class="left-img">
        <img src="istockphoto-1394055240-612x612.jpg" alt="Left Image">
    </div>
</div>
<br><br>
<footer class="bg-dark text-light py-4">
        <div class="row">
            <div class="col-md-4 mb-4 mb-md-0">
               <center> <img src="download (10).jpeg" style="width:75px;height:75px;border-radius:50px;"></center>

                
            </div>
            <div class="col-md-4 mb-4 mb-md-0">
               <center><h5>TasteRate</h5>
                <p>Discover, share, and rate the best recipes from around the world.</p>
                </div></center>
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
    cookery_id = form.getvalue("student_id")
    password = form.getvalue("pass")
    q = """SELECT id, admin_status FROM student_register WHERE cookery_id=%s AND password=%s"""
    cur.execute(q, (cookery_id, password))
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
            location.href ="CookeryStudent_Dashboard.py?id=%s";
            </script>
            """ % (det[0]))
    else:
        print("""
        <script>
        alert("Incorrect username or password");
        </script>
        """)