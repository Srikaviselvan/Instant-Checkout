#!C:/Users/Admin/AppData/Local/Programs/Python/Python311/python.exe
import os.path

print("content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql

cgitb.enable()

conn = pymysql.connect(host = "Localhost", user = "root", password = "", database = "hackathon_db")
cursor = conn.cursor()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Virtual Cart</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link rel="icon" href="./Image/retail background.jpg">
    <link rel="stylesheet" href="./style.css">
    <style>
        footer{
            position: relative;
            top: 300px;
        }
        
        header{
        background-image: url("./Image/retail background.jpg");
        }
        
        body{
        background-image: url("./Image/retail background.jpg");
        background-repeat: no-repeat;
        background-size: cover;
        }
        
        footer{
        position: relative;
        top: 570px;
        }
        
        table{
            margin-top: 50px;
        }
        
        table, tr, th{
            border: 5px solid yellow;
            background-color: black;
        }
        
        th, td{
            font-size: 30px;
            padding: 30px 50px;
            color: aqua;
        }
        
        caption{
        background-color: black;
        color: yellow;
        text-align: center;
        border: 6px solid yellow;
        }
        
    </style>
</head>
<body>
    
    <nav class = "nav navbar-default">
        <div class = "container-fluid">
            

            <div class = "col-md-1" style="float: right;">
                <ul class = "nav navbar-nav">

                    <li><a style = "background-color: black;" style = "cursor: pointer" href = "#" id = "categories">Profile</a></li>
                    
                </ul>
            </div>

            <div class = "col-md-2" style="float: left;">
                <ul class = "nav navbar-nav">
                    <li><a style = "background-color: black;" href="./home.py" class = "navbar-brand" id = "home_page_link">Home Page</a></li>
                </ul>
            </div>

            

        </div>

    </nav>


""")

print("""
    <center>
        <table>
        <caption>STOCK</caption>
""")

query = """select * from stock"""
cursor.execute(query)
stock = cursor.fetchall()


for object in stock:
    print("""
    <tr>
        <th>%s</th>
        <td>%s</td>
    </tr>
    """ % (object[1], object[2]))

print("""        
        </table>
    </center>
""")


print("""
<center>
<table>
<caption>CART</caption>
""")

query = """select * from cart"""
cursor.execute(query)
cart = cursor.fetchall()

for object in cart:
    print("""
    <tr>
        <th>%s</th>
        <td>%s</td>
    </tr>
    """ % (object[1], object[2]))

print("""        
        </table>
    </center>
""")




print("""
    
    <footer class = "text-center row" style="width: 1380px;">
        <div>

            <div class = "col-md-4" style = "background-color: black; opacity: 1;">
                <ul>
                    <li><a style = "cursor: pointer;" href = "#">About Us</a></li>
                </ul>
            </div>

            <div class = "col-md-4" style = "background-color: black; opacity: 1;">
                <ul>
                    <li><a style = "cursor: pointer;" href="#">Contact Us</a></li>
                </ul>
            </div>
            
            <div class = "col-md-4" style = "background-color: black; opacity: 1;">
                <ul>
                    <li><a style = "cursor: pointer;" href="#">FAQs</a></li>
                </ul>
            </div>
        </div>
    </footer>

</body>
</html>
""")



conn.close()