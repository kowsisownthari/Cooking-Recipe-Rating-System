#!C:/Users/Home/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb
import cgi
import pymysql, os

cgitb.enable()
form = cgi.FieldStorage()
con = pymysql.connect(host="localhost", user="root", password="", database="rating_system")

cur = con.cursor()
q2 = "SELECT * FROM food_recipes WHERE status='pending'"
cur.execute(q2)
emp_application_data = cur.fetchall()
q3 = "SELECT * FROM food_recipes WHERE Name=%s and status='Reject'"
recipeid = ""
for row in emp_application_data:
    recipeid = row[0]
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
<title> Chef UnReviewed Recipe</title>
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
.star-rating {
    display: inline-flex;
    flex-direction: row-reverse;
    font-size: 0;
}
.star-rating input {
    display: none;
}
.star-rating label {
    cursor: pointer;
    font-size: 30px;
    color: #ccc;
}
.star-rating label:before {
    content: "\\f005";
    font-family: "Font Awesome 5 Free";
    font-weight: 900;
    font-size: 24px;
}
.star-rating input:checked ~ label,
.star-rating label:hover,
.star-rating label:hover ~ label {
    color: #f8ce0b;
}
</style>
</head>""")
print(f"""
<body>
   <div id="sidebarmenu" class="sidebar">
        <nav class="sidenavbar">
            <div class="navbar-nav">
                <a href="Chef_Dashboard.py?id={userid}"><i class="fas fa-th-large"></i>Dashboard</a>
             <a href="Chef_Recipe_Collection.py?id={userid}"><i class="fas fa-utensils"></i>Recipe Collection</a>

 <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" id="loanRequestDropdown" data-bs-toggle="dropdown" aria-expanded="false">
                       <i class="fas fa-star"></i>Awaiting Rating
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="loanRequestDropdown" style="width:300px;height:300px;">
                         <li><a class="dropdown-item" href="chef_Unreview_Recipe.py?id={userid}">Unreviewed Recipes</a></li>
                        <li><a class="dropdown-item" href="Chef_reviewedRecipe.py?id={userid}">Existing Recipes</a></li>
                    </ul>
                </li>
              
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" id="loanRequestDropdown" data-bs-toggle="dropdown" aria-expanded="false">
                       <i class="fas fa-hamburger"></i>Recipes
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="loanRequestDropdown" style="width:300px;height:300px;">
                         <li><a class="dropdown-item" href="ChefAdd_Recipe.py?id={userid}">Add Recipes</a></li>
                        <li><a class="dropdown-item" href="Chef_Pending_recipe.py?id={userid}">Pending Recipes</a></li>
                        <li><a class="dropdown-item" href="Chef_ExistingRecipe.py?id={userid}">Existing Recipes</a></li>
                 <li><a class="dropdown-item" href="Chef_Wishlist_Recipe.py?id={userid}">Wishlist Recipes</a></li>
                    </ul>
                </li>
                  <a href="home.py"><i class="fas fa-sign-out-alt"></i>Logt Out</a>
            </div>
        </nav>
    </div>
    </div>
<div class="col-md-10 main-content" style="margin-left:45vh;width:1000px">
    <center><h3 style="margin-top:20px;">UnReviewed Recipe</h3></center><br>
    <div class="table-section">
        <div class="table-responsive">
            <table class="table table-bordered table-striped">
                <thead>
                    <tr>
                        <th>Serial No.</th>
                         <th>Recipe Id</th>
                        <th>Recipe Name</th>
                        <th>Main Category</th>
                         <th>Name</th>
                        <th>Designation</th>
                        <th>Recipe Video</th>
                        <th>Other Details</th>
                    </tr>
                </thead>
                <tbody>
