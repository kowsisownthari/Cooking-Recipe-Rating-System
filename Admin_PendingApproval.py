#!C:/Users/Home/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb
import cgi
import pymysql, os
cgitb.enable()
form = cgi.FieldStorage()
con = pymysql.connect(host="localhost", user="root", password="", database="rating_system")
cur = con.cursor()
q2 = """
SELECT fr.*, COUNT(rr.rating) as rating_count, AVG(rr.rating) as avg_rating
FROM food_recipes fr
JOIN recipe_ratings rr ON fr.recipeid = rr.recipeid
WHERE rr.status='High rated' and fr.status='pending'
GROUP BY fr.recipeid
"""
cur.execute(q2)
highly_rated_recipes = cur.fetchall()
q3="""select * from food_recipes where status='pendingrecipe'"""
cur.execute(q3)
chef_recipes = cur.fetchall()
userid = form.getvalue("id")
chefid = ""
chefName = ""
designation = ""
if userid is not None:
    q = "SELECT * FROM chef_register WHERE id=%s"
    cur.execute(q, (userid,))
    res = cur.fetchall()
    for i in res:
        chefid = i[20]
        chefName = i[1]
        designation = i[21]
print("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Admin Pending Approval</title>
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
    background-color: #11152d;
    height: 100vh;
    overflow-y: auto;
    transition: 0.5s;
    z-index: 999;
}

