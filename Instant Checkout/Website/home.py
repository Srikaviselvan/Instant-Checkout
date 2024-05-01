#!C:/Users/Admin/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql

cgitb.enable()

conn = pymysql.connect(host="Localhost", user="root", password="", database="gamers_den")
cursor = conn.cursor()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Virtual Cart</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link rel="icon" href="./Image/retail background.jpg">

<style>

@keyframes left-to-right{
    from {
        left: -100%;
    }

    to {
        left: 37%;
    }
}

@keyframes right-to-left{
    from {
        left: 1500px;
    }

    to {
        left: 25%;
    }
}

@keyframes left-to-right-2{
    from {
        left: -100%;
    }

    to {
        left: 23%;
    }
}

.topic{
    font-size: 100px;
    color: yellow;
    position: absolute;
}

#one{
    margin-left: 2%;
    color: yellow;
    animation: left-to-right 1s ease forwards;
    text-shadow: 2px 7px 5px red;
}

#two{
    top: 220px;
    color: yellow;
    animation: right-to-left 1s ease forwards;
    text-shadow: 2px 7px 5px red;
    margin-top: -1px;
    margin-left: 180px;
}

#three{
    top: 350px;
    color: yellow;
    animation: left-to-right-2 1s ease forwards;
    text-shadow: 2px 7px 5px red;
    margin-top: -1px;
    margin-left: 240px;
}



footer{
    position: relative;
    top: 10px;
}

label{
    margin-left: 20px;
    color: yellow;
    font-size: 20px;
}

/* Full-width input fields */
input[type=text], input[type=password], input[type=email] {
  width: 80%;
  padding: 12px 20px;
  margin: 20px 0;
  margin-left: 60px;
  display: inline-block;
  border: 3px solid yellow;
  box-sizing: border-box;
  color: yellow;
  font-size: 20px;
  background-color: black;
}


/* Set a style for all buttons */
button {
  background-color: yellow;
  color: yellow;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 20%;
}

#btn_submit{
    width: max-content;
    font-size: 20px;
    background-color: black;
    border: 3px solid yellow;
}

button:hover {
  opacity: 0.8;
}

/* Center the image and position the close button */
.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
  position: relative;
}

img.avatar {
  width: 10%;
  border-radius: 50%;
}

.container {
  padding: 16px;
}

span.psw {
  float: right;
  padding-top: 16px;
}

/* The Modal (background) */
.modal{
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 110%; /* Cover all content */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
  padding-top: 60px;
}

/* Modal Content/Box */
.modal-content {
  background-image: url("./Image/retail background.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  margin: 5% auto 15% auto; /* 5% from the top, 15% from the bottom and centered */
  border: 1px solid #888;
  width: 80%; /* Could be more or less, depending on screen size */
}

/* The Close Button (x) */
.close {
  position: absolute;
  right: 25px;
  top: 0;
  color: yellow;
  font-size: 35px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: yellow;
  cursor: pointer;
}

/* Add Zoom Animation */
.animate {
  -webkit-animation: animatezoom 0.6s;
  animation: animatezoom 0.6s
}



@-webkit-keyframes animatezoom {
  from {-webkit-transform: scale(0)} 
  to {-webkit-transform: scale(1)}
}

@keyframes animatezoom {
  from {transform: scale(0)} 
  to {transform: scale(1)}
}

#home_page_link{
    color: yellow;
}

#categories{
    color: yellow;
    font-size: medium;
}

#home_page_link:hover, #categories:hover{
    background-color: yellow;
}


.dropdown .dropdown-menu a{
    color: yellow;
}

.dropdown .dropdown-menu a:hover {
    background-color: yellow;
    color: black;
}

.navbar-default{
    background-image: url("./Image/retail background.jpg");
}

.dropdown-categories{
    background-color: black;
}

#category_dropdown{
    background-color: black;
}

footer{
    position: relative;
    top: 580px;
    left: 12px;
}

body{
    background-color: yellow;
    background-image: url("./Image/retail background.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    overflow: hidden;
}

h1{
    color: white;
}

li{
    padding: 10px;
}

footer div ul{
    list-style-type: none;
}



footer div ul li a{
    padding: 2px;
    padding-right: 10px;
    padding-left: 10px;
    color: yellow;
}

footer div ul li a:hover{
    text-decoration: none;
    background-color: yellow;
    color: black;
}

.container{
    margin-top: 50px;
}

#whitespace-needed-n1{
  padding-right: 42px;
}

#whitespace-needed-n2{
  padding-right: 33px;
}

</style>

