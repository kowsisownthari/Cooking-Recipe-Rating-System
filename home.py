#!C:/Users/Home/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb
import cgi
import pymysql, os
cgitb.enable()
form = cgi.FieldStorage()
con = pymysql.connect(host="localhost", user="root", password="", database="rating_system")
cur = con.cursor()
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
top_recipes = cur.fetchall()
def generate_stars(rating):
    full_stars = int(rating)
    has_half = (rating - full_stars) >= 0.5
    empty_stars = 5 - full_stars - (1 if has_half else 0)

    stars_html = ''
    stars_html += '<i class="fas fa-star"></i>' * full_stars
    if has_half:
        stars_html += '<i class="fas fa-star-half-alt"></i>'
    stars_html += '<i class="far fa-star"></i>' * empty_stars

    return stars_html
print("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Home</title>
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
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
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

    .search-bar {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 50px;
        padding: 10px 20px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
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
                        <li><a class="dropdown-item" href="Admin_Login.py">Admin</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</nav>
<section id="home" class="hero-section position-relative d-flex align-items-center">
    <div class="container">
        <div class="row align-items-center">
            <div class="col-lg-6">
                <h1 class="display-4 fw-bold mb-4">Discover & Rate Amazing Recipes</h1>
                <p class="lead mb-4">Join our community of food lovers to find, share, and rate the best recipes from around the world.</p>
               
                <a href="Home_Share_Recipe.py" class="btn btn-light btn-lg me-3"">Share Recipe</a>
                 <a href="Browse_Recipe.py" class="btn btn-primary btn-lg">Browse Recipes</a>
            </div>
            <div class="col-lg-6">
                <div class="image-container" style="background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); border-radius: 15px; padding: 20px;">
                    <img src="istockphoto-1139747523-612x612.jpg" alt="Delicious Food" class="img-fluid floating rounded-3" style="mix-blend-mode: multiply;">
                </div>
            </div>
        </div>
    </div>
    <div class="custom-shape">
        <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
            <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V120H0V0C50.45,22.34,121.09,43.44,195.97,62.32Z" fill="#fff"></path>
        </svg>
    </div>
</section>""")


print("""
<section id="recipes" class="py-5">
    <div class="container">
        <h2 class="text-center mb-5">Top Rated Recipes</h2>
        <div class="row g-4">
""")

for recipe in top_recipes:
    recipeid, Recipe_Name, mainCategory, duration, Name, avg_rating, rating_count = recipe

    print(f"""
        <div class="col-md-4">
            <div class="card recipe-card h-100 border-0 shadow">
                <div class="card-body">
                    <div class="d-flex justify-content-between align-items-center mb-2">
                        <span class="category-badge">{mainCategory}</span>
                        <div class="rating">
                            {generate_stars(float(avg_rating))}
                        </div>
                    </div>
                    <h5 class="card-title">{Recipe_Name}</h5>
                    <div class="recipe-stats d-flex justify-content-between mb-3">
                        <span><i class="far fa-clock"></i> {duration} </span>
                        <span><i class="far fa-user"></i> By {Name}</span>
                    </div>
                    <div class="d-flex justify-content-between align-items-center">
                        <small class="text-muted">{rating_count} ratings</small>
                        <button class="btn btn-primary" onclick="window.location.href='Browse_Recipe.py'">
                            View Recipe
                        </button>
                    </div>
                </div>
            </div>
        </div>
    """)
print("""
        </div>
    </div>
</section>
""")
print(""""
<section id="categories" class="py-5 bg-light">
    <div class="container">
        <h2 class="text-center mb-5">Popular Categories</h2>
        <div class="row g-4">
            <div class="col-md-3 col-6">
                <div class="card feature-card text-center border-0 shadow h-100">
                    <div class="card-body">
                        <i class="fas fa-pizza-slice display-4 text-primary mb-3"></i>
                        <h5>Italian</h5>
                        <p class="text-muted">150+ Recipes</p>
                    </div>
                </div>
            </div>
            <div class="col-md-3 col-6">
                <div class="card feature-card text-center border-0 shadow h-100">
                    <div class="card-body">
                        <i class="fas fa-drumstick-bite display-4 text-primary mb-3"></i>
                        <h5>Asian</h5>
                        <p class="text-muted">200+ Recipes</p>
                    </div>
                </div>
            </div>
            <div class="col-md-3 col-6">
                <div class="card feature-card text-center border-0 shadow h-100">
                    <div class="card-body">
                        <i class="fas fa-birthday-cake display-4 text-primary mb-3"></i>
                        <h5>Desserts</h5>
                        <p class="text-muted">120+ Recipes</p>
                    </div>
                </div>
            </div>
            <div class="col-md-3 col-6">
                <div class="card feature-card text-center border-0 shadow h-100">
                    <div class="card-body">
                        <i class="fas fa-leaf display-4 text-primary mb-3"></i>
                        <h5>Vegetarian</h5>
                        <p class="text-muted">180+ Recipes</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
<footer class="bg-dark text-light py-4">
    <div class="container">
        <div class="row">
            <div class="col-md-4 mb-4 mb-md-0">
                <img src="download (10).jpeg" style="width:75px;height:75px;border-radius:50px;">
            </div>
            <div class="col-md-4 mb-4 mb-md-0">
              <center> <h5>TasteRate</h5>
                <p>Discover, share, and rate the best recipes from around the world.</p><center>
                </div>
                <div class="col-md-4">
                      <center>  <script>
                var a = new Date();
                var year = a.getFullYear();
                document.write("Copyright claimed @ " + year + ". All rights reserved.");
              </script> </center
                </div>
            </div>
         
        </div>
    </footer>

</body>
</html>
""")