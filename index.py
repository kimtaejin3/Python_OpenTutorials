#!C:\Program Files\Python38\python.exe
print("Content-Type: text/html")
print()
import cgi, os

files=os.listdir('data')
listStr=''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
form=cgi.FieldStorage()

if 'id' in form:
    pageId=form["id"].value
    f=open('data/'+ pageId,'r')
    description=f.read()
    update_link='<a href="update.py?id={}">update</a>'.format(pageId)
else:
    pageId='Welcome'
    description='Hello Web'
    update_link=''


print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
   <a href="create.py">create</a>
   {update_link}
   <h2>{title}</h2>
   <p>{des}</p>
</body>
</html>
'''.format(title=pageId,des=description,listStr=listStr,update_link=update_link))
