from rest_framework.decorators import api_view
from app.models.mediators import Mediators
from util.http_util import HttpUtil

@api_view(['GET'])
def index(request):
    try:   
        mediators = Mediators.objects.all()
        resp = []
        for mediator in mediators:
            resp.append({
                'mediator_id' : mediator.mediator_id,
                'name' : mediator.name,
                'mobile' : mediator.mobile,
                'email' : mediator.email,
                'mobile_verified' : mediator.mobile_verified,
                'email_verified' : mediator.email_verified
        })

        return HttpUtil.respond(200 , None, resp)

    except Exception as e0: 
        return HttpUtil.respond(400, str(e0))