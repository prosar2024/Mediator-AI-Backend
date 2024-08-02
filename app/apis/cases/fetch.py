from rest_framework.decorators import api_view
from util.http_util import HttpUtil

@api_view(['GET'])
def index(request, case_id):
    try:   
        party = Parties.objects.get(party_id = party_id)
        dict = {
            'party_id' : party.party_id,
            'name' : party.name,
            'mobile' : party.mobile,
            'email' : party.email,
            'mobile_verified' : party.mobile_verified,
            'email_verified' : party.email_verified
        }
        return HttpUtil.respond(200 , None, dict)

    except Exception as e0: 
        return HttpUtil.respond(400, str(e0))