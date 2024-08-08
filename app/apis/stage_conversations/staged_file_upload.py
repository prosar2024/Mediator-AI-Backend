from rest_framework.decorators import api_view
from util.http_util import HttpUtil
from django.conf import settings
import base64
import uuid
import os

@api_view(['POST'])
def index(request, conversation_id=None):
    data = request.data
    filename = data.get("filename")
    description = data.get("description")
    file_base64 = data.get("file_base64")
    
    try:
        # Decode the base64 file
        file_data = base64.b64decode(file_base64)
        
        # Get the file extension correctly
        _, file_extension = os.path.splitext(filename)
        
        # Generate a unique UUID filename with the correct extension
        unique_filename = f"{uuid.uuid4()}{file_extension}"
        
        # Ensure the directory exists
        if not os.path.exists(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT)
        
        # Save the file to the desired folder
        file_path = os.path.join(settings.MEDIA_ROOT, unique_filename)
        with open(file_path, 'wb') as file:
            file.write(file_data)

        response_dict = {
            'conversation_id': conversation_id,
            'unique_filename': unique_filename,
            'filename': filename,
            'description': description,
        }
        return HttpUtil.respond(200, None, response_dict)
        
    except Exception as e:
        raise e
        return HttpUtil.respond(400, str(e))
