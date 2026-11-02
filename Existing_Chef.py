#!C:/Users/Home/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb
import cgi
import pymysql

cgitb.enable()
form = cgi.FieldStorage()
con = pymysql.connect(host="localhost", user="root", password="", database="rating_system")
cur = con.cursor()

q3 = "SELECT * FROM chef_register WHERE status='Accept'"
cur.execute(q3)
complaints = cur.fetchall()
q3 = "SELECT * FROM chef_register WHERE status='Reject'"
cur.execute(q3)
old_complaints = cur.fetchall()

print("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Existing Chef</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function() {
            $('.view-image').click(function(e) {
                e.preventDefault();
                var imageUrl = $(this).data('image');
                var previewContainer = $(this).closest('.col-md-6').find('.image-preview-container');
                var previewImage = previewContainer.find('.preview-image');

                previewImage.attr('src', imageUrl);
                previewContainer.show();
            });
        });
    </script>
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

        .modal-content {
            border-radius: 15px;
        }

        .modal-header .btn-close {
            background-color: white;
            border: none;
        }
        .modal p{
        font-size:15px;
        }
.modal-body {
            max-height: 80vh;
            overflow-y: auto;
        }
        .preview-image {
            max-width: 100%;
            max-height: 300px; 
            width: auto;
            height: auto;
            margin-top: 10px;
            object-fit: contain;
        }
        .image-preview-container {
            display: none;
            margin-top: 15px;
            text-align: center; 
        }
        .image-controls {
            margin-top: 10px;
            text-align: center;
        }
     .modal-profile-image {
        max-width: 100%;
        height: auto;
    }

</style>

</head>""")
print(f"""
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


    </div>
<div class="container mt-4">
    <div class="table-responsive" style="margin-left:200px;max-width:1100px;">
        <center><h3>Accepted Chef</h3></center>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>S.No</th>
                    <th>Name</th>
                    <th>ID</th>
                    <th>Profile</th>
                    <th>Email</th>
                    <th>Gender</th>
                  <th>Restaurant</th>
                    <th>Current Role</th>
                    <th>Exp(Yrs)</th>
                    <th>Other Details</th>
                </tr>
            </thead>
            <tbody>
""")

serial_number = 1
for row in complaints:
    print(f"""
        <tr>
            <td>{serial_number}</td>
            <td>{row[1]}</td>
            <td>{row[20]}</td>
            <td><img src="Chef_images/{row[17]}" 
                     onclick="showImage('{row[17]}')"
                     style="border-radius: 50%; width: 120px; height: 120px; border: 5px solid #ffffff; cursor: pointer;" 
                     alt="Profile Image"></td>
          <td>{row[2]}</td>
          
                    <td>{row[4]}</td>
                     <td>{row[12]}</td>
                    <td>{row[13]}</td>
                     <td>{row[14]}</td>
            <td>
                <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modal{row[0]}">
                    View More
                </button>
            </td>
        </tr>
    """)
    serial_number += 1

print("""
            </tbody>
        </table>
    </div>

    <div class="table-responsive mt-4" style="margin-left:200px;width:950px;">
        <center><h3>Rejected Chef</h3></center>
        <table class="table table-striped">
            <thead>
                <tr>
                     <th>S.No</th>
                    <th>Name</th>
                    <th>profile</th>
                    <th>Email</th>
                    <th>Gender</th>
                  <th>Restaurant </th>
                    <th>Current Role</th>
                    <th>Experience(yrs)</th>
                     <th>Other Details</th>
                </tr>
            </thead>
            <tbody>
""")

serial_number = 1
for row in old_complaints:
    print(f"""
        <tr>
            <td>{serial_number}</td>
            <td>{row[1]}</td>
            <td><img src="Chef_images/{row[17]}" 
                     onclick="showImage('{row[17]}')"
                     style="border-radius: 50%; width: 120px; height: 120px; border: 5px solid #ffffff; cursor: pointer;" 
                     alt="Profile Image"></td>
           
 <td>{row[2]}</td>
                    <td>{row[4]}</td>
                     <td>{row[12]}</td>
                    <td>{row[13]}</td>
                     <td>{row[14]}</td>
            <td>
                <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalRejected{row[0]}">
                    View More
                </button>
            </td>
        </tr>
    """)
    serial_number += 1

print("""
            </tbody>
        </table>
    </div>
    <div class="modals-container">
