#!C:/Users/Home/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type: text/html\r\n\r\n")
import cgitb, os
import cgi
import pymysql

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="rating_system")
cur = con.cursor()
form = cgi.FieldStorage()
userid = form.getvalue("id")
userid = userid[0]
q = "SELECT * FROM visitor_register WHERE id=%s"
cur.execute(q, (userid))
res = cur.fetchall()
for i in res:
 print("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Visitor Dashboard</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Open sans', sans-serif;
}
.sidebar {
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    width: 250px;
    height: 100vh;
    overflow-y: auto;
    background-color:  #11152d;
    transition: 0.5s;
    z-index: 999;
}
.sidebar .sidenavbar {
    position: relative;
    padding: 8px 0;
}
.sidebar .sidenavbar .sidebar-header {
    padding: 16px 20px;
    text-align: center;
}
.sidebar .sidenavbar .sidebar-header .user-photo {
    width: 90px;
    height: 90px;
    background-color:  #11152d;
    box-shadow: 0 0 0 10px  #11152d;
    border: 1px solid transparent;
    margin: 16px 0;
    padding: 2px;
    border-radius: 50%;
}
.sidebar .sidenavbar .sidebar-header .username {
    color: white;
    padding: 2px 0;
    font-size: 16px;
    font-weight: 700;
    margin: 0;
    white-space: nowrap;
}
.sidebar .sidenavbar .navbar-nav {
    display: flex;
    flex-direction: column;
    padding-left: 0;
    list-style: none;
}
.sidebar .sidenavbar .navbar-nav a,.sidebar .sidenavbar .navbar-nav button {
    color: white;
    padding: 7px 20px;
    font-size: 16px;
    font-weight: 500;
    border-radius: 0 30px 30px 0;
    outline: none;
    text-decoration: none;
}
.sidebar .sidenavbar .navbar-nav a:hover,
.sidebar .sidenavbar .navbar-nav a.active{
    color: blue;
    background-color: white;
    border-color: blue;
}
.sidebar .dropdown-menu {
        background: #11152d;
    }
    .sidebar .dropdown-menu a {
        color: #fff;
        padding: 10px 20px;
    }
    .sidebar .dropdown-menu a:hover {
        background-color: #0056b3;
    }
.sidebar .sidenavbar .navbar-nav a i {
    width: 40px;
    height: 40px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background-color: #e9ecef;
    color:  #11152d;
    border-radius: 40px;
    margin-right: 8px;
}
.sidebar .sidenavbar .navbar-nav a:hover i,
.sidebar .sidenavbar .navbar-nav a.active i {
    background-color: #3c3cef;
    color: #e9ecef;
}

.Student-Details{
    padding: 24px;
    margin-left: 270px;
    display: flex;
    flex-direction: row;
    gap: 24px;
}

.Student-Details .box{
    width: calc(33.33% - 16px);
    height: 200px; 
    background-color: #e9ecef;
    border-radius: 5px;
    padding: 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.Student-Details .box i{
    color: #11152d;
    font-size: 48px;
}
.Student-Details .box .right-text{
    margin-left: 16px;
}
.Student-Details .box .right-text p{
    color:  #11152d;
    font-size: 16px;
    font-weight: 500;
    margin-bottom: 8px;
}
.Student-Details .box .right-text h6{
    font-size: 16px;
    font-weight: 700;
    color: black;
}
  .dashboard-container {
            background: rgb(14, 14, 57);
            padding: 10px 10px;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            text-align: center;
            color: #ffffff;
            position: relative;
            margin-top: -200px;
        }
        .dashboard-container img {
            border-radius: 50%;
            width: 120px;
            height: 120px;
            border: 5px solid #ffffff;
            background-color: #ffffff;
            object-fit: cover;
            position: absolute;
            top: -60px;
            left: 50%;
            transform: translateX(-50%);
        }
        .dashboard-container h6 {
            margin-top: 60px; 
            font-size: 18px;
            color: #ffffff;
        }
        .dashboard-container .btn-primary {
            background-color: #ffffff;
            border-color: #ffffff;
            color: #0077b6;
            padding: 10px 30px;
            font-size: 18px;
            margin-top: 25px;
            border-radius: 30px;
            transition: background-color 0.3s, transform 0.3s;
        }
        .dashboard-container .btn-primary:hover {
            background-color: #f0f2f5;
            transform: scale(1.05);
        }
        .dashboard-container .btn-primary:focus {
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.6);
        }
</style>""")
 print(f"""
