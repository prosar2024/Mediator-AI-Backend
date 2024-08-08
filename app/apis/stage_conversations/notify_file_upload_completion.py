from app.models.conversation_staging import ConversationStaging
from app.models.files_staging import FilesStaging
from rest_framework.decorators import api_view
from util.http_util import HttpUtil

@api_view(['POST'])
def index(request, conversation_id=None):
    data = request.data
    fingerprint = data.get("fingerprint")

    try:
        converstion_stage = ConversationStaging.objects.get(conversation_id = conversation_id, system_fingerprint = fingerprint)
        files = FilesStaging.objects.filter(conversation_staging = converstion_stage)
        for file in files:
            print(file.actual_file_name+" || "+file.description)
        return HttpUtil.respond(200, None, None)
        
    except Exception as e:
        return HttpUtil.respond(400, str(e))
