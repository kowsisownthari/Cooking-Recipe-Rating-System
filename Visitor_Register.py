#!C:/Users/Home/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb
import cgi
import pymysql,os
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
<title>Visitor Register</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<style>
 body {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    margin: 0;
    padding: 0;
    font-family: 'Roboto condensed', sans-serif;
}
section {
    flex: 1;
    width: 100%;
    min-height: max-content;
    background-image: url('login.jpg');
    background-size: cover;
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
    padding: 40px 5%;
}
footer {
    margin-top: auto;  
}
.login-container {
    width: 100%;
    text-align: center;
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;

max-width: min(700px, 90%); 
    margin: 0 auto; 
      background-color: #00251a;
}

.login-form {
    position: relative;
    box-sizing: border-box;
  padding: 40px 5%;    transform: .5s;
    background-color: rgba(255, 255, 255, .1);
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0, 0, 0, .2);
    width: 100%;
}

    .login-form h1 {
        margin: 0 0 20px;
        color: #fff;
        font-size: 30px;
        text-transform: uppercase;
    }
    .login-form input,select {
        display: block;
         width: 100%;
    max-width: 100%;
    padding: 10px 4%;
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
    .login-form div[style*="display: flex"] {
    flex-wrap: wrap;
    gap: 20px;
}

.login-form div[style*="display: flex"] > div {
    flex: 1 1 250px;
}
    .login-form input::placeholder {
        color: white;
    }
    .login-form input[type="submit"] {
        color: white;
        background: #0072ff;
        border: none;
        font-size: 16px;
        cursor: pointer;
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
        text-decoration: none;
        color: black;
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
     .login-form option{
         background-color:white;
         color:black
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
<section>
        <div class="login-container">
            <div class="login-form">
                <h1>Visitor Register</h1>
               <form method="post" enctype="multipart/form-data">
    <input type="text" id="fullname" name="fullname" placeholder="Full Name" required>
    <input type="email" id="email" name="email" placeholder="Email" required>
    <input type="number" id="phone" name="phone" placeholder="Phone Number" required>
    
    <label for="Date of birth" style="margin-right:70vh;color:white;">Date Of Birth:</label>
    <input type="date" name="DOB" id="DOB">
    
    <select name="gen" id="gen" class="custom-select" style="border-radius: 25px; margin-bottom: 20px;background-color:transparent;color: white; margin-top:23px;" required>
        <option value="" disabled selected>Select Your Gender</option>
        <option value="MALE">MALE</option>
        <option value="FEMALE">FEMALE</option>
    </select>
    
  <p style="margin-right:520px;color:white">Address:</p>
    <div style="display: flex; justify-content: space-between;">
        <div style="width: 48%;">
            <input type="text" name="no" id="no" placeholder="Door No">
            <input type="text" name="add1" placeholder="Address Line 1">
        </div>
        <div style="width: 48%;">
            <input type="text" name="add2" placeholder="Address Line 2">
            <input type="text" name="State" placeholder="State">
        </div>
    </div>
    <div style="display: flex; justify-content: space-between;">
        <div style="width: 48%;">
            <input type="text" name="city" placeholder="City">
        </div>
        <div style="width: 48%;">
            <input type="text" name="Country" placeholder="Country">
        </div>
    </div>


    <select id="work-sector" name="worksector">
        <option value="" disabled selected>Select Profession</option>
        <option value="it">Information Technology (IT)</option>
        <option value="healthcare">Healthcare</option>
        <option value="education">Education</option>
        <option value="agriculture">Agriculture</option>
        <option value="manufacturing">Manufacturing</option>
        <option value="construction">Construction</option>
        <option value="finance">Finance & Banking</option>
        <option value="retail">Retail & E-commerce</option>
        <option value="Other">Other</option>
    </select>
    
    <select name="cuisine" id="cuisine" required>
        <option value="" disabled selected>Prefered Cuisine</option>
        <option value="Italian">Italian</option>
        <option value="Indian">Indian</option>
        <option value="Chinese">Chinese</option>
        <option value="Mexican">Mexican</option>
        <option value="French">French</option>
        <option value="Other">Other</option>
    </select>
               
    <input type="password" name="password" placeholder="Password">
            
    <div style="display: flex; justify-content: space-between;">
        <div style="width: 48%;">
            <label for="id-upload" class="required-field" style="color:white;">Upload ID Proof:</label>
            <input type="file" class="form-control" id="id-upload" name="IDProof" multiple>
        </div>
        <div style="width: 48%;">
            <label for="profile-upload" class="required-field" style="color:white;">Upload Profile picture:</label>
            <input type="file" class="form-control" id="profile-upload" name="profile" multiple>
        </div>
    </div>

    <input type="submit" name="sub" value="Submit" style="background-color:blue;color:white;">
    <button class="btn btn-primary" onclick="window.location.href='home.py'" style="background-color:red;color:white;width:90%;max-width:650px;height:40px;border-radius:25px;">Cancel</button>
<br><br>
    <p style="color:white;">Already having an account? <a href="Visitor_Login.py" style="color:Blue">Login</a></p>
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
               <center><h5>TasteRate</h5>
                <p>Discover, share, and rate the best recipes from around the world.</p>
                </div></center>
                <div class="col-md-4">
                      <script>
                var a = new Date();
                var year = a.getFullYear();
                document.write("Copyright claimed @ " + year + ". All rights reserved.");
              </script>  
                </div>
            </div>
          
        </div>
    </footer>

</body>
</html>""")
submit = form.getvalue("sub")
if submit != None:
        if len(form) != 0:
            Img = form['IDProof']
            Img1 = form['profile']
            if Img.filename and Img1.filename:
                pi = os.path.basename(Img.filename)
                open("Visitor_Images/" + pi, "wb").write(Img.file.read())
                si = os.path.basename(Img1.filename)
                open("Visitor_Images/" + si, "wb").write(Img1.file.read())
                Name = form.getvalue("fullname")
                Email = form.getvalue("email")
                phno = form.getvalue("phone")
                DOB = form.getvalue("DOB")
                gender = form.getvalue("gen")
                Doorno = form.getvalue("no")
                Address1 = form.getvalue("add1")
                Address2 = form.getvalue("add2")
                city = form.getvalue("city")
                state = form.getvalue("State")
                country = form.getvalue("Country")
                worksector= form.getvalue("worksector")
                cuisine = form.getvalue("cuisine")
                password = form.getvalue("password")
                q = """insert into visitor_register(Name,Email,phno,DOB,gender,Doorno, Address1,Address2, city,state,country,worksector,cuisine,password,IDProof,profile,designation) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','visitor')""" %(Name,Email,phno,gender,DOB,Doorno,Address1,Address2,city,state,country,worksector,cuisine,password,pi,si)
                cur.execute(q)
                con.commit()
                print("""
                   <script>
                   alert("Registered Successfully");
                   </script>
                   """)