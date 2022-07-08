import time

# while True:
# 	print("I am working!")
# 	time.sleep(2)
import requests
import schedule
def index():
    # response=requests.get('https://brl1test.herokuapp.com/').json()
    # print(response)
    # return HttpResponse("hello")
    schedule.every(30).minutes.do(index2)    
    schedule.run_pending()
    while True:
        schedule.run_pending()
        time.sleep(1)
def index2():
    response=requests.get('https://brl1test.herokuapp.com/').json()
print(index())