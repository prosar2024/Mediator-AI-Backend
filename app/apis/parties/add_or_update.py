from rest_framework.decorators import api_view
from app.models.parties_involved import PartiesInvolved
from util.http_util import HttpUtil
from app.models.cases import Cases

@api_view(['POST'])
def index(request, case_id, party_id = None):
    data = request.data
    
    try:
        case = Cases.objects.get(case_id = case_id)

        parties = PartiesInvolved.objects.filter(party_id = party_id, case = case)
        if(party_id != None and party_id != ""  and (not parties.exists())):
            raise Exception('Invalid party id or party doesnt belong to case '+case_id)
        elif(parties.exists()):
            party = parties.first()
        else:
            party = PartiesInvolved()
            party.party_id = PartiesInvolved.objects.generate_id(case)
            party.case = case

        #Party's Role
        role = data.get('role')
        if(role != '' and role != None):
            party.role = role
        elif(party.role == None or party.role == ""):
            raise Exception('Party\'s role cannot be empty')
      
        #Party Name
        name = data.get('name')
        if(name != '' and name != None):
            party.name = name
        elif(party.name == None or party.name == ""):
            raise Exception('Party name cannot be empty')
        
        #Mobile Number
        mobile = data.get('mobile')
        if(mobile != '' and mobile != None):
            party.mobile = mobile
            party.mobile_verified = False
        elif(party.mobile == None or party.mobile == ""):
            raise Exception('Mobile number cannot be empty')
        
        #Email ID
        email = data.get('email')
        if(email != '' and email != None):
            party.email = email
            party.email_verified = False
        elif(party.email == None or party.email == ""):
            raise Exception('Email cannot be empty')
        
        party.save()

        dict = {
            'party_id' : party.party_id,
            'case_id' : party.case.case_id,
            'name' : party.name,
            'role' : party.role,
            'mobile' : party.mobile,
            'email' : party.email,
            'mobile_verified' : party.mobile_verified,
            'email_verified' : party.email_verified
        }
        return HttpUtil.respond(200 if parties.exists() else 201 , None, dict)

    except Exception as e0: 
        return HttpUtil.respond(400, str(e0))