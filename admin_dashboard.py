#!C:/Users/Home/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type: text/html\r\n\r\n")
import cgitb, os
import cgi
import pymysql

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="rating_system")
cur = con.cursor()
form = cgi.FieldStorage()
cur.execute("SELECT COUNT(*) FROM student_register")
total_students = cur.fetchone()[0]
cur.execute("SELECT COUNT(*) FROM chef_register")
total_chefs = cur.fetchone()[0]
cur.execute("SELECT COUNT(*) FROM visitor_register")
total_visitors = cur.fetchone()[0]
cur.execute("SELECT COUNT(*) FROM food_recipes")
total_recipes = cur.fetchone()[0]
print("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Admin Dashboard</title>
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
 .dashboard-stats {
        display: flex;
        justify-content: space-between;
        gap: 24px;
    }
    .dashboard-stats .stat-box {
        background-color: #e9ecef;
        border-radius: 8px;
        padding: 20px;
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .dashboard-stats .stat-box h3 {
        font-size: 24px;
        color: #11152d;
    }
    .dashboard-stats .stat-box p {
        font-size: 18px;
        color: #333;
        margin: 8px 0;
    }
    .dashboard-stats .stat-box i {
        font-size: 48px;
        color: #11152d;
    }
</style>
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
                        <li><a class="dropdown-item" href="Admin_Low_RatedRecipe.py">Low Rated Recipes</a></li>
                        <li><a class="dropdown-item" href="Admin_Incorrect_Recipes.py">Incorrect Recipes</a></li>
                    </ul>
                </li>
                  <a href="home.py"><i class="fas fa-sign-out-alt"></i>Logt Out</a>
            </div>
        </nav>
    </div>


    </div>""")
print(f"""
    <div class="content" style="margin-left:260px; margin-top:50px;">
    <center><h3>Admin Dashboard</h3></center><br><br>

    <div class="dashboard-stats">
        <div class="stat-box">
            <i class="fas fa-user-graduate"></i>
            <p>Total Students</p>
            <h3>{total_students}</h3>
            
        </div>

        <div class="stat-box">
            <i class="fas fa-hat-cowboy"></i>
              <p>Total Chefs</p>
            <h3>{total_chefs}</h3>
          
        </div>

        <div class="stat-box">
            <i class="fas fa-users"></i>
             <p>Total Visitors</p>
            <h3>{total_visitors}</h3>
           
        </div>

        <div class="stat-box">
            <i class="fas fa-book"></i>
             <p>Total Recipes</p>
            <h3>{total_recipes}</h3>    
        </div>
    </div>
</div>
</body>
</html>
""")
