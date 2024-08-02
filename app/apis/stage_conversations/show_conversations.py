from app.models.conversation_staging import ConversationStaging
from rest_framework.decorators import api_view
from util.http_util import HttpUtil
import json

@api_view(['POST'])
def index(request, conversation_id):
    data = request.data
    try:
        system_fingerprint = data.get("fingerprint")
        converstion_stage = ConversationStaging.objects.get(conversation_id = conversation_id, system_fingerprint = system_fingerprint)     
        return HttpUtil.respond(200, None, json.loads(converstion_stage.conversation))
    except Exception as e0: 
        return HttpUtil.respond(400, str(e0))