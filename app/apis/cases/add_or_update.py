from rest_framework.decorators import api_view
from util.http_util import HttpUtil
from app.models.cases import Cases
from app.models.mediators import Mediators
from datetime import datetime

@api_view(['POST'])
def index(request, case_id = None):
    data = request.data
    
    try:   
        cases = Cases.objects.filter(case_id = case_id)
        if(case_id != None and case_id != ""  and (not cases.exists())):
            raise Exception('Invalid case id')
        elif(cases.exists()):
            case = cases.first()
        else:
            case = Cases()
            case.case_id = Cases.objects.generate_id()

        #Case Summary
        summary = data.get('summary')
        if(summary != '' and summary != None):
            case.summary = summary
        elif(case.summary == None or case.summary == ""):
            raise Exception('Case summary cannot be empty')
        
        #Case Mediator
        mediator_id = data.get('mediator_id')
        if(mediator_id != '' and mediator_id != None):
            case.mediator = Mediators.objects.get(mediator_id = mediator_id)
        elif(case.mediator == None):
            raise Exception('Mediator id cannot be empty')
        
        #Case Closed Date
        closed_on = data.get('closed_on')
        if(closed_on != '' and closed_on != None):
            case.closed_on = datetime.strptime(closed_on, "%Y-%m-%d").date()
        
        case.save()

        dict = {
            'case_id' : case.case_id,
            'summary' : case.summary,
            'mediator' : {
                'mediator_id' : case.mediator.mediator_id,
                'name' : case.mediator.name,
                'mobile' : case.mediator.mobile,
                'email' : case.mediator.email
        },
            'closed_on' : case.closed_on
        }
        return HttpUtil.respond(200 if cases.exists() else 201 , None, dict)

    except Exception as e0: 
        return HttpUtil.respond(400, str(e0))