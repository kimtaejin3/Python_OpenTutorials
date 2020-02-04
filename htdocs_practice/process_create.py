#!C:\Program Files\Python38\python.exe


import cgi
form=cgi.FieldStorage()
title=form["title"].value
description=form['description'].value

opened_file=open('data/'+title,'w')
opened_file.write(description)
#Redirection
print("Location: index.py?id="+title)
print()
