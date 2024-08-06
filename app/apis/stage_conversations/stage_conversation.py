from app.models.conversation_staging import ConversationStaging
from rest_framework.decorators import api_view
from app.ai.ai_handler import AIHandler
from util.http_util import HttpUtil
import uuid
import json

@api_view(['POST'])
def index(request, conversation_id = None):
    data = request.data
    system_fingerprint = data.get("fingerprint")
            
    try:
        if(conversation_id == None or conversation_id == "" or system_fingerprint == "" or system_fingerprint == None):
            converstion_stage = ConversationStaging()
            converstion_stage.conversation_id = uuid.uuid4()
            converstion_stage.system_fingerprint = uuid.uuid4()
        else:
            converstion_stage = ConversationStaging.objects.get(conversation_id = conversation_id, system_fingerprint = system_fingerprint)

        user_message = data.get("user_message", None)
        ai_message = AIHandler.stage_talk(converstion_stage.conversation_id, user_message, converstion_stage.conversation)
        
        if(user_message != None and user_message != ""):
            user_data = {
                "role": "user", 
                "content": user_message
            }

        ai_data = {
            "role": "ai", 
            "content": ai_message
        }

        if(converstion_stage.conversation == None or converstion_stage.conversation == ""):
            if(user_message != None and user_message != ""):
                json_history = [user_data, ai_data]
            else:
                json_history = [ai_data]
        else:
            json_history = json.loads(converstion_stage.conversation)
            if(user_message != None and user_message != ""):
                json_history.append(user_data)
            json_history.append(ai_data)
        converstion_stage.conversation = json.dumps(json_history)
        converstion_stage.save()

        dict = {
            'conversation_id' : converstion_stage.conversation_id,
            'fingerprint' : converstion_stage.system_fingerprint,
            'message' : ai_message,
            'request_fileupload' : True if user_message.__contains__("file") else False
        }
        return HttpUtil.respond(200, None, dict)
        
    except Exception as e0: 
        return HttpUtil.respond(400, str(e0))