<body>
    <div id="sidebarmenu" class="sidebar">
        <nav class="sidenavbar">
            <div class="navbar-nav">
                <a href="Visitor_Dashboard.py"><i class="fas fa-th-large"></i>Dashboard</a>

 <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" id="loanRequestDropdown" data-bs-toggle="dropdown" aria-expanded="false">
                       <i class="fas fa-hamburger"></i>Recipe Collection
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="loanRequestDropdown" style="width:300px;height:300px;">
                         <li><a class="dropdown-item" href="Visitor_Recipe_Collection.py?id={userid}">All Recipes</a></li>
                        <li><a class="dropdown-item" href="Visitor_Wishlist_Recipe.py?id={userid}">Wishlist Recipes</a></li>
                        <li><a class="dropdown-item" href="Visitor_Rated_Recipe.py?id={userid}">Rated Recipes</a></li>
                    </ul>
                </li>
 <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" id="loanRequestDropdown" data-bs-toggle="dropdown" aria-expanded="false">
                       <i class="fas fa-hamburger"></i>Recipes
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="loanRequestDropdown" style="width:300px;height:300px;">
                        <li><a class="dropdown-item" href="VisitorAdd_Recipes.py?id={userid}">Add Recipes</a></li>
                         <li><a class="dropdown-item" href="VisitorPending_Recipe.py?id={userid}">Pending Recipes</a></li>
                        <li><a class="dropdown-item" href="VisitorExisting_Recipe.py?id={userid}">Existing Recipes</a></li>
                        <li><a class="dropdown-item" href="Visitor_PoorRated_Recipe.py?id={userid}">Poor Ratings Recipes</a></li>
                    </ul>
                </li>
              
                  <a href="home.py"><i class="fas fa-sign-out-alt"></i>Logt Out</a>
            </div>
        </nav>
    </div>


    </div>""")
 print(f"""
  <center> <div class="col-12 col-md-9" style="margin-top:100px;">
                <div class="header"> 
                    <h2>Visitor Dashboard</h2>
                    <br>
                    <h3>Welcome {i[1]}</h3><br>
                </div>
                <div class="dashboard-container mx-auto mt-5 col-12 col-sm-10 col-md-8 col-lg-6">
                    <img src="./Visitor_Images/{i[16]}" alt="Profile Image">
                   
                    <h6>{i[1]}</h6>
                    <h6>{i[2]}</h6>
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal">
                        Change Password
                    </button>
                    <button type="button"class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#editModal">
                    Edit Details
                </button>
                </div>
            </div>
        </div>
    </div></center>
    <div class="modal fade" id="myModal">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title">Change Password</h4>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <form method="post">
                        <div class="form-group">
                            <label for="newPassword">New Password</label>
                            <input type="password" class="form-control" id="newPassword" name="newPassword" required>
                        </div>
                        <div class="form-group">
                            <label for="confirmPassword">Confirm New Password</label>
                            <input type="password" class="form-control" id="confirmPassword" name="confirmPassword" required>
                        </div>
                        <input type="submit"  class="btn btn-primary" value="submit" name="sub1">
                    </form>
                </div>
            </div>
        </div>
    </div><div class="modal fade" id="editModal">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title">Edit Details</h4>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <form method="post">
                      <div class="form-group">
                            <label for="Name">Name</label>
                            <input type="text" class="form-control" id="name" name="name" value="{i[1]}">
                        </div><br>
                        <div class="form-group">
                            <label for="phoneNumber">Phone Number</label>
                            <input type="text" class="form-control" id="phoneNumber" name="phoneNumber" value="{i[3]}">
                        </div><br>
                        <div class="form-group">
                            <label for="email">Email ID</label>
                            <input type="email" class="form-control" id="email" name="email" value="{i[2]}">
                        </div><br>
                          
                        <input type="hidden" name="id" value="{i[0]}">
                        <input type="submit"  class="btn btn-primary" value="Save changes" name="sub">
                    </form>
                </div>
            </div>
        </div>
    </div>
        <div class="modal fade" id="complaintModal" tabindex="-1" aria-labelledby="complaintModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="complaintModalLabel">Edit Details</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                         <form method="post" enctype="multipart/form-data">
                            <div class="mb-3">
                                <label for="studentName" class="form-label">Student Name</label>
                                <input type="text" class="form-control" id="studentName" name="studentName" value="{i[1]}" readonly>
                            </div>
                             <div class="mb-3">
                                <label for="StudentId" class="form-label">Student Id</label>
                                <input type="text" class="form-control" id="Student_id" name="Student_id" value="{i[0]}" readonly>
                            </div>
</body>
</html>
""")
password = form.getvalue("confirmPassword")
pass_submit = form.getvalue("sub1")
submit = form.getvalue("sub")
Name= form.getvalue("name")
phno = form.getvalue("phoneNumber")
Email = form.getvalue("email")


if submit:
    q1 = """update visitor_register set Name='%s',phno='%s',Email='%s' where id='%s' """ % (Name,phno,Email, userid)
    cur.execute(q1)
    con.commit()
    print(f"""
        <script>
        alert(" changed successfully.");
        </script>
    """)
if pass_submit:
    q2 = """update visitor_register set password='%s'where id='%s' """ % (password,userid)
    cur.execute(q2)
    con.commit()
    print(f"""
        <script>
        alert("changed successfully.");
        </script>
    """)

