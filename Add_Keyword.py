#!C:/Users/Home/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type: text/html\r\n\r\n")
import cgitb, os
import cgi
import pymysql

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="rating_system")
cur = con.cursor()
form = cgi.FieldStorage()
q2 = "SELECT * FROM keywords"
cur.execute(q2)
existing_keywords = cur.fetchall()
print("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Admin Add Keyword</title>
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
.container {
    display: flex;
    width:800px;
    height:500px;
    margin-left:250px;
    margin-top:50px;
}
.left-box, .right-box {
    flex: 1;
    padding: 20px;
}
.left-box {
    background-color: #11152d; 
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
}
.right-box {
    background-color: #f0f0f0; 
}
.login-form {
    width: 100%;
    max-width: 340px;
    padding: 40px 30px;
    background-color: grey;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0, 0, 0, .2);
}
.login-form h1 {
    margin-bottom: 20px;
    color: #fff;
    font-size: 30px;
    text-transform: uppercase;
}
.login-form option {
    background-color: white;
    color: black;
}
.login-form input, .login-form select {
    display: block;
    width: 100%;
    padding: 10px 20px;
    margin-bottom: 20px;
    border-radius: 25px;
    outline: none;
    font-size: 14px;
    border: none;
    color:black;
}
.login-form input[type="submit"] {
    background: #0072ff;
    cursor: pointer;
}
.login-form input[type="text"] {
    color: black;
}
.login-form input[type="submit"]:hover {
    background: #005aca;
}
.login-form input[type="button"] {
    background: red;
    cursor: pointer;
}
.login-form input[type="button"]:hover {
    background: darkred;
}
.sidebar {
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    width: 250px;
    height: 100vh;
    overflow-y: auto;
    background-color: #11152d;
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
    background-color: #11152d;
    box-shadow: 0 0 0 10px #11152d;
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
.sidebar .sidenavbar .navbar-nav a,
.sidebar .sidenavbar .navbar-nav button {
    color: white;
    padding: 7px 20px;
    font-size: 16px;
    font-weight: 500;
    border-radius: 0 30px 30px 0;
    outline: none;
    text-decoration: none;
}
.sidebar .sidenavbar .navbar-nav a:hover,
.sidebar .sidenavbar .navbar-nav a.active {
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
    color: #11152d;
    border-radius: 40px;
    margin-right: 8px;
}
.sidebar .sidenavbar .navbar-nav a:hover i,
.sidebar .sidenavbar .navbar-nav a.active i {
    background-color: #3c3cef;
    color: #e9ecef;
}
#otherInput {
    display: none;
    margin-top: 10px;
}
#otherInput input {
    display: block;
    width: 100%;
    padding: 10px 20px;
    margin-bottom: 20px;
    border-radius: 25px;
    outline: none;
    font-size: 14px;
    border: none;
    color: white;
}
</style>
</head>
<body>
  <div id="sidebarmenu" class="sidebar">
        <nav class="sidenavbar">
            <div class="navbar-nav">
                <a href="Admin_Dashboard.py"><i class="fas fa-th-large"></i>Dashboard</a>
              
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" id="loanRequestDropdown" data-bs-toggle="dropdown" aria-expanded="false">
                       <i class="fa fa-user-shield"></i>Cookery Student
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="loanRequestDropdown" style="width:300px;height:300px;">
                        <li><a class="dropdown-item" href="NewCookery_Students.py">New Cookery Student</a></li>
                        <li><a class="dropdown-item" href="ExistingCookery_Students.py">Existing Cookery Student</a></li>
                    </ul>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" id="loanRequestDropdown" data-bs-toggle="dropdown" aria-expanded="false">
                       <i class="fas fa-hat-cowboy"></i>Manage Chef
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="loanRequestDropdown" style="width:300px;height:300px;">
                        <li><a class="dropdown-item" href="New_Chef.py">New Chef</a></li>
                        <li><a class="dropdown-item" href="Existing_Chef.py">Existing Chef</a></li>
                    </ul>
                </li>

                  <a href="Add_keyword.py"><i class="fas fa-tag"></i>Keyword</a>

                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" id="loanRequestDropdown" data-bs-toggle="dropdown" aria-expanded="false">
                       <i class="fas fa-hamburger"></i>Recipes
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="loanRequestDropdown" style="width:300px;height:300px;">
                        <li><a class="dropdown-item" href="Admin_Recipe_Collection.py">All Recipes</a></li>
                        <li><a class="dropdown-item" href="Admin_PendingApproval.py">Pending Approvals</a></li>
                        <li><a class="dropdown-item" href="">Low Rated Recipes</a></li>
                        <li><a class="dropdown-item" href="">Incorrect Recipes</a></li>
                    </ul>
                </li>
                  <a href="home.py"><i class="fas fa-sign-out-alt"></i>Logt Out</a>
            </div>
        </nav>
    </div>


    </div>
<div class="container">
    <div class="left-box">
        <div class="login-form">
            <center><h1>Keyword</h1></center>
            <form method="post" enctype="multipart/form-data">
                <input type="text" name="common_recipes" placeholder="Enter keyword" style="color:black;">
                <input type="submit" name="sub" value="Add">
                <input type="button" name="can" value="Cancel">
            </form>
        </div>
    </div>

      <div class="right-box">
        <center><h3>Existing Keywords</h3></center>
        <ul>
""")

for keyword in existing_keywords:
    print(f"<li>{keyword[1]}</li>")

print("""
        </ul>
    </div>
</div>


<script>
document.addEventListener('DOMContentLoaded', function() {
    var select = document.getElementById('common_recipes');
    var otherInput = document.getElementById('otherInput');

    select.addEventListener('change', function() {
        if (this.value === 'other') {
            otherInput.style.display = 'block';
        } else {
            otherInput.style.display = 'none';
        }
    });
});
</script>
</body>
</html>
""")

submit = form.getvalue("sub")
if submit is not None:
    keyword = form.getvalue("common_recipes")
    q = """INSERT INTO keywords(keyword) VALUES(%s)"""
    cur.execute(q, (keyword,))
    con.commit()
    print("<script>alert('Keyword added successfully!');</script>")