</head>
<body>

    <nav class = "nav navbar-default">
        <div class = "container-fluid">

            <div class = "navbar-header col-md-5" style="padding-top: 10px;">
                
            </div>

            <div style="float: right;">
                <ul class = "nav navbar-nav">

                    <li class = "dropdown"><a style = "background-color: black;" href="#" class = "dropdown-toggle" data-toggle = "dropdown" id = "categories">Sign in <span class = "caret"></span></a>
                        <ul class = "dropdown-menu" id = "category_dropdown">
                            <li class = "dropdown-categories"><a style="cursor: pointer;" onclick="document.getElementById('id01').style.display='block'">Login</a></li>
                            <li class = "dropdown-categories"><a style="cursor: pointer;" onclick="document.getElementById('id02').style.display='block'">Register</a></li>
                        </ul>
                    </li>

                </ul>
            </div>  

            <div>
              <ul class = "nav navbar-nav ">
                <li><a class = "navbar-brand website_name" style="cursor: default; color: yellow; font-size: 23px; font-weight: 700; text-shadow: 2px 4px 5px red;"></a></li>
              </ul>
            </div>

        </div>

    </nav>


    <div id = "topic-background"><h1 class = "topic" id = "one">JUST</h1></div>
    <div id = "topic-background"><h1 class = "topic" id = "two">WALK</h1></div>
    <div id = "topic-background"><h1 class = "topic" id = "three">OUT</h1></div>


    <footer class = "text-center row" style="width: 1380px;">
        <div>

            <div class = "col-md-4" style = "background-color: black;">
                <ul>
                    <li><a style = "cursor: pointer;" href = "#">About Us</a></li>
                </ul>
            </div>

            <div class = "col-md-4" style = "background-color: black;">
                <ul>
                    <li><a style = "cursor: pointer;" href="#">Contact Us</a></li>
                </ul>
            </div>
            
            <div class = "col-md-4" style = "background-color: black;">
                <ul>
                    <li><a style = "cursor: pointer;" href="#">FAQs</a></li>
                </ul>
            </div>
            

            

        </div>
    </footer>


    <div id="id01" class="modal">

        <form class="modal-content animate" method = "post">

          <div class="container-fluid">
            <label for="uname"><b>Username</b></label>
            <input type="text" placeholder="Enter Username" name="uname" id = "uname" required>
              <br>
            <label for="psw"><b>Password</b></label>
            <input type="password" placeholder="Enter Password" name="psw" id = "psw" required>
            <input type="hidden" name="login-button" value="LoginButton">
            <center><button value="LoginButton" name = "login-button" type="submit" id = "btn_submit">Login</button></center>
          </div>
        </form>
    </div>

    <div id="id02" class="modal" style="margin-top: -100px;">

        <form class="modal-content animate" method = "post">
            <div class="imgcontainer">
              <span style = "color: black; opacity: 1;" onclick="document.getElementById('id02').style.display='none'" class="close" title="Close Modal">x</span>
            </div>

            <div class="container-fluid">
                  <label for="email2" id = "whitespace-needed-n1"><b>Email</b></label>
                  <input type="email" placeholder="Enter Email" name="email2" id = "email2" required>
                <label for="uname2"><b>Username</b></label>
                <input type="text" placeholder="Enter Username" name="uname2" id = "uname2" required>
                <label for="psw2"><b>Password</b></label>
                <input type="password" placeholder="Enter Password" name="psw2" id = "psw2" required>
                <label for="num2" id = "whitespace-needed-n2"><b>Phone</b></label>
                <input type="text" placeholder="Enter Phone Number" name="num2" id = "num2" required>
                <input type="hidden" name="register-button" value="RegisterButton">
                <center><button name = "register-button" type="submit" value="RegisterButton" id = "btn_submit" onclick="registration_alert()">Register</button></center>
            </div>
        </form>
    </div>
    
    <script>
    function go_to_about(){
    const queryString = window.location.search;
    const url = new URLSearchParams(queryString);
    id = url.get('Id');
    location.href = "about_page.py?Id=" + id;
    }
    </script>

</body>
</html>
""")

form = cgi.FieldStorage()

register_button = form.getvalue('register-button')

if register_button:
    email = form.getvalue('email2')

    query = """select * from users where email = '%s'""" % email
    cursor.execute(query)

    record = cursor.fetchone()

    if not record:

        username = form.getvalue('uname2')
        email = form.getvalue('email2')
        password = form.getvalue('psw2')
        phonenumber = form.getvalue('num2')

        query = """insert into users (username, email, password, phonenumber) values ('%s', '%s', '%s', '%s')""" % (
        username, email, password, phonenumber)
        cursor.execute(query)
        conn.commit()

        print("""
        <script>
        alert("Registration Successful")
        </script>
        """)

    else:
        print("""
        <script>
        alert("This email is already in use");
        </script>
        """)

login_button = form.getvalue('login-button')

if login_button:
    username = form.getvalue('uname')
    password = form.getvalue('psw')

    query = """select * from users where username = '%s' and password = '%s'""" % (username, password)
    cursor.execute(query)

    record = cursor.fetchone()

    if record:
        id = record[0]
        print("""
        <script>
        alert("Login successful");
        location.href = "main.py?Id=%s";
        </script>
        """ % id)
    else:
        print("""
        <script>
        alert("Wrong Username / Password");
        </script>
        """)

conn.close()