from rest_framework.decorators import api_view
from app.models.mediators import Mediators
from util.http_util import HttpUtil

@api_view(['GET'])
def index(request, mediator_id):
    try:   
        mediator = Mediators.objects.get(mediator_id = mediator_id)
        dict = {
            'mediator_id' : mediator.mediator_id,
            'name' : mediator.name,
            'mobile' : mediator.mobile,
            'email' : mediator.email,
            'mobile_verified' : mediator.mobile_verified,
            'email_verified' : mediator.email_verified
        }
        return HttpUtil.respond(200 , None, dict)

    except Exception as e0: 
        return HttpUtil.respond(400, str(e0))