""")

for row in complaints:
    print(f"""
        <!-- View More Modal for Accepted Student -->
        <div class="modal fade" id="modal{row[0]}" tabindex="-1" aria-labelledby="modalLabel{row[0]}" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="viewMoreModalLabel{row[0]}">More Details</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body" style="max-height: 130vh; overflow-y: auto;">
                        <div class="container-fluid">
                            <center>
                                <img src="Chef_images/{row[17]}" alt="Profile Image" style="border-radius:70px; width:150px; height:150px;">
                            </center>
                            <br>
                            <div class="row">
                                <div class="col-md-6">
                                    <p><strong>Name:</strong> {row[1]}</p>
                              <p><strong>Email:</strong> {row[2]}</p> 
                              <p><strong>Gender:</strong> {row[4]}</p>
                               <p><strong>Restaurant:</strong> {row[12]}</p>
                               <p><strong>Current Role:</strong> {row[13]}</p>
                               <p><strong>Experience:</strong> {row[14]}</p>
                                <p><strong>Doorno:</strong> {row[6]}</p>
                                   <p><strong>Address1:</strong> {row[7]}</p>
                             <p><strong>Address2:</strong> {row[8]}</p>
                               <p><strong>City:</strong> {row[9]}</p>
                                </div>
                                <div class="col-md-6">
                                     <p><strong>State:</strong> {row[10]}</p>
                                  <p><strong>Country:</strong> {row[11]}</p>
                                    <p><strong>Date Of Birth:</strong> {row[5]}</p>
                                      <p><strong>Phone Number</strong> {row[3]}</p>  
                                       <p><strong>Cuisine:</strong> {row[15]}</p>
                                    <p><strong>ID Proof:</strong>
                                        <a href="#" class="view-image" data-image="Chef_images/{row[16]}">View</a> |
                                        <a href="Chef_images/{row[16]}" download>Download</a>
                                    </p>
                                    <p><strong>ID Card:</strong>
                                        <a href="#" class="view-image" data-image="Chef_images/{row[18]}">View</a> |
                                        <a href="Chef_images/{row[18]}" download>Download</a>
                                    </p>
                                    <div class="image-preview-container">
                                        <img src="" alt="Preview" class="preview-image">
                                    </div>
                                    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#changePasswordModal{row[0]}">
                                        Change Password
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="modal fade" id="changePasswordModal{row[0]}" tabindex="-1" aria-labelledby="changePasswordModalLabel{row[0]}" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="changePasswordModalLabel{row[0]}">Change Password</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form method="post" enctype="multipart/form-data" id="passwordChangeForm{row[0]}">
                            <div class="mb-3">
                                <input type="hidden" name="rowid" value="{row[0]}">
                                <label for="newPassword" class="form-label">New Password</label>
                                <input type="password" class="form-control" id="newPassword" name="newPassword" required>
                            </div>
                            <div class="mb-3">
                                <label for="confirmPassword" class="form-label">Confirm New Password</label>
                                <input type="password" class="form-control" id="confirmPassword" name="confirmPassword" required>
                            </div>
                            <div class="alert alert-danger d-none" id="passwordError">
                                Passwords do not match!
                            </div>
                            <div class="modal-footer">
                                <input type="submit" class="btn btn-primary" name="sub" value="Save Changes">
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    """)

for row in old_complaints:
    print(f"""
        <div class="modal fade" id="modalRejected{row[0]}" tabindex="-1" aria-labelledby="modalLabelRejected{row[0]}" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="viewMoreModalLabelRejected{row[0]}">More Details</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body" style="max-height: 130vh; overflow-y: auto;">
                        <div class="container-fluid">
                            <center>
                                <img src="Chef_images/{row[17]}" alt="Profile Image" style="border-radius:70px; width:150px; height:150px;">
                            </center>
                            <br>
                            <div class="row">
                                <div class="col-md-6">
                                    <p><strong>Name:</strong> {row[1]}</p>
                              <p><strong>Email:</strong> {row[2]}</p> 
                              <p><strong>Gender:</strong> {row[4]}</p>
                               <p><strong>Restaurant:</strong> {row[12]}</p>
                               <p><strong>Current Role:</strong> {row[13]}</p>
                               <p><strong>Experience:</strong> {row[14]}</p>
                                <p><strong>Doorno:</strong> {row[6]}</p>
                                   <p><strong>Address1:</strong> {row[7]}</p>
                             <p><strong>Address2:</strong> {row[8]}</p>
                               <p><strong>City:</strong> {row[9]}</p>
                                </div>
                                <div class="col-md-6">
                                     <p><strong>State:</strong> {row[10]}</p>
                                  <p><strong>Country:</strong> {row[11]}</p>
                                    <p><strong>Date Of Birth:</strong> {row[5]}</p>
                                      <p><strong>Phone Number</strong> {row[3]}</p>  
                                       <p><strong>Cuisine:</strong> {row[15]}</p>
                                    <p><strong>ID Proof:</strong>
                                        <a href="#" class="view-image" data-image="Chef_images/{row[16]}">View</a> |
                                        <a href="Chef_images/{row[16]}" download>Download</a>
                                    </p>
                                    <p><strong>ID Card:</strong>
                                        <a href="#" class="view-image" data-image="Chef_images/{row[18]}">View</a> |
                                        <a href="Chef_images/{row[18]}" download>Download</a>
                                    </p>
                                    <div class="image-preview-container">
                                        <img src="" alt="Preview" class="preview-image">
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """)


print("""
        <script>
       function changePassword() {
    const newPassword = document.getElementById('newPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const errorDiv = document.getElementById('passwordError');

    if (newPassword !== confirmPassword) {
        errorDiv.classList.remove('d-none');
        return false;
    }

    errorDiv.classList.add('d-none');
    return true;
}

// Add event listeners to all password change forms
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form[id^="passwordChangeForm"]');
    forms.forEach(form => {
        form.onsubmit = function(e) {
            return changePassword();
        };
    });
});
        function showImage(imageUrl) {
            document.querySelector('#imageModal .modal-profile-image').src = imageUrl;
            var modal = new bootstrap.Modal(document.getElementById('imageModal'));
            modal.show();
        }
        </script>
</body>
</html>
""")
password = form.getvalue("confirmPassword")
rowid = form.getvalue("rowid")
pass_submit = form.getvalue("sub")
if pass_submit:
        q2 = "UPDATE chef_register SET password=%s,admin_status='passchanged' WHERE id=%s"
        cur.execute(q2, (password, rowid))
        con.commit()
        print("""
            <script>
                alert("Password changed successfully.");
            </script>
        """)