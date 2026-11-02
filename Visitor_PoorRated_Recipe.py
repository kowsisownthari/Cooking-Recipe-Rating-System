#!C:/Users/Home/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb
import cgi
import pymysql

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
q2 = """
SELECT fr.recipeid, fr.Recipe_Name, fr.mainCategory, fr.subCategory, fr.keyword, fr.duration, fr.Steps, fr.ingredients, fr.quantities, fr.video, fr.Name,fr.cookery_id,
       MAX(rr.rating) as rating, MAX(rr.comment) as comment, MAX(rr.chefName) as chefName
FROM food_recipes fr
JOIN recipe_ratings rr ON rr.recipeid = fr.recipeid
WHERE fr.Name = %s AND fr.cookery_id=%s and rr.status = 'Low Rated'
GROUP BY fr.recipeid
"""
cur.execute(q2, (Name,id))
emp_application_data = cur.fetchall()
print(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Visitor Poor Rated Recipes</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
        <style>
          * {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Open sans', sans-serif;
}}
.sidebar {{
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
}}

.sidebar .sidebar-header {{
    text-align: center;
    padding: 20px;
}}

.sidebar .dropdown-menu {{
        background: #11152d;
    }}
    .sidebar .dropdown-menu a {{
        color: #fff;
        padding: 10px 20px;
    }}
    .sidebar .dropdown-menu a:hover {{
        background-color: #0056b3;
    }}

.sidebar .navbar-nav {{
    list-style: none;
    padding-left: 0;
}}

.sidebar .navbar-nav li {{
    display: block;
}}

.sidebar .navbar-nav a {{
    display: flex;
    align-items: center;
    color: white;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: 500;
    text-decoration: none;
    border-radius: 0 30px 30px 0;
    transition: background-color 0.3s, color 0.3s;
}}

.sidebar .navbar-nav a i {{
    background-color: #e9ecef;
    color: #11152d;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    margin-right: 10px;
}}


.sidebar .navbar-nav a:hover,
.sidebar .navbar-nav a.active {{
    background-color: white;
    color: blue;
}}

.sidebar .navbar-nav a:hover i,
.sidebar .navbar-nav a.active i {{
    background-color: blue;
    color: white;
}}
        }}
        body {{
            background: #f0f2f5;
            color: #333;
            font-size: 16px;
        }}

        .header {{
            text-align: center; 
            margin-top: -55px;
        }}

        .header h2 {{
            font-size: 26px;
            color: black;
            margin-top: 100px;
        }}
        .header h1 {{
            font-size: 26px;
            color: black;
            margin-bottom: 100px;
        }}
        
        .side-menu {{
            background: #11152d;
            color: white;
            padding-top: 30px;
            box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
            height: 100vh;
            position: fixed;
            top: 0;
            left: 0;
            width: 250px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            transition: width 0.3s;
        }}
        .side-menu:hover {{
            width: 270px; 
        }}
        .side-menu a {{
            color: white;
            text-decoration: none;
            padding: 15px 20px;
            display: block;
            width: 100%;
            text-align: center;
            margin-bottom: 20px;
            transition: background-color 0.3s, padding 0.3s;
        }}
        .side-menu a i {{
            margin-right: 10px;
            font-size: 18px;
        }}
        .side-menu a:hover {{
            background-color: #0077b6;
            padding-left: 25px;
        }}
        .side-menu ul {{
            padding-left: 0;
            width: 100%;
        }}
        .side-menu ul li {{
            list-style: none;
            width: 100%;
        }}
        .logout-button {{
            margin-bottom: 30px; 
            width: 80%;
            background-color: #ff4b5c;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 25px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
        }}
        .logout-button:hover {{
            background-color: #ff6b7a;
            transform: scale(1.05);
        }}
        .modal-content {{
            border-radius: 15px;
        }}
        .modal-header, .modal-footer {{
            background: rgb(14, 14, 57);
            color: white;
            border-top-left-radius: 15px;
            border-top-right-radius: 15px;
        }}
        .modal-header .btn-close {{
            background-color: white;
            border: none;
        }}
        .employee-name {{
            font-size: 22px;
            font-weight: bold;
            color: #0077b6;
            margin-bottom: 500px;
            justify-content: center;
            align-items: center;
        }}
        .table-section {{
            background: white;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);

.form-group {{
    margin-bottom: 15px; 
}}
.step-input-group, .ingredient-input-group {{
    display: flex;
    align-items: center;
    margin-bottom: 8px;
    gap: 8px; 
}}
.ingredient-input-group {{
    display: grid;
    grid-template-columns: 1fr 1fr auto;
    align-items: center;
}}
.video-play-btn {{
    background-color: #0077b6;
    color: white;
    border: none;
    padding: 8px 15px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}}
.video-play-btn:hover {{
    background-color: #005c8a;
}}
.video-container {{
    position: relative;
    padding-bottom: 56.25%;
    height: 0;
    overflow: hidden;
}}
.step-box {{
    display: flex;
    align-items: center;
    margin-bottom: 10px;
}}
.step-number {{
    font-weight: bold;
    margin-right: 10px;
    min-width: 70px;
}}
.step-text {{
    flex-grow: 1;
}}
.ingredient-box {{
    display: flex;
    align-items: center;
    margin-bottom: 8px;
}}
.ingredient-name {{
    flex: 1;
    margin-right: 10px;
}}
.ingredient-quantity {{
    flex: 1;
    text-align: left;
}}
.form-group label {{
    display: block;
    margin-bottom: 4px; 
    font-weight: 500;
}}

.form-control {{
    padding: 6px 8px;
    height: 32px; 
    font-size: 14px; }}

.ingredients-container, .steps-container {{
    margin-top: 4px;
}}
 .video-play-btn {{
            background-color: #0077b6;
            color: white;
            border: none;
            padding: 8px 15px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }}

        .video-play-btn:hover {{
            background-color: #005c8a;
        }}
        .video-container {{
position: relative;
            padding-bottom: 56.25%;
            height: 0;
            overflow: hidden;
        }}
        .video-container video {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }}
    </style>
</head>
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
    <center><h3 style="margin-top:20px;">Poor Rated Recipe</h3></center><br>
    <div class="table-section">
        <div class="table-responsive">
            <table class="table table-bordered table-striped">
                <thead>
                    <tr>
                        <th>Serial No.</th>

                        <th>Recipe Name</th>
                        <th>Recipe Id</th>
                        <th>Main Category</th>
                         <th>Sub Category</th>
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

    steps = row[6].split(',') if row[6] else []
    ingredients = row[7].split(',') if row[7] else []
    quantities = row[8].split(',') if row[8] else []

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
            <td>{row[0]}</td>

                <td>{row[2]}</td>
                <td>{row[3]}</td>
            <td>
               <div class="d-flex gap-2">
                    <button class="video-play-btn" onclick="playVideo('{row[9]}')">
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
                                                <p><strong>Name:</strong>{row[10]} </p>
                                            </div>
                                            <div class="form-group">
                                                <p><strong>ID:</strong>{row[11]} </p>
                                            </div>
                                         <div class="form-group">
                                                <p><strong>Recipe Name:</strong>{row[1]} </p>
                                            </div>
                                            <div class="form-group">
                                                <p><strong>Main Category:</strong>{row[2]} </p>
                                            </div>
                                            <div class="form-group">
                                                <p><strong>Sub Category:</strong> {row[3]}</p>
                                            </div>
                                            <div class="form-group">
                                                <p><strong>Keywords:</strong> {row[4]}</p>
                                            </div>
                                            <div class="form-group">
                                                <p><strong>Cooking Duration:</strong> {row[5]}</p>
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