.sidebar .sidebar-header {
    text-align: center;
    padding: 20px;
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

.sidebar .navbar-nav {
    list-style: none;
    padding-left: 0;
}

.sidebar .navbar-nav li {
    display: block;
}

.sidebar .navbar-nav a {
    display: flex;
    align-items: center;
    color: white;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: 500;
    text-decoration: none;
    border-radius: 0 30px 30px 0;
    transition: background-color 0.3s, color 0.3s;
}

.sidebar .navbar-nav a i {
    background-color: #e9ecef;
    color: #11152d;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    margin-right: 10px;
}

.sidebar .navbar-nav a:hover,
.sidebar .navbar-nav a.active {
    background-color: white;
    color: blue;
}

.sidebar .navbar-nav a:hover i,
.sidebar .navbar-nav a.active i {
    background-color: blue;
    color: white;
}

.step-input-group, .ingredient-input-group {
    display: flex;
    align-items: center;
    margin-bottom: 8px;
    gap: 8px; 
}
.ingredient-input-group {
    display: grid;
    grid-template-columns: 1fr 1fr auto;
    align-items: center;
}
.video-play-btn {
    background-color: #0077b6;
    color: white;
    border: none;
    padding: 8px 15px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}
.video-play-btn:hover {
    background-color: #005c8a;
}
.video-container {
    position: relative;
    padding-bottom: 56.25%;
    height: 0;
    overflow: hidden;
}
.video-container video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}
.rating {
    display: flex;
    flex-direction: row-reverse;
    justify-content: center;
}
.rating input {
    display: none; 
}
.rating label {
    font-size: 2rem;
    color: lightgray;
    cursor: pointer;
}
.rating label:hover,
.rating label:hover ~ label {
    color: gold;
}
.rating input:checked ~ label {
    color: gold;
}
.step-box {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
}
.step-number {
    font-weight: bold;
    margin-right: 10px;
    min-width: 70px;
}
.step-text {
    flex-grow: 1;
}
.ingredient-box {
    display: flex;
    align-items: center;
    margin-bottom: 8px;
}
.ingredient-name {
    flex: 1;
    margin-right: 10px;
}
.ingredient-quantity {
    flex: 1;
    text-align: left;
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
                        <li><a class="dropdown-item" href="Admin_Low_RatedRecipe.py">Low Rated Recipes</a></li>
                        <li><a class="dropdown-item" href="Admin_Incorrect_Recipes.py">Incorrect Recipes</a></li>
                    </ul>
                </li>
                  <a href="home.py"><i class="fas fa-sign-out-alt"></i>Logt Out</a>
            </div>
        </nav>
    </div>


    </div>
<div class="col-md-10 main-content" style="margin-left:45vh;width:1000px"">
    <center><h3 style="margin-top:20px;">Pending Approvals</h3></center><br>
    <div class="table-section">
        <div class="table-responsive">
            <table class="table table-bordered table-striped">
                <thead>
                    <tr>
                        <th>Serial No.</th>
                       
                        <th>Recipe Name</th>
                        <th>Main Category</th>
                         <th>Name</th>
                        <th>Designation</th>
                        <th>Recipe Video</th>
                         <th>Action</th>
                          <th>Other Details</th>
                    </tr>
                </thead>
                <tbody>
""")

serial_no = 1
for row in highly_rated_recipes:
    ratings_query = "SELECT * FROM recipe_ratings  WHERE recipeid=%s"
    cur.execute(ratings_query, (row[0],))
    ratings_data = cur.fetchall()

    steps = row[2].split(',') if row[2] else []
    ingredients = row[6].split(',') if row[6] else []
    quantities = row[7].split(',') if row[7] else []

    steps_html = ""
    for i, step in enumerate(steps):
        steps_html += f"""
            <div class="step-box">
                <div class="step-number">Step {i + 1}</div>
                <div class="step-text">{step.strip()}</div>
            </div>
        """

    ingredients_html = ""
    for i in range(len(ingredients)):
        quantity = quantities[i].strip() if i < len(quantities) else ''
        ingredients_html += f"""
            <div class="ingredient-box">
                <div class="ingredient-name">{ingredients[i].strip()}</div>
                <div class="ingredient-quantity">{quantity}</div>
            </div>
        """

    print(f"""
        <tr>
            <td>{serial_no}</td>
           
            <td>{row[1]}</td>
            <td>{row[4]}</td>
             <td>{row[11]}</td>
            <td>{row[14]}</td>
            <td>
                <button class="video-play-btn" onclick="playVideo('{row[10]}')">
                    <i class="fas fa-play"></i> Play Video
                </button>
            </td><td>
                 <form method="post" enctype="multipart/form-data">
<input type="hidden" name="student_id" value="{row[0]}">
<input type="hidden" name="student_name" value="{row[11]}">
<input type="hidden" name="Email" value="{row[12]}">
<input type="submit" name="status" value="Accept" class="btn btn-success">
<input type="submit" name="status" value="Reject" class="btn btn-danger">
</form>
            </td>
            <td>
                <button class="btn btn-success btn-sm" data-bs-toggle="modal" data-bs-target="#ratingsModal{row[0]}">
                    View Ratings
                </button>

                <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modal{row[0]}">
                    Recipe Details
                </button>

                <div class="modal fade" id="modal{row[0]}" tabindex="-1" aria-hidden="true">
                    <div class="modal-dialog modal-lg">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title">Recipe Details</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="row">
                                    <div class="col-md-6">
                                        <div class="form-group">
                                            <p><strong>Name:</strong> {row[11]}</p>
                                        </div>
                                         <div class="form-group">
                                            <p><strong>ID:</strong> {row[12]}</p>
                                        </div>
                                        <div class="form-group">
                                            <p><strong>Recipe Name:</strong> {row[1]}</p>
                                        </div>
                                        <div class="form-group">
                                            <p><strong>Main Category:</strong> {row[4]}</p>
                                        </div>
                                        <div class="form-group">
                                            <p><strong>Sub Category:</strong> {row[5]}</p>
                                        </div>
                                        <div class="form-group">
                                            <p><strong>Keywords:</strong> {row[8]}</p>
                                        </div>
                                        <div class="form-group">
                                            <p><strong>Cooking Duration:</strong> {row[3]}</p>
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="recipe-details">
                                            <div class="recipe-section">
                                                <h4 class="section-title">Instructions</h4>
                                                <div class="steps-container">
                                                    {steps_html}
                                                </div>
                                            </div>
                                            <div class="recipe-section">
                                                <h4 class="section-title">Ingredients</h4>
                                                <div class="ingredients-container">
                                                    {ingredients_html}
                                                </div>
                                            </div>
                                        </div>

                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="modal fade" id="ratingsModal{row[0]}" tabindex="-1" aria-hidden="true">
                    <div class="modal-dialog modal-lg">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title">Ratings for {row[1]}</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <table class="table">
                                    <thead>
                                        <tr>
                                            <th>Chef Name</th>
                                             <th>Chef Id</th>
                                            <th>Rating</th>
                                            <th>Comment</th>
                                        </tr>
                                    </thead>
                                    <tbody>
    """)
    if ratings_data:
        for rating in ratings_data:
            print(f"""
                <tr>
                     <td>{rating[1]}</td>
                    <td>{rating[2]}</td>
                    <td>{rating[3]}/5</td>
                    <td>{rating[4]}</td>
                </tr>
            """)
    else:
        print("<tr><td colspan='3' class='text-center'>No ratings yet</td></tr>")

    print("""
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </td>  

        </tr>
    """)
    serial_no += 1

print("""
                </tbody>
            </table>
        </div>
    </div>
      <center><h3>Chef Recipes Pending Approval</h3><br></center>
        <div class="table-section">
            <div class="table-responsive">
                <table class="table table-bordered table-striped">
                    <thead>
                        <tr>
                            <th>Serial No.</th>
                           
                            <th>Recipe Name</th>
                            <th>Main Category</th>
                            <th>Sub Category</th>
                             <th>Name</th>
                            <th>ID</th>
                            <th>Recipe Video</th>
                            <th>Actions</th>
                            <th>Other Details</th>
                        </tr>
                    </thead>
                    <tbody>
""")

serial_no = 1
for row in chef_recipes:

    steps = row[2].split(',') if row[2] else []
    ingredients = row[6].split(',') if row[6] else []
    quantities = row[7].split(',') if row[7] else []
    steps_html = ""
    for i, step in enumerate(steps):
        steps_html += f"""
                <div class="step-box">
                    <div class="step-number">Step {i + 1}</div>
                    <div class="step-text">{step.strip()}</div>
                </div>
            """

    ingredients_html = ""
    for i in range(len(ingredients)):
        quantity = quantities[i].strip() if i < len(quantities) else ''
        ingredients_html += f"""
                <div class="ingredient-box">
                    <div class="ingredient-name">{ingredients[i].strip()}</div>
                    <div class="ingredient-quantity">{quantity}</div>
                </div>
            """

    print(f"""
        <tr>
            <td>{serial_no}</td>
           
            <td>{row[1]}</td>
            <td>{row[4]}</td>
            <td>{row[5]}</td>
             <td>{row[11]}</td>
            <td>{row[12]}</td>
            <td>
                <button class="video-play-btn" onclick="playVideo('{row[10]}')">
                    <i class="fas fa-play"></i> Play Video
                </button>
            </td><td>
            <form method="post" enctype="multipart/form-data">
<input type="hidden" name="chef_id" value="{row[0]}">
<input type="hidden" name="student_name" value="{row[11]}">
<input type="hidden" name="Email" value="{row[12]}">
<input type="submit" name="status" value="Accept" class="btn btn-success">
<input type="submit" name="status" value="Reject" class="btn btn-danger">
</form></td>
            <td>
                <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modal{row[0]}">
                    Recipe Details
                </button>
               
                <div class="modal fade" id="modal{row[0]}" tabindex="-1" aria-hidden="true">
                    <div class="modal-dialog modal-lg">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title">Edit Recipe Details</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <form id="editForm{row[0]}"  method="post" enctype="multipart/form-data">
                                <div class="modal-body">
                                <div class="row">
                                    <div class="col-md-6">
                                        <div class="form-group">
                                            <p><strong>Name:</strong> {row[11]}</p>
                                        </div>
                                          <div class="form-group">
                                            <p><strong>ID:</strong> {row[12]}</p>
                                        </div>
 <div class="form-group">                                            <p><strong>Recipe Name:</strong> {row[1]}</p>
                                        </div>
                                        <div class="form-group">
                                            <p><strong>Main Category:</strong> {row[4]}</p>
                                        </div>
                                        <div class="form-group">
                                            <p><strong>Sub Category:</strong> {row[5]}</p>
                                        </div>
                                        <div class="form-group">
                                            <p><strong>Keywords:</strong> {row[8]}</p>
                                        </div>
                                        <div class="form-group">
                                            <p><strong>Cooking Duration:</strong> {row[3]}</p>
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="recipe-details">
                                            <div class="recipe-section">
                                                <h4 class="section-title">Instructions</h4>
                                                <div class="steps-container">
                                                    {steps_html}
                                                </div>
                                            </div>
                                            <div class="recipe-section">
                                                <h4 class="section-title">Ingredients</h4>
                                                <div class="ingredients-container">
                                                    {ingredients_html}
                                                </div>
                                            </div>
                                        </div>
    """)
print(f"""
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
            </td>
        </tr>
    """)
serial_no += 1

print("""
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <div class="modal fade" id="videoModal" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Recipe Video</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="video-container" id="videoContainer"></div>
                </div>
            </div></div>
</div>



<script>
function playVideo(videoName) {
    const modal = document.getElementById('videoModal');
    const videoContainer = document.getElementById('videoContainer');
    videoContainer.innerHTML = '';
    const video = document.createElement('video');
    video.controls = true;
    video.style.width = '100%';
    video.src = `Visitor_Recipe/${videoName}`;
    videoContainer.appendChild(video);
    const modalInstance = new bootstrap.Modal(modal);
    modalInstance.show();
    modal.addEventListener('shown.bs.modal', function () {
        video.play();
    });
    modal.addEventListener('hidden.bs.modal', function () {
        video.pause();
    });
}
</script>
</body>
</html>
""")
submit = form.getvalue("status")
if submit is not None:
    chef_id = form.getvalue('chef_id')
    q = "SELECT Name, Email,designation FROM food_recipes WHERE recipeid=%s"
    cur.execute(q, (chef_id,))
    student_data = cur.fetchone()
    if student_data:
        Name = student_data[0]
        email = student_data[1]
        status = form.getvalue('status')
        q = "UPDATE food_recipes SET status=%s WHERE recipeid=%s"
        cur.execute(q, (status, chef_id))
        con.commit()
        con.commit()
        print(f"""
        <script>
        alert("Recipe published");
        </script>
       """)
submit = form.getvalue("status")
if submit is not None:
    student_id = form.getvalue('student_id')
    q = "SELECT Name, Email,designation FROM food_recipes WHERE recipeid=%s"
    cur.execute(q, (student_id,))
    student_data = cur.fetchone()
    if student_data:
        Name = student_data[0]
        email = student_data[1]
        status = form.getvalue('status')
        q = "UPDATE food_recipes SET status=%s WHERE recipeid=%s"
        cur.execute(q, (status, student_id))
        con.commit()
        con.commit()
        print(f"""
        <script>
        alert("Recipe published");
        </script>
       """)