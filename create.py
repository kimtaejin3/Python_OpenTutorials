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
else:
    pageId='Welcome'
    description='Hello Web'


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
 <form action="process_create.py" method="post">
      <p><input type="text" name="title" placeholder="title"></p>
      <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
      <p><input type="submit"></p>
  </form>
</body>
</html>
'''.format(title=pageId,des=description,listStr=listStr))
