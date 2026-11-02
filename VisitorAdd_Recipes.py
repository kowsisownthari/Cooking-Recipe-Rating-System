#!C:/Users/Home/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgitb
import cgi
import pymysql,os

cgitb.enable()
form = cgi.FieldStorage()
con = pymysql.connect(host="localhost", user="root", password="", database="rating_system")
cur = con.cursor()
userid = form.getvalue("id")
Name = ""
Email = ""
designation =""
id=""
if userid is not None:
    q = "SELECT * FROM visitor_register WHERE id=%s"
    cur.execute(q, (userid,))
    res = cur.fetchall()
    for i in res:
        Name = i[1]
        Email = i[2]
        designation=i[17]
        id=i[0]
cur.execute("SELECT keyword FROM keywords")
keywords = [row[0] for row in cur.fetchall()]
print("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Visitor Add Recipe</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<style>
body {
    margin: 0;
    padding: 0;
    font-family: 'Roboto condensed', sans-serif;
}

section {
    width: 100%;
    height: 130vh;
    background: #E6E6FA;
    padding: 40px 40px; 
    margin-right:200vh;
}

.login-container {
    width: 100%;
    max-width: 480px;
    text-align: center;
    margin-left: 400px;
    color:black;
}

.login-form {
    position: relative;
    box-sizing: border-box;
    padding: 40px 30px;
    transform: .5s;
    background-color: rgba(255, 255, 255, .1);
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0, 0, 0, .2);
    width: 100%;
        color:black;

}

.login-form h1 {
    margin: 0 0 20px;
    color: #fff;
    font-size: 30px;
    text-transform: uppercase;
        color:black;

}

.login-form input, .login-form select {
    display: block;
    width: 100%;
    padding: 10px 20px;
    box-sizing: border-box;
    margin-bottom: 20px;
    border-radius: 25px;
    outline: none;
    font-size: 14px;
    letter-spacing: 1px;
    color: #fff;
    border: none;
    background: rgba(255, 255, 255, .1);
    font-family: 'Roboto condensed', sans-serif;
        color:black;

}

.login-form select {
    cursor: pointer;
}

.login-form select option {
    background: #333;
    color: #fff;
}

#subCategoryContainer {
    display: none;
    margin-top: 10px;
}

.step-container {
    position: relative;
    margin-bottom: 10px;
}

.remove-step {
    position: absolute;
    right: -30px;
    top: 50%;
    transform: translateY(-50%);
    color: red;
    border: none;
    border-radius: 50%;
    background:#E6E6FA;
    width: 25px;
    height: 25px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
}

.add-step {
    background: #28a745;
    color: white;
    border: none;
    border-radius: 25px;
    padding: 10px 20px;
    margin: 10px 0;
    cursor: pointer;
    width: 100%;
}

.submit-btn {
    background: #0072ff;
    color: white;
    border: none;
    border-radius: 25px;
    padding: 10px 20px;
    margin: 10px 0;
    cursor: pointer;
    width: 100%;
}

.cancel-btn {
    background: red;
    color: white;
    border: none;
    border-radius: 25px;
    padding: 10px 20px;
    margin: 10px 0;
    cursor: pointer;
    width: 100%;
}

.ingredient-quantity-container {
    display: flex;
    gap: 10px;
    margin-bottom: 10px;
    position: relative;
    padding-right: 35px;
}

.ingredient-quantity-container input {
    margin-bottom: 0;
}

