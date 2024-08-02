from rest_framework.decorators import api_view
from app.models.mediators import Mediators
from util.http_util import HttpUtil

@api_view(['POST'])
def index(request, mediator_id = None):
    data = request.data
    
    try:   
        mediators = Mediators.objects.filter(mediator_id = mediator_id)
        if(mediator_id != None and mediator_id != ""  and (not mediators.exists())):
            raise Exception('Invalid mediator id')
        elif(mediators.exists()):
            mediator = mediators.first()
        else:
            mediator = Mediators()
            mediator.mediator_id = Mediators.objects.generate_id()

        #Mediator Name
        name = data.get('name')
        if(name != '' and name != None):
            mediator.name = name
        elif(mediator.name == None or mediator.name == ""):
            raise Exception('Mediator name cannot be empty')
        
        #Mobile Number
        mobile = data.get('mobile')
        if(mobile != '' and mobile != None):
            mediator.mobile = mobile
            mediator.mobile_verified = False
        elif(mediator.mobile == None or mediator.mobile == ""):
            raise Exception('Mobile number cannot be empty')
        
        #Email ID
        email = data.get('email')
        if(email != '' and email != None):
            mediator.email = email
            mediator.email_verified = False
        elif(mediator.email == None or mediator.email == ""):
            raise Exception('Email cannot be empty')
        
        mediator.save()

        dict = {
            'mediator_id' : mediator.mediator_id,
            'name' : mediator.name,
            'mobile' : mediator.mobile,
            'email' : mediator.email,
            'mobile_verified' : mediator.mobile_verified,
            'email_verified' : mediator.email_verified
        }
        return HttpUtil.respond(200 if mediators.exists() else 201 , None, dict)

    except Exception as e0: 
        return HttpUtil.respond(400, str(e0))