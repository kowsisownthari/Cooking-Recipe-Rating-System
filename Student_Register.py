#!C:/Users/Home/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb
import cgi, smtplib, random
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
<title>Student Register</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<style>
    body {
     background-color:#b2f2d0;
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
        font-size:17px;
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
        background-color: rgb(10, 10, 46);
        color: white;}
    .text {
        color: white;
        font-size: 20px;
        position: absolute;
        top: 50%;
        left: 50%;
        text-align: center;
    }

    .form-group {
        margin-bottom: 1rem;
        width: 60%; 

    }
    .btn-container {
        display: flex;
        justify-content: space-between;
    }
    .btn-container .btn {
        margin: 0 10px;
    }
   .login-form-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 40px; 
       
        border-radius: 20px; 
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); 
        max-width: 800px; 
        margin: 20px auto; 
    }

    .login-form {
        background: #ffffff; 
        border-radius: 15px;
        padding: 30px;
        color: #333; 
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border: 1px solid #e0e0e0; 
    }

    .form-row {
        display: flex;
        gap: 7px; 
        margin-bottom: 8px;
    }

    .form-group {
        flex: 1; 
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
    .form-group input,
    .form-group select {
        width: 100%;
        padding: 8px 12px; 
        box-sizing: border-box;
        border-radius: 12px; 
        border: 1px solid #ccc; 
        background: #f9f9f9; 
        color: #333; 
        font-size: 16px; 

    }

    .form-group input::placeholder {
        color: #888; 
    }

    .form-group input:focus,
    .form-group select:focus {
        border-color: #007bff; 
        background-color: #fff; 
    }

    .form-group input[type="submit"] {
        background-color: #007bff;
        color: white;
        border: none;
        font-size: 16px;
        cursor: pointer;
        padding: 14px 20px;
        border-radius: 12px; 
    }
    .form-group input[type="submit"]:hover {
        background-color: #0056b3; 
    }
    .form-group input[type="reset"] {
        color: white;
        background: #dc3545; 
        border: none;
        font-size: 16px;
        cursor: pointer;
        padding: 14px 20px;
        border-radius: 12px;
      }

    .form-group input[type="reset"]:hover {
        background: #c82333; 
    }
     .login-form option{
         background-color:white;
         color:black
        }
             .login-form p{
          font-family: 'Roboto condensed',sans-serif;
         
        }
  .login-form a{
          font-family: 'Roboto condensed',sans-serif;
          text-decoration:none;
          color:green;
         
        }
</style>
</head>""")
print(f"""
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
<div class="container mt-4">
      <div class="login-form-wrapper">
    <div class="login-form">

            <h4>Student Registration</h4>
            <form method="post" enctype="multipart/form-data">
              <div class="form-row">
                <div class="form-group">
             <input type="text" name="name" id="name" placeholder="Name" required>
             </div>
             <div class="form-group">

                <input type="mail" name="Email" id="Email" placeholder="Email" required ">
               </div></div>
              <div class="form-row">
                <div class="form-group">
                    <input type="mail" name="phno" id="phno" placeholder="Contact Number" required>
                    </div>
                           <div class="form-group">

    <select name="gen" id="gen" class="custom-select"  style="border-radius: 25px;
             margin-bottom: 20px;background-color:white;color: black; margin-top:5px;" required>
      <option value="" disabled selected>Select Your Gender</option>
    <option value="MALE">MALE</option>
    <option value="FEMALE">FEMALE</option></select></div></div>
             
                     <div class="form-row" style="margin-top:-35px;">
                <div class="form-group" >
                <p >Date Of Birth:</p>
                    <input type="date" name="birth" id="birth" ></div>
         
             <div class="form-group">
             <p>Address:</p>
              <input type="text" name="no" id="no" placeholder="Door No">
             </div></div>
     <div class="form-row">
    <div class="form-group">
             <input type="text" name="add1" placeholder="Address Line 1"></div>
                <div class="form-group">
              <input type="text" name="add2" placeholder="Address Line 2"></div></div>
             <div class="form-row">
    <div class="form-group">
                    <input type="text" name="city" placeholder="City"></div>
                <div class="form-group">
                    <input type="text" name="State" placeholder="State"></div></div>
                     <div class="form-row">
                    <div class="form-group">
                    <input type="text" name="Country" placeholder="Country"></div>
                <div class="form-group">
                      <input type="text" id="Rname" name="Rname" placeholder="Restaurant/Institution Name" required>
                    </div></div>
     <div class="form-row">
      <div class="form-group">
                     <select name="Type" id="Type" class="custom-select"  style="border-radius: 25px;
            margin-bottom: 20px;background-color:white;color: black; ">

        <option value="" disabled selected>Select Training Type</option>
        <option value="Baking">Baking</option>
        <option value="Grilling">Grilling</option>
        <option value="Sautéing">Sauteing</option>
        <option value="Food Presentation">Food Presentation</option>
        <option value="Pastry Making">Pastry Making</option>
        <option value="Butchery">Butchery</option>
        <option value="Sauce Making">Sauce Making</option>
        <option value="Plating">Plating</option>
        <option value="Knife Skills">Knife Skills</option>
        <option value="Food Safety">Food Safety</option>
        <option value="Other">Other</option>
    </select>
                    </div>
                <div class="form-group">
     <input type="mail" name="Period" id="Period" placeholder="Enter Training Period" required>
</div></div>
  <div class="form-row">
  <div class="form-group">
              <input type="mail" name="Location" id="Location" placeholder="Enter Location" required>
            </div>

   <div class="form-group" >
     <div class="col-lg-12 col-xs-12">
  <label for="id-upload" class="required-field">Upload ID Proof(Aadhar card/Passport):</label>
  <input type="file" class="form-control" id="IDProof" name="IDProof" multiple ></div></div></div>

      <div class="form-row">
                <div class="form-group">
       <div class="col-lg-12 col-xs-12">
  <label for="id-upload" class="required-field">Upload Profile Picture</label>
  <input type="file" class="form-control" id="profile" name="profile"></div></div>
   <div class="form-group">
   <label for="id-upload" class="required-field">Upload ID Card:</label>
  <input type="file" class="form-control" id="IDCard" name="IDCard" multiple ></div></div>
    <div class="form-row">
                <div class="form-group">
 <input type="submit" name="sub" value="Submit" style="background-color:blue;color:white;" ></div>
    <div class="form-group">
                    <button class="btn btn-primary" onclick="window.location.href='home.py'" style="background-color:red;color:white;width:300px;height:50px;">
                     Cancel
                        </button>
                    <br>
                    <br>
                     <p>Have an account already? <a href="Student_Login.py">Login</a></p>
                    </form>
                </div></div></div>

        </div>
    </div>
</div> </div>
</div>

<footer class="bg-dark text-light py-4">
    <div class="container">
        <div class="row">
            <div class="col-md-4 mb-4 mb-md-0">
                <img src="download (10).jpeg" style="width:75px;height:75px;border-radius:50px;">

                
            </div>
            <div class="col-md-4 mb-4 mb-md-0">
               <center><h5>TasteRate</h5>
                <p>Discover, share, and rate the best recipes from around the world.</p></center>
                </div>
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
</html>
""")
submit = form.getvalue("sub")
if submit != None:
        if len(form) != 0:
            Img = form['IDProof']
            Img1 = form['profile']
            Img2 = form['IDCard']
            if Img.filename and Img1.filename and Img2.filename:
                pi = os.path.basename(Img.filename)
                open("Student_Images/" + pi, "wb").write(Img.file.read())
                si = os.path.basename(Img1.filename)
                open("Student_Images/" + si, "wb").write(Img1.file.read())
                ai = os.path.basename(Img2.filename)
                open("Student_Images/" + ai, "wb").write(Img2.file.read())
                Name = form.getvalue("name")
                Email = form.getvalue("Email")
                phno = form.getvalue("phno")
                gender = form.getvalue("gen")
                DOB = form.getvalue("birth")
                Doorno = form.getvalue("no")
                Address1 = form.getvalue("add1")
                Address2 = form.getvalue("add2")
                city = form.getvalue("city")
                state = form.getvalue("State")
                country = form.getvalue("Country")
                Restaurant = form.getvalue("Rname")
                TrainingType = form.getvalue("Type")
                TrainingPeriod = form.getvalue("Period")
                Location = form.getvalue("Location")
                q = """insert into Student_register(Name,Email,phno,gender,DOB,Doorno, Address1,Address2, city,state,country,Restaurant,TrainingType,TrainingPeriod,Location,IDProof,profile,IDCard,status,designation) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','registered','student')""" % (Name,Email,phno,DOB,gender,Doorno, Address1,Address2, city,state,country,Restaurant,TrainingType,TrainingPeriod,Location,pi,si,ai)
                cur.execute(q)
                con.commit()