""")

serial_no = 1
for row in emp_application_data:
    ratings_query = "SELECT * FROM recipe_ratings WHERE recipeid=%s"
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
           
             <td>{row[0]}</td>
            <td>{row[1]}</td>
             
            <td>{row[4]}</td>
             <td>{row[11]}</td>
             <td>{row[14]}</td>
            <td>
               <div class="d-flex gap-2">
                    <button class="video-play-btn" onclick="playVideo('{row[10]}')">
                        <i class="fas fa-play"></i> Play Video
                    </button>
                   
                </div>
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
                                            <p><strong>Recipe ID:</strong> {row[0]}</p>
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
                                   <form method="post" enctype="multipart/form-data">
                    <input type="hidden" name="recipeid" value="{row[0]}">
                    
                     <h6>Ratings</h6>
                    <div class="star-rating">
                   
                        <input type="radio" id="star5_{row[0]}" name="rating" value="5" required/>
                        <label for="star5_{row[0]}" title="5 stars"></label>
                        <input type="radio" id="star4_{row[0]}" name="rating" value="4" required/>
                        <label for="star4_{row[0]}" title="4 stars"></label>
                        <input type="radio" id="star3_{row[0]}" name="rating" value="3" required/>
                        <label for="star3_{row[0]}" title="3 stars"></label>
                        <input type="radio" id="star2_{row[0]}" name="rating" value="2" required/>
                        <label for="star2_{row[0]}" title="2 stars"></label>
                        <input type="radio" id="star1_{row[0]}" name="rating" value="1" required/>
                        <label for="star1_{row[0]}" title="1 star"></label>
                    </div><br>
                    <h6>Comment</h6>
                    <textarea name="comment" placeholder="Your comment" required></textarea><br>
                                    <input type="submit" class="btn btn-save" style="background-color:green;color:white;" value="Submit" name="sub">
                </form>
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
                    <td>{rating[5]}</td>
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
                <div class="text-center mt-3">
                    <a id="videoDownloadBtn" href="" download class="btn btn-primary">
                        <i class="fas fa-download"></i> Download Video
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
function playVideo(videoName) {
    const modal = document.getElementById('videoModal');
    const videoContainer = document.getElementById('videoContainer');
    const downloadBtn = document.getElementById('videoDownloadBtn');
    videoContainer.innerHTML = '';
    const video = document.createElement('video');
    video.style.width = '100%';
    video.src = `Visitor_Recipe/${videoName}`;
    videoContainer.appendChild(video);
    downloadBtn.href = `Visitor_Recipe/${videoName}`;
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
if "sub" in form:
    recipeid = form.getvalue("recipeid")
    rating = form.getvalue("rating")
    comment = form.getvalue("comment")
    query = "SELECT COUNT(*) FROM recipe_ratings WHERE chefid = %s AND recipeid = %s"
    cur.execute(query, (chefid, recipeid))
    review_count = cur.fetchone()[0]

    if review_count > 0:
        print("""
            <script>
            alert("You have already reviewed this recipe.");
            </script>
            """)
    else:
        q = """INSERT INTO recipe_ratings(rating, comment, chefName, chefid, designation, status, recipeid) 
               VALUES (%s, %s, %s, %s, %s, 'Pending', %s)"""
        cur.execute(q, (rating, comment, chefName, chefid, designation, recipeid))
        con.commit()


        q1 = "SELECT COUNT(*) FROM recipe_ratings WHERE recipeid = %s"
        cur.execute(q1, (recipeid,))
        rating_count = cur.fetchone()[0]
        if rating_count >= 2:
            q3 = "SELECT AVG(rating) FROM recipe_ratings WHERE recipeid = %s"
            cur.execute(q3, (recipeid,))
            average_rating = cur.fetchone()[0]

            status = "Low Rated" if average_rating < 3 else "High Rated"

            q4 = "UPDATE recipe_ratings SET status = %s WHERE recipeid = %s"
            cur.execute(q4, (status, recipeid))

            q5 = "UPDATE food_recipes SET status = %s WHERE recipeid = %s"
            cur.execute(q5, (status, recipeid))

            con.commit()

        print("""
            <script>
            alert("Review added successfully!");
            </script>
            """)

cur.close()
con.close()