from app.models.parties_involved import PartiesInvolved
from app.models.conversations import Conversations
from rest_framework.decorators import api_view
from app.ai.ai_handler import AIHandler
from util.http_util import HttpUtil
import uuid

@api_view(['POST'])
def index(request, case_id, party_id):
    data = request.data
    try:
        party = PartiesInvolved.objects.get(case__case_id = case_id, party_id = party_id)
        msg = data.get("user_message")
        if(msg == None or msg == ""):
            raise Exception("Input message cannot be empty")

        conv = Conversations.objects.filter(party = party)
        if(conv.exists()):
            conv = conv.first()
        else:
            conv = Conversations()
            conv.conversation_id = uuid.uuid4()
            conv.party = party
                
        ai_data = AIHandler.talk(conv.conversation_id, msg, conv.conversation)
        conv.conversation = ai_data['full_json']
        resp = ai_data['bot_response']

        conv.save()

        dict = {
            'conversation_id' : conv.conversation_id,
            'bot_message' : resp
        }
        return HttpUtil.respond(200, None, dict)
        
    except Exception as e0: 
        return HttpUtil.respond(400, str(e0))