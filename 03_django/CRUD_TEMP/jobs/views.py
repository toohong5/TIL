import requests
from pprint import pprint
from django.shortcuts import render
from decouple import config
from .models import Job
from faker import Faker
# Create your views here.

def index(request):
    return render(request, 'jobs/index.html')

def past_life(request):
    # 사용자로부터 이름 데이터를 받음.
    name = request.POST.get('name') # request에 이름 들어있음..
    # db에 매칭되는 name 가져오기
    person = Job.objects.filter(name=name).first()# filter는 한개던 0개던 상관없이 무조건 쿼리셋으로 가져옴..(리스트형식)
    # 리스트의 첫번째 값을 가져옴(비었으면 null가져음)
    # .get이 더 간단하지만 해당 값이 없을 경우 에러가 발생하기 때문. -> pk값에서 주로 사용!!
    
    # db에 person이 있는지 없는지 판단
    if person: # db에 기존 이름이 있을 경우
        # 해당 person이 가지고 있는 job가져옴
        past_job = person.past_job
    else:
        # db 에 기존 이름이 없다면(person이 빈 쿼리셋(False)일 경우)새로운 직업
        faker = Faker()
        past_job = faker.job()
        person = Job(name=name, past_job=past_job) # 새로운 레코드를 추가한다.
        person.save() # 저장

    # GIPHY (past_job 을 api에 요청을 보내서 응답을 받음)
    GIPHY_API_KEY = config('GIPHY_API_KEY')
    url = f'https://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={past_job}&limit=1'
    data = requests.get(url).json()
    try:
        image = data.get('data')[0].get('images').get('original').get('url') # 이미지 주소
    except IndexError:
        image = None
    context = {'person': person, 'image': image, }
    return render(request, 'jobs/past_life.html', context)

    # past_jobs = Job.objects.all()
    # names = Job.objects.POST.get('name')
    # if name in names:
    #     context = {'name': names, 'past_jobs': past_jobs}