.remove-ingredient {
    position: absolute;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
    color: red;
    border: none;
    border-radius: 50%;
    width: 25px;
        background:#E6E6FA;
    height: 25px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
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
<section>
    <div class="login-container">
        <div class="login-form">
            <h3>ADD RECIPE</h3>
            <form method="post" enctype="multipart/form-data" id="recipeForm">
                <input type="text" name="name" placeholder="Recipe Name">
                <div id="stepsContainer">
                    <div class="step-container">
                        <input type="text" name="steps[]" placeholder="Cooking step 1">
                    </div>
                </div>
                <button type="button" class="add-step" onclick="addStep()">Add Step</button>
                <input type="text" name="duration" placeholder="Cooking Duration">

                <div class="ingredient-selects">
                    <select name="mainCategory" id="mainCategory" onchange="updateSubcategory()">
                        <option value="">Select Main Ingredient Category</option>
                        <option value="meat">Meat</option>
                        <option value="vegetables">Vegetables</option>
                        <option value="fruits">Fruits</option>
                        <option value="grains">Grains</option>
                        <option value="dairy">Dairy</option>
                        <option value="seafood">Seafood</option>
                    </select>

                    <div id="subCategoryContainer">
                        <select name="subCategory" id="subCategory">
                            <option value="">Select Sub Category</option>
                        </select>
                    </div>
                </div>

                <div id="ingredientQuantityContainer">
                    <div class="ingredient-quantity-container">
                        <input type="text" name="ingredients[]" placeholder="Ingredient">
                        <input type="text" name="quantities[]" placeholder="Quantity">
                        <button type="button" class="remove-ingredient" onclick="removeIngredient(this)">X</button>
                    </div>
                </div>
                <button type="button" class="add-step" onclick="addIngredient()">Add Ingredient</button>
<select name="common_recipes" id="common_recipes">
  <option value="" disabled selected>Select Keyword</option>
""")


for keyword in keywords:
    print(f'  <option value="{keyword}">{keyword}</option>')

print("""
   <label for="video" style="color:black; margin-left:-250px;">Choose a video file:</label>
        <input type="file" id="video" name="video" accept="video/*">
               <input type="submit" name="sub" value="Add" style="text-align:center;color:white;background:blue;">
                     <input type="button" name="can" value="cancel" style="text-align:center;color:white;background:red;">
            </form>
        </div>
    </div>
</section>

<script>
let stepCount = 1;

const subcategories = {
    meat: ['Chicken', 'Beef', 'Pork', 'Lamb', 'Turkey', 'Goat', 'Duck', 'Veal', 'Quail'],
    vegetables: ['Onions', 'Tomatoes', 'Carrots', 'Potatoes', 'Cabbage', 'Cauliflower', 'Mushrooms', 'Green Beans', 'Peas', 'Pumpkin', 'Cucumbers', 'Radishes', 'Leeks', 'Beetroot'],
    fruits: ['Oranges', 'Lemon', 'Grapefruit', 'Peaches', 'Plums', 'Strawberries', 'Apricots', 'Blueberries', 'Pineapples', 'Mangoes', 'Bananas', 'Papayas'],
    grains: ['Rice', 'Wheat', 'Oats', 'Maize', 'Millet', 'Rye', 'Buckwheat', 'Spelt', 'Kamut'],
    dairy: ['Milk', 'Cheese', 'Yogurt', 'Cream', 'Butter'],
    seafood: ['Fish', 'Shellfish', 'Prawn', 'Crab', 'Lobster', 'Mussels', 'Clams', 'Halibut', 'Scallops']
};

function updateSubcategory() {
    const mainCategory = document.getElementById('mainCategory').value;
    const subCategoryContainer = document.getElementById('subCategoryContainer');
    const subCategorySelect = document.getElementById('subCategory');

    subCategorySelect.innerHTML = '<option value="">Select Sub Category</option>';

    if (mainCategory) {
        const options = subcategories[mainCategory];
        options.forEach(option => {
            const optionElement = document.createElement('option');
            optionElement.value = option.toLowerCase();
            optionElement.textContent = option;
            subCategorySelect.appendChild(optionElement);
        });
        subCategoryContainer.style.display = 'block';
    } else {
        subCategoryContainer.style.display = 'none';
    }
}

function addStep() {
    stepCount++;
    const container = document.createElement('div');
    container.className = 'step-container';

    container.innerHTML = `
        <input type="text" name="steps[]" placeholder="Cooking step ${stepCount}">
        <button type="button" class="remove-step" onclick="removeStep(this)">X</button>
    `;

    document.getElementById('stepsContainer').appendChild(container);
}
function removeStep(button) {
    button.parentElement.remove();
    reorganizeSteps();
}

function reorganizeSteps() {
    stepCount = 0;
    const steps = document.querySelectorAll('.step-container input');
    steps.forEach(step => {
        stepCount++;
        step.placeholder = `Cooking step ${stepCount}`;
    });
}

function addIngredient() {
    const container = document.createElement('div');
    container.className = 'ingredient-quantity-container';

    container.innerHTML = `
        <input type="text" name="ingredients[]" placeholder="Ingredient">
        <input type="text" name="quantities[]" placeholder="Quantity">
        <button type="button" class="remove-ingredient" onclick="removeIngredient(this)">X</button>
    `;

    document.getElementById('ingredientQuantityContainer').appendChild(container);
}

function removeIngredient(button) {
    button.parentElement.remove();
}
</script>
</body>
</html>""")
submit = form.getvalue("sub")
if submit is not None:
    if 'video' in form:
        Img = form['video']
        if Img.filename:
            pi = os.path.basename(Img.filename)
            open("Visitor_Recipe/" + pi, "wb").write(Img.file.read())
            Recipe_Name = form.getvalue("name")
            Steps = ','.join(form.getlist("steps[]")) if form.getlist("steps[]") else ''
            duration = form.getvalue("duration")
            mainCategory = form.getvalue("mainCategory")
            subCategory = form.getvalue("subCategory")
            ingredients = ','.join(form.getlist("ingredients[]")) if form.getlist("ingredients[]") else ''
            quantities = ','.join(form.getlist("quantities[]")) if form.getlist("quantities[]") else ''
            keyword = form.getvalue("common_recipes")
            q = """INSERT INTO food_recipes
                (Recipe_Name, Steps, duration, mainCategory, subCategory, ingredients, 
                quantities, keyword, status, video, Name, Email,designation,cookery_id) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 'pending', %s, %s, %s,%s,%s)"""
            values = (Recipe_Name, Steps, duration, mainCategory, subCategory,
                      ingredients, quantities, keyword, pi, Name, Email,designation,id)
            cur.execute(q, values)
            con.commit()