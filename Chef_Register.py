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
<title>Chef Register</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<style>
    body {

        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-color:rgb(217, 220, 224);
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

    .text {
        color: white;
        font-size: 20px;
        position: absolute;
        top: 50%;
        left: 50%;
        text-align: center;
    }
   .container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.left-box, .right-box {
    flex: 1 1 300px; 
    margin: 10px;
    max-width: 800px;
    max-height: 1300px;
}


    .right-box {
        background-color: rgb(10, 26, 7);
        color: white;
        width:1000px;
    }
    .left-box {
        background-color: white;
        color: black;
        text-align: center;
        margin-top: 10px;

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

    .login-form{
position: relative;
box-sizing: border-box;
padding: 60px 30px;
transform: .5s;
        }
        .login-form:hover{
background-color: rgba(255,255,255,.1);
box-shadow: 0 0 20px rgba(0,0,0,.2);
        }
        .login-form h1{
            margin:0 0 20px;
            color: #fff;
            font-size: 20px;
            text-transform: uppercase;
        }
        .login-form input,select{
            display: block;
            width:100%;
            padding:10px 20px;
            box-sizing: border-box;
            margin-bottom: 20px;
           border-radius: 25px;
           outline: none;
           font-size: 14px;
           letter-spacing: 1px;
           color: #fff;
           border: none;
           background: rgba(255,255,255,.1);
           font-family: 'Roboto condensed',sans-serif;
           letter-spacing: 1px;
        }
        .login-form input::placeholder{
            color: white;
        }
        .login-form input[type="sub"]{
            color: white;
            background: #0072ff;
            border: none;
            font-size: 16px;
            cursor:pointer;

        }
        .login-form input[type="sub"]:hover{
            background: #005aca;
        }
         .login-form input[type="can"]{
            color: white;
            background: #0072ff;
            border: none;
            font-size: 16px;
            cursor:pointer;}
 .login-container{
            position:absolute;
            top:50%;
            left:50%;
            transform: translate(-50%,-50%);
            width:340px;
            text-align: center;
            height:500px;
        }

        .login-form input[type="can"]:hover{
            background: #005aca;
        }
        .login-form a{
            text-decoration: none;
            color:#0072ff;
            text-transform: uppercase;
        }
        .login-form h2,h4{
            text-transform: uppercase;
              font-family: 'Roboto condensed',sans-serif;
        }
        .login-form p{
          font-family: 'Roboto condensed',sans-serif;
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
<div class="container mt-4">
    <div class="row">
   

        <div class="col-md-6 col-sm-12 right-box">

         <div class="login-form">
            <center><h4>Chef Registration</h4></center>
            <form method="post" enctype="multipart/form-data">
               <input type="text" id="full_name" name="full_name" placeholder="Full Name" required>
                    <input type="email" id="email" name="email" placeholder="Email" required>

     <input type="number" id="phone" name="phone" placeholder="Phone Number" required>
     
   <label for="Date of birth">DATE OF BIRTH:</label>
                    <input type="date" name="DOB" id="DOB" >
                     <select name="gen" id="gen" class="custom-select"  style="border-radius: 25px;
             margin-bottom: 20px;background-color:transparent;color: white; margin-top:23px;" required>
      <option value="" disabled selected>Select Your Gender</option>
    <option value="MALE">MALE</option>
    <option value="FEMALE">FEMALE</option></select>

             <p>ADDRESS</p>
              <div style="display: flex; justify-content: space-between;">
        <div style="width: 48%;">
            <input type="text" name="no" id="no" placeholder="Door No">
            <input type="text" name="add1" placeholder="Address Line 1">
        </div> 
         <div style="width: 48%;">
            <input type="text" name="add2" placeholder="Address Line 2">
            <input type="text" name="city" placeholder="City">
        </div></div>
                
             <div style="display: flex; justify-content: space-between;">
        <div style="width: 48%;">
            <input type="text" name="city" placeholder="City">
        </div>
        <div style="width: 48%;">
            <input type="text" name="Country" placeholder="Country">
        </div>
    </div>
       <input type="text" id="RName" name="RName" placeholder="Restaurant Name" required>
    
<select name="currentrole" id="currentrole" required>
                            <option value="" disabled selected>Select Current Role</option>
                            <option value="Head Chef">Head Chef</option>
                            <option value="Sous Chef">Sous Chef</option>
                            <option value="Pastry Chef">Pastry Chef</option>
                            <option value="Line Cook">Line Cook</option>
                            <option value="Chef de Partie">Chef de Partie</option>
                            <option value="Catering Chef">Catering Chef</option>
                            <option value="Personal Chef">Personal Chef</option>
                            <option value="Kitchen Manager">Kitchen Manager</option>
                            <option value="Prep Cook">Prep Cook</option>
                            <option value="Baker">Baker</option>
                            <option value="Commis Chef">Commis Chef</option>
                            <option value="Culinary Instructor">Culinary Instructor</option>
                        </select>
    
                <select name="Experience" id="Experience" required>
                    <option value="" disabled selected>Select Year of Experience</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                    <option value="More than 5 years">More than 5 years</option>
                </select>

           <select name="cuisine" id="cuisine" required>
                    <option value="" disabled selected>Select Cuisine</option>
                    <option value="Italian">Italian</option>
                    <option value="Indian">Indian</option>
                    <option value="Chinese">Chinese</option>
                    <option value="Mexican">Mexican</option>
                    <option value="French">French</option>
                    <option value="All">All</option>
                    <option value="Other">Other</option>
                </select>
               
            
 <div class="col-lg-12 col-xs-12">
  <label for="id-upload" class="required-field">Upload ID   Proof(Aadhar Card/Passport):</label>
  <input type="file" class="form-control" id="id-upload" name="IDProof" multiple>
</div>
<div class="col-lg-12 col-xs-12">
  <label for="id-upload" class="required-field">Upload Profile picture</label>
  <input type="file" class="form-control" id="id-upload" name="profile" multiple>
</div>
<div class="col-lg-12 col-xs-12">
  <label for="id-upload" class="required-field">Upload Id Card</label>
  <input type="file" class="form-control" id="IDCard" name="IDCard" multiple>
</div>
<center>
 <input type="submit" name="sub" value="Submit" style="background-color:blue;color:white;width:550px;" >
                                       <button class="btn btn-primary" onclick="window.location.href='home.py'" style="background-color:red;color:white;width:550px;height:40px;border-radius:25px;">
Cancel</button><br><br></center>
                   <center> <p>Have an account already? <a href="Chef_login.py">Login</a></p></center>

                    </form>
                </div>
            </form>
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
              </script> </center>
                </div>
            </div>
            <hr class="my-4">
           
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
                open("Chef_images/" + pi, "wb").write(Img.file.read())
                si = os.path.basename(Img1.filename)
                open("Chef_images/" + si, "wb").write(Img1.file.read())
                ai = os.path.basename(Img2.filename)
                open("Chef_images/" + ai, "wb").write(Img2.file.read())
                chefName = form.getvalue("full_name")
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
                Restaurant = form.getvalue("RName")
                currentrole = form.getvalue("currentrole")
                Experience = form.getvalue("Experience")
                cuisine = form.getvalue("cuisine")
                q = """insert into chef_register(chefName,Email,phno,DOB,gender,Doorno, Address1,Address2, city,state,country,Restaurant,currentrole,Experience,cuisine,IDProof,profile,IDCard,status,designation) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','registered','chef')""" % (chefName,Email,phno,DOB,gender,Doorno, Address1,Address2, city,state,country,Restaurant,currentrole,Experience,cuisine,pi,si,ai)
                cur.execute(q)
                con.commit()
