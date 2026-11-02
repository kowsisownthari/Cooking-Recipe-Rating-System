#!C:/Users/Home/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb
import cgi
import pymysql, os

cgitb.enable()
form = cgi.FieldStorage()
con = pymysql.connect(host="localhost", user="root", password="", database="rating_system")
cur = con.cursor()
q2 = """Select * From food_recipes where status='Accept'"""
cur.execute(q2)
highly_rated_recipes = cur.fetchall()
cur.execute("""
    SELECT 
        fr.recipeid,
        fr.Recipe_Name,
        fr.mainCategory,
        fr.duration,
        fr.Name,
        AVG(rr.rating) as avg_rating,
        COUNT(rr.rating) as rating_count
    FROM food_recipes fr
    JOIN recipe_ratings rr ON fr.recipeid = rr.recipeid
    WHERE rr.status = 'High Rated'
    GROUP BY fr.recipeid
    ORDER BY avg_rating DESC, rating_count DESC
    LIMIT 3
""")

print("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Browse Recipe</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/js/all.min.js"></script>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<style>
    :root {
        --primary-color: #ff6b6b;
        --secondary-color: #ffd93d;
    }

    .hero-section {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        min-height: 100vh;
        color: white;
    }

    .feature-card {
        transition: transform 0.3s ease;
        cursor: pointer;
        border-radius: 15px;
        overflow: hidden;
    }

    .feature-card:hover {
        transform: translateY(-10px);
    }

    .recipe-card {
        border-radius: 15px;
        overflow: hidden;
        transition: transform 0.3s ease;
    }

    .recipe-card:hover {
        transform: translateY(-5px);
    }

    .navbar {
        background: purple;
    }

    .custom-shape {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        overflow: hidden;
        line-height: 0;
    }

    .custom-shape svg {
        position: relative;
        display: block;
        width: calc(100% + 1.3px);
        height: 150px;
    }

    .rating {
        color: var(--secondary-color);
        font-size: 24px;
    }

    .recipe-stats {
        font-size: 0.9rem;
        color: #666;
    }

    .floating {
        animation: float 3s ease-in-out infinite;
    }

    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }
        

    .category-badge {
        background: var(--primary-color);
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 0.9rem;
    }
    .card-img-top{
    height:200px;
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
     .search-container {
            margin: 20px 0;
            display: flex;
            justify-content: center;
            gap: 10px;
            
        }
        .search-container input {
            width: 300px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .search-container button {
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .no-results {
            text-align: center;
            padding: 20px;
            background-color: #f8d7da;
            color: #721c24;
            border-radius: 4px;
            margin: 20px;
            display: none;
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
<nav class="navbar navbar-expand-lg navbar-dark fixed-top">
    <div class="container">
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
                    <a class="nav-link dropdown-toggle" href="" id="loginDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Register
                    </a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="Visitor_Register.py">Visitor</a></li>
                        <li><a class="dropdown-item" href="Student_Register.py">Cookery Student</a></li>
                        <li><a class="dropdown-item" href="Chef_Register.py">Chef</a></li>
                    </ul>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="" id="loginDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Login
                    </a>
                    <ul class="dropdown-menu">
                         <li><a class="dropdown-item" href="Visitor_Login.py">Visitor</a></li>
                        <li><a class="dropdown-item" href="Student_Login.py">Cookery Student</a></li>
                        <li><a class="dropdown-item" href="Chef_login.py">Chef</a></li>
                        <li><a class="dropdown-item" href="Admin_Login.py">Login</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</nav>
""")
print("""
    <div class="col-md-10 main-content" style="margin-left:35vh;">
        <center><h3 style="margin-top:20px;">Recipe collection</h3></center><br>
        <div class="container" style="margin-left:-200px; margin-top:100px;">
            <div class="search-container">
                <input type="text" id="searchInput" placeholder="Search by chef, recipe, category...">
                <button onclick="searchRecipes()">Search</button>
            </div>

            <div id="noMatchMessage"></div>
            <div class="table-section">
                <div class="table-responsive" id="recipeTableContainer" style="margin-left:100px;">
                    <table class="table table-bordered table-striped">
                        <thead>
                            <tr>
                                <th>Serial No.</th>
                                <th>Name</th>
                                <th>Designation</th>
                                <th>Recipe Name</th>
                                <th>Main Category</th>
                                <th>Recipe Video</th>
                                <th>Other Details</th>
                            </tr>
                        </thead>
                        <tbody id="recipeTableBody">
""")

serial_no = 1
for row in highly_rated_recipes:
    ratings_query = "SELECT * FROM recipe_ratings WHERE recipeid=%s"
    cur.execute(ratings_query, (row[0],))
    ratings_data = cur.fetchall()
    steps = row[2].split(',') if row[2] else []
    ingredients = row[6].split(',') if row[6] else []
    quantities = row[7].split(',') if row[7] else []

    # Generate steps and ingredients HTML
    steps_html = "".join([f"""
        <div class="step-box">
            <div class="step-number">Step {i + 1}</div>
            <div class="step-text">{step.strip()}</div>
        </div>
    """ for i, step in enumerate(steps)])

    ingredients_html = "".join([f"""
        <div class="ingredient-box">
            <div class="ingredient-name">{ingredients[i].strip()}</div>
            <div class="ingredient-quantity">{quantities[i].strip() if i < len(quantities) else ''}</div>
        </div>
    """ for i in range(len(ingredients))])

    # Print the table row with the modal
    print(f"""
        <tr>
            <td>{serial_no}</td>
            <td>{row[11]}</td>
            <td>{row[14]}</td>
            <td>{row[1]}</td>
            <td>{row[4]}</td>
            <td>
                <button class="video-play-btn" onclick="playVideo('{row[10]}')">
                    <i class="fas fa-play"></i> Play Video
                </button>
            </td>
            <td>
                <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modal{row[0]}">
                    Recipe Details
                </button>

                <!-- Modal -->
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
                                            <p><strong>Email:</strong> {row[12]}</p>
                                            <p><strong>Recipe Name:</strong> {row[1]}</p>
                                            <p><strong>Main Category:</strong> {row[4]}</p>
                                            <p><strong>Sub Category:</strong> {row[5]}</p>
                                            <p><strong>Keywords:</strong> {row[8]}</p>
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

    <!-- Video Modal -->
    <div class="modal fade" id="videoModal" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Recipe Video</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div id="videoContainer"></div>
                </div>
            </div>
        </div>
    </div>
""")

print(""""
<script>
 function playVideo(videoName) {
        const modal = document.getElementById('videoModal');
        const videoContainer = document.getElementById('videoContainer');
        videoContainer.innerHTML = `
            <div class="alert alert-info" role="alert">
                <h4 class="alert-heading">Login Required</h4>
                <p>Please log in to view this recipe video.</p>
                <hr>
                <p class="mb-0">
                    <a href="Visitor_Login.py" class="btn btn-primary">Login as Visitor</a>
                    <a href="Student_Login.py" class="btn btn-secondary">Login as Student</a>
                    <a href="Chef_login.py" class="btn btn-success">Login as Chef</a>
                </p>
            </div>
        `;
        const modalInstance = new bootstrap.Modal(modal);
        modalInstance.show();
    }
function searchRecipes() {
    var input = document.getElementById("searchInput");
    var filter = input.value.toLowerCase();
    var table = document.getElementById("recipeTableBody");
    var tr = table.getElementsByTagName("tr");
    var noMatch = true;
    var existingNoMatch = document.getElementById("noMatchRow");
    if (existingNoMatch) {
        existingNoMatch.remove();
    }
    for (var i = 0; i < tr.length; i++) {
        var chefName = tr[i].getElementsByTagName("td")[1]; 
        var recipeName = tr[i].getElementsByTagName("td")[3]; 
        var category = tr[i].getElementsByTagName("td")[4]; 

        if (chefName && recipeName && category) {
            var txtChef = chefName.textContent || chefName.innerText;
            var txtRecipe = recipeName.textContent || recipeName.innerText;
            var txtCategory = category.textContent || category.innerText;

            if (txtChef.toLowerCase().indexOf(filter) > -1 || 
                txtRecipe.toLowerCase().indexOf(filter) > -1 || 
                txtCategory.toLowerCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
                noMatch = false;
            } else {
                tr[i].style.display = "none";
            }
        }
    }

    if (noMatch && filter !== "") {
        var noMatchRow = table.insertRow();
        noMatchRow.id = "noMatchRow";
        var cell = noMatchRow.insertCell(0);
        cell.colSpan = "7";
        cell.style.textAlign = "center";
        cell.innerHTML = "No match found";
    }
}
    </script>

</body>
</html>
""")