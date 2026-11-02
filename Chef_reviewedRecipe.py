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
q = """select * from chef_register where id='%s'""" %(userid)
cur.execute(q)
det = cur.fetchall()
chefName = det[0][1]
chef_id=det[0][20]
q2 = """
SELECT fr.recipeid, fr.Recipe_Name,fr.mainCategory,fr.subCategory,fr.Name, rr.rating, rr.comment,fr.cookery_id,fr.duration,fr.Steps,fr.ingredients,fr.quantities,fr.keyword
FROM food_recipes fr
JOIN recipe_ratings rr ON rr.recipeid = fr.recipeid
WHERE rr.chefName = %s and chefid=%s
"""
cur.execute(q2, (chefName,chef_id))
emp_application_data = cur.fetchall()
print(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chef Reviewed Recipes</title>
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
       .btn-remove-step {{
            background-color: white;
            color: white;
            border: none;
            padding: 5px 10px;
            border-radius: 4px;
            display: none; 
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
.form-group {{
    margin-bottom: 15px; 
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


    </style>
</head>
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
            <h2>Reviewed Recipe</h2><br>
            <div class="table-section">
                <div class="table-responsive">
                    <table class="table table-bordered table-striped">
                        <thead>
                            <tr>
                                <th>Serial No.</th>
                                
                                <th>Recipe id</th>
                                <th>Recipe Name</th>
                                <th>Main Category</th>
                                <th>Sub Category</th>
                                 <th>Added By</th>
                                <th>Rating</th>
                                <th>Comments</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
""")
serial_no = 1
for row in emp_application_data:
    steps = row[9].split(',') if row[9] else []
    ingredients = row[10].split(',') if row[10] else []
    quantities = row[11].split(',') if row[11] else []

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
            <td>{row[2]}</td>
           <td>{row[3]}</td>
            <td>{row[4]}</td>
            <td>{row[5]}</td>
            <td>{row[6]}</td>
            <td>
                 <button class="btn btn-success btn-sm" data-bs-toggle="modal" data-bs-target="#ratingsModal{serial_no}">
        Edit Ratings
    </button>

                <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modal{row[0]}">
                    Recipe Details
                </button>
               <div class="modal fade" id="ratingsModal{serial_no}" tabindex="-1" aria-labelledby="ratingsModalLabel{row[0]}" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="ratingsModalLabel{row[0]}">Edit Ratings</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <form id="ratingsForm{row[0]}" method="post">
                    <div class="modal-body">
                        <input type="hidden" name="rowid" value="{row[0]}">
                        <div class="mb-3">
                            <label for="rating{row[0]}" class="form-label">Rating</label>
                            <input type="number" class="form-control" id="rating{row[0]}" name="rating" 
                                   value="{row[5]}" min="1" max="5" step="0.1" required>
                        </div>
                        <div class="mb-3">
                            <label for="comment{row[0]}" class="form-label">Comment</label>
                            <textarea class="form-control" id="comment{row[0]}" name="comment" rows="3" required>{row[6]}</textarea>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="submit" class="btn btn-primary" name="sub">Save changes</button>
                    </div>
                </form>
                    
                        </div>
                    </div>
                </div>

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
                                            <p><strong>Name:</strong>  {row[4]}</p>
                                        </div>

                                            <div class="form-group">
                                            <p><strong>ID:</strong>  {row[7]}</p>
                                        </div>
                                        
                                        <div class="form-group">
                                            <p><strong>Recipe Name:</strong> {row[1]}</p>
                                        </div>
                                        <div class="form-group">
                                            <p><strong>Main Category:</strong> {row[2]}</p>
                                        </div>
                                        <div class="form-group">
                                            <p><strong>Sub Category:</strong> {row[3]}</p>
                                        </div>
                                        <div class="form-group">
                                            <p><strong>Keywords:</strong>{row[12]}</p>
                                        </div>
                                        <div class="form-group">
                                            <p><strong>Cooking Duration:</strong> {row[8]}</p>
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
submit = form.getvalue("sub")
if submit is not None:
    rowid = form.getvalue("rowid")
    rating = form.getvalue("rating")
    comment = form.getvalue("comment")
    q2 = """update recipe_ratings set rating='%s',comment='%s' where id='%s' """ % (rating,comment,rowid)
    cur.execute(q2)
    con.commit()