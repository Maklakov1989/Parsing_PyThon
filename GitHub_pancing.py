# print(('*' * 25), 'Задание №1 к лекции № 1', ('*' * 25))
import requests
def git_api():
  username = 'Maklakov1989'
  request = requests.get('https://api.github.com/users/'+username+'/repos')
  json = request.json()
  for i in range(0,len(json)):
    print("Project Number:",i+1)
    print("Project Name:",json[i]['name'])
    print("Project URL:",json[i]['svn_url'],"\n")
git_api()
print(('*' * 25), 'Задание №2 к лекции № 1', ('*' * 25))
def vk():
  user_id = '1276429'
  request = requests.get('https://api.vk.com/method/users.get?groups.get='+user_id+'&v=5.52')
  print(request)
vk()
