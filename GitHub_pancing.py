import requests
username = 'Maklakov1989'
request = requests.get('https://api.github.com/users/'+username+'/repos')
json = request.json()
for i in range(0,len(json)):
  print("Project Number:",i+1)
  print("Project Name:",json[i]['name'])
  print("Project URL:",json[i]['svn_url'],"\n")