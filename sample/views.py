import json

from django.http import HttpResponse

# Create your views here.
# from sample.bk import Profile
from sample.models.profiles import Profile


def index(response):
    return HttpResponse('<h3>Index page!</h3>')


def view_1(response):
    return HttpResponse('<h3>View-1 page!</h3>')


def add_profile(request):
    user_id = request.POST.get('user_id')
    has_kyc = request.POST.get('has_kyc')


# def get_profile(request, user_id):
def get_profile(request, user_id):
    p: Profile = Profile.objects.get(user_id=user_id)
    if p is not None:
        print('profile[user_id={}, has_kyc={}]'.format(p.user_id, p.has_kyc))
    # p: Profile = Profile.objects.all()
    # print(p[0].user_id, p[0].has_kyc)

    # response = json.dumps({'user_id': p.user_id, 'has_kyc': p.has_kyc, 'military_service_status': 'FINISHED'})
    response = json.dumps({'user_id': user_id, 'has_kyc': True, 'military_service_status': 'FINISHED'})
    return HttpResponse(response, content_type='text/json')
