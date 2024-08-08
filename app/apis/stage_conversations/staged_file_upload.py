from app.models.conversation_staging import ConversationStaging
from app.models.files_staging import FilesStaging
from rest_framework.decorators import api_view
from util.http_util import HttpUtil
from django.conf import settings
import base64
import uuid
import os

@api_view(['POST'])
def index(request, conversation_id=None):
    data = request.data

    fingerprint = data.get("fingerprint")
    filename = data.get("filename")
    description = data.get("description")
    file_base64 = data.get("file_base64")
    
    try:
        converstion_stage = ConversationStaging.objects.get(conversation_id = conversation_id, system_fingerprint = fingerprint)
        file_data = base64.b64decode(file_base64)
        _, file_extension = os.path.splitext(filename)
        file_id = uuid.uuid4()
        unique_filename = f"{file_id}{file_extension}"
        if not os.path.exists(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT)
        file_path = os.path.join(settings.MEDIA_ROOT, unique_filename)
        with open(file_path, 'wb') as file:
            file.write(file_data)

        file = FilesStaging()
        file.actual_file_name = filename
        file.conversation_staging = converstion_stage
        file.unique_file_name = unique_filename
        file.description = description
        file.file_id = file_id
        file.save()

        response_dict = {
            'unique_filename': unique_filename,
            'actual_file_name': filename,
            'description': description,
            'file_id' : file_id
        }
        return HttpUtil.respond(200, None, response_dict)
        
    except Exception as e:
        return HttpUtil.respond(400, str(e))
