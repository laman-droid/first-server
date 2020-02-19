import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()

print("Content-Type: text/html")
print()   
print("<TITLE>CGI script output</TITLE>")
print("<h1>Hello", form["submitted-name"].value, "!</h1>")