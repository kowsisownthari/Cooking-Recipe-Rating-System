#!C:/Users/Home/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb
import cgi
import pymysql, os
cgitb.enable()
form = cgi.FieldStorage()
con = pymysql.connect(host="localhost", user="root", password="", database="rating_system")
cur = con.cursor()
userid = form.getvalue("id")
q = """select * from visitor_register where id='%s'""" % (userid)
cur.execute(q)
det = cur.fetchall()
Name = det[0][1]
id=det[0][0]

q2 = "SELECT * FROM food_recipes WHERE cookery_id='%s' and status='Accept'"%(userid)
cur.execute(q2)
accepted_recipes = cur.fetchall()
recipeid = ""
for row in accepted_recipes:
    recipeid = row[0]
q3 = "SELECT * FROM food_recipes WHERE cookery_id='%s' and status='Reject'"%(userid)
cur.execute(q3)
rejected_recipes = cur.fetchall()
recipeid = ""
for row in rejected_recipes:
    recipeid = row[0]
print("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Visitor Existing Recipe</title>
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
.btn-add-step {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 4px 12px; 
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
    margin-top: 8px;
}

.btn-add-step:hover {
    background-color: #218838;
}

.form-group {
    margin-bottom: 15px; 
}
.form-group label {
    display: block;
    margin-bottom: 4px; 
    font-weight: 500;
}
.form-control {
    padding: 6px 8px;
    height: 32px;
    font-size: 14px; }

.ingredients-container, .steps-container {
    margin-top: 4px;
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
 .new-item .btn-remove-step {
            display: inline-block;
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
.btn-remove-step {
    background-color: #dc3545;
    color: white;
    border: none;
    width: 25px;
    height: 25px; 
    border-radius: 50%;
    display: none;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: background-color 0.3s;
    padding: 0;
}
.new-item .btn-remove-step {
    display: flex;
}
.btn-remove-step:hover {
    background-color: #c82333;
}
.btn-remove-step i {
    font-size: 12px; 
}
.btn-add-step {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 4px 12px; 
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
    margin-top: 8px;
}
.btn-add-step:hover {
    background-color: #218838;
}
</style>
</head>""")
print(f"""
<body>
 <div id="sidebarmenu" class="sidebar">
        <nav class="sidenavbar">
            <div class="navbar-nav">
                <a href="Visitor_Dashboard.py?id={userid}"><i class="fas fa-th-large"></i>Dashboard</a>

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


    </div>
 <div class="col-md-10 main-content" style="margin-left:45vh;width:1000px">
            <h2>Published Recipes</h2><br>
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
                                <th>Recipe Video</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
""")

serial_no = 1

for row in accepted_recipes:
        ratings_query = "SELECT * FROM recipe_ratings WHERE recipeid=%s"
        cur.execute(ratings_query, (row[0],))
        ratings_data = cur.fetchall()
        steps = row[2].split(',') if row[2] else []
        ingredients = row[6].split(',') if row[6] else []
        quantities = row[7].split(',') if row[7] else []

        print(f"""
            <tr>
                <td>{serial_no}</td>
               
                <td>{row[1]}</td>
                <td>{row[4]}</td>
                <td>{row[5]}</td>
                 <td>{row[11]}</td>
                <td>
               <button class="video-play-btn" onclick="playVideo('{row[10]}')">
                <i class="fas fa-play"></i> Play Video
            </button>
        </td>
                <td>
                    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modal{row[0]}">
                        Edit Recipe
                    </button>
     <button class="btn btn-success btn-sm" data-bs-toggle="modal" data-bs-target="#ratingsModal{row[0]}">
                        View Ratings
                    </button>
                    <div class="modal fade" id="modal{row[0]}" tabindex="-1" aria-hidden="true">
                        <div class="modal-dialog modal-lg">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title">Edit Recipe Details</h5>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                <form id="editForm{row[0]}"  method="post" enctype="multipart/form-data">
                                         <input type="hidden" name="recipeid" value="{row[0]}" class="form-control" >

                                    <div class="modal-body">
                                        <div class="row">
                                            <div class="col-md-6">
                                               <div class="form-group">
                                            <h6><Strong>Name:</strong>{row[11]}</h6>
                                            </div>
                                            <div class="form-group">
                                            <h6><Strong>ID:</strong>{row[12]}</h6>
                                            </div>
                                                <div class="form-group">
                                                    <label>Recipe Name:</label>
                                                    <input type="text" name="recipe_name" value="{row[1]}" class="form-control">
                                                </div>
                                                <div class="form-group">
                                                    <label>Main Category:</label>
                                                    <input type="text" name="main_category" value="{row[4]}" class="form-control">
                                                </div>
                                                <div class="form-group">
                                                    <label>Sub Category:</label>
                                                    <input type="text" name="sub_category" value="{row[5]}" class="form-control">
                                                </div>
                                                  <div class="form-group">
                                                    <label>Keywords:</label>
                                                    <input type="text" name="keywords" value="{row[8]}" class="form-control">
                                                </div>
                                               <div class="form-group">
                                                    <label>Cooking Duration:</label>
                                                    <input type="text" name="duration" value="{row[3]}" class="form-control">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="form-group">
                                                    <label>Cooking Steps:</label>
                                                    <div class="steps-container" id="steps-container-{row[0]}">
                                                        {''.join(f'''
                                                        <div class="step-input-group">
                                                            <input type="text" name="steps[]" value="{step.strip()}" class="form-control" placeholder="Enter step">
                                                            <button type="button" class="btn-remove-step" onclick="removeStep(this)">
                                                                <i class="fas fa-times"></i>
                                                            </button>
                                                        </div>
                                                        ''' for step in steps)}
                                                    </div>
                                                    <button type="button" class="btn-add-step" onclick="addStep('steps-container-{row[0]}')">
                                                        <i class="fas fa-plus"></i> Add Step
                                                    </button>
                                                </div>

                                                <div class="form-group">
                                                    <label>Ingredients and Quantities:</label>
                                                    <div class="ingredients-container" id="ingredients-container-{row[0]}">
                                                        {''.join(f'''
                                                        <div class="ingredient-input-group">
                                                            <input type="text" name="ingredients[]" value="{ingredients[i].strip()}" class="form-control ingredient-name" placeholder="Ingredient">
                                                            <input type="text" name="quantities[]" value="{quantities[i].strip() if i < len(quantities) else ''}" class="form-control ingredient-quantity" placeholder="Quantity">
                                                            <button type="button" class="btn-remove-step" onclick="removeIngredient(this)">
                                                                <i class="fas fa-times"></i>
                                                            </button>
                                                        </div>
                                                        ''' for i in range(len(ingredients)))}
                                                    </div>
                                                    <button type="button" class="btn-add-step" onclick="addIngredient('ingredients-container-{row[0]}')">
                                                        <i class="fas fa-plus"></i> Add Ingredient
                                                    </button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="modal-footer">
                                        <input type="submit" class="btn btn-save" style="background-color:green;color:white;" value="Save Changes" name="sub">
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div class="modal fade" id="videoModal" tabindex="-1" aria-hidden="true">
                        <div class="modal-dialog modal-lg">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title">Recipe Video</h5>
                                    <input type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" >
                                </div>
                                <div class="modal-body">
                                    <div class="video-container" id="videoContainer"></div>
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
                                                <th> Name</th>
                                                 <th>Id</th>
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
            print("<tr><td colspan='4' class='text-center'>No ratings yet</td></tr>")
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

        <h2>Rejected Recipes</h2><br>
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
                            <th>Recipe Video</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
""")

serial_no = 1

for row in rejected_recipes:
    ratings_query = "SELECT * FROM recipe_ratings WHERE recipeid=%s"
    cur.execute(ratings_query, (row[0],))
    ratings_data = cur.fetchall()
    steps = row[2].split(',') if row[2] else []
    ingredients = row[6].split(',') if row[6] else []
    quantities = row[7].split(',') if row[7] else []

    print(f"""
        <tr>
            <td>{serial_no}</td>
            
            <td>{row[1]}</td>
            <td>{row[4]}</td>
            <td>{row[5]}</td>
            <td>{row[11]}</td>
            <td>
           <button class="video-play-btn" onclick="playVideo('{row[10]}')">
            <i class="fas fa-play"></i> Play Video
        </button>
    </td>
            <td>
                <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modal{row[0]}">
                    Edit Recipe
                </button>
 <button class="btn btn-success btn-sm" data-bs-toggle="modal" data-bs-target="#ratingsModal{row[0]}">
                    View Ratings
                </button>
                <div class="modal fade" id="modal{row[0]}" tabindex="-1" aria-hidden="true">
                    <div class="modal-dialog modal-lg">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title">Edit Recipe Details</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <form id="editForm{row[0]}"  method="post" enctype="multipart/form-data">
                                                            <input type="hidden" name="recipeid" value="{row[0]}" class="form-control" >

                                <div class="modal-body">
                                    <div class="row">
                                        <div class="col-md-6">
                                           <div class="form-group">
                                            <h6><Strong>Name:</strong>{row[11]}</h6>
                                            </div>
                                            <div class="form-group">
                                            <h6><Strong>ID:</strong>{row[12]}</h6>
                                            </div>
                                            <div class="form-group">
                                                <label>Recipe Name:</label>
                                                <input type="text" name="recipe_name" value="{row[1]}" class="form-control">
                                            </div>
                                            <div class="form-group">
                                                <label>Main Category:</label>
                                                <input type="text" name="main_category" value="{row[4]}" class="form-control">
                                            </div>
                                            <div class="form-group">
                                                <label>Sub Category:</label>
                                                <input type="text" name="sub_category" value="{row[5]}" class="form-control">
                                            </div>
                                              <div class="form-group">
                                                <label>Keywords:</label>
                                                <input type="text" name="keywords" value="{row[8]}" class="form-control">
                                            </div>
                                           <div class="form-group">
                                                <label>Cooking Duration:</label>
                                                <input type="text" name="duration" value="{row[3]}" class="form-control">
                                            </div>
                                        </div>
                                        <div class="col-md-6">
                                            <div class="form-group">
                                                <label>Cooking Steps:</label>
                                                <div class="steps-container" id="steps-container-{row[0]}">
                                                    {''.join(f'''
                                                    <div class="step-input-group">
                                                        <input type="text" name="steps[]" value="{step.strip()}" class="form-control" placeholder="Enter step">
                                                        <button type="button" class="btn-remove-step" onclick="removeStep(this)">
                                                            <i class="fas fa-times"></i>
                                                        </button>
                                                    </div>
                                                    ''' for step in steps)}
                                                </div>
                                                <button type="button" class="btn-add-step" onclick="addStep('steps-container-{row[0]}')">
                                                    <i class="fas fa-plus"></i> Add Step
                                                </button>
                                            </div>

                                         

                                            <div class="form-group">
                                                <label>Ingredients and Quantities:</label>
                                                <div class="ingredients-container" id="ingredients-container-{row[0]}">
                                                    {''.join(f'''
                                                    <div class="ingredient-input-group">
                                                        <input type="text" name="ingredients[]" value="{ingredients[i].strip()}" class="form-control ingredient-name" placeholder="Ingredient">
                                                        <input type="text" name="quantities[]" value="{quantities[i].strip() if i < len(quantities) else ''}" class="form-control ingredient-quantity" placeholder="Quantity">
                                                        <button type="button" class="btn-remove-step" onclick="removeIngredient(this)">
                                                            <i class="fas fa-times"></i>
                                                        </button>
                                                    </div>
                                                    ''' for i in range(len(ingredients)))}
                                                </div>
                                                <button type="button" class="btn-add-step" onclick="addIngredient('ingredients-container-{row[0]}')">
                                                    <i class="fas fa-plus"></i> Add Ingredient
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="modal-footer">
                                    <input type="submit" class="btn btn-save" style="background-color:green;color:white;" value="Save Changes" name="sub">
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
                <div class="modal fade" id="videoModal" tabindex="-1" aria-hidden="true">
                    <div class="modal-dialog modal-lg">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title">Recipe Video</h5>
                                <input type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" >
                            </div>
                            <div class="modal-body">
                                <div class="video-container" id="videoContainer"></div>
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
                                            <th> Name</th>
                                             <th>Id</th>
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
        print("<tr><td colspan='4' class='text-center'>No ratings yet</td></tr>")
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
    </div>
    <script>
        function addStep(containerId) {
            const container = document.getElementById(containerId);
            const stepDiv = document.createElement('div');
            stepDiv.className = 'step-input-group new-item';
            stepDiv.innerHTML = `
                <input type="text" name="steps[]" class="form-control" placeholder="Enter step">
                <button type="button" class="btn-remove-step" onclick="removeStep(this)">
                    <i class="fas fa-times"></i>
                </button>
            `;
            container.appendChild(stepDiv);
        }
        function addIngredient(containerId) {
            const container = document.getElementById(containerId);
            const ingredientDiv = document.createElement('div');
            ingredientDiv.className = 'ingredient-input-group new-item';
            ingredientDiv.innerHTML = `
                <input type="text" name="ingredients[]" class="form-control ingredient-name" placeholder="Ingredient">
                <input type="text" name="quantities[]" class="form-control ingredient-quantity" placeholder="Quantity">
                <button type="button" class="btn-remove-step" onclick="removeIngredient(this)">
                    <i class="fas fa-times"></i>
                </button>
            `;
            container.appendChild(ingredientDiv);
        }
        function removeStep(button) {
            button.closest('.step-input-group').remove();
        }
        function removeIngredient(button) {
            button.closest('.ingredient-input-group').remove();
        }
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
recipeid = form.getvalue("recipeid")
Recipe_Name = form.getvalue("recipe_name")
mainCategory = form.getvalue("main_category")
subCategory = form.getvalue("sub_category")
keyword = form.getvalue("keywords")
duration = form.getvalue("duration")
Steps = ','.join(form.getlist("steps[]")) if form.getlist("steps[]") else ''
ingredients = ','.join(form.getlist("ingredients[]")) if form.getlist("ingredients[]") else ''
quantities = ','.join(form.getlist("quantities[]")) if form.getlist("quantities[]") else ''
submit = form.getvalue("sub")
if submit:
    q = "UPDATE food_recipes SET Recipe_Name='%s',mainCategory='%s',subCategory='%s',keyword='%s',duration='%s',Steps='%s',ingredients='%s',quantities='%s',status='pending' WHERE recipeid='%s'"%(Recipe_Name, mainCategory, subCategory, keyword, duration, Steps, ingredients, quantities, recipeid)
    cur.execute(q)
    con.commit()
    print("""
    <script>
    alert("Updated.");
    </script>
    """)
con.close()