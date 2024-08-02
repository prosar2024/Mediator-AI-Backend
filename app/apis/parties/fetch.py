from rest_framework.decorators import api_view
from app.models.parties_involved import PartiesInvolved
from util.http_util import HttpUtil

@api_view(['GET'])
def index(request, case_id, party_id=None):
    try:   
        parties = PartiesInvolved.objects.filter(case__case_id = case_id)
        if(party_id != None and party_id != ""):
            parties = parties.filter(party_id = party_id)

        resp = []
        for party in parties:
            resp.append({
                'party_id' : party.party_id,
                'case_id' : party.case.case_id,
                'name' : party.name,
                'role' : party.role,
                'mobile' : party.mobile,
                'email' : party.email,
                'mobile_verified' : party.mobile_verified,
                'email_verified' : party.email_verified
            })
        return HttpUtil.respond(200 , None, resp)

    except Exception as e0: 
        return HttpUtil.respond(400, str(e0))