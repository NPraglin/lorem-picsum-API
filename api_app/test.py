import cgi

form = cgi.FieldStorage()
searchterm =  form.getvalue('heightinput')
print(searchterm)