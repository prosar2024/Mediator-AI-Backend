from django.urls import path
from app.apis.mediators.fetch_all import index as mediator_fetch_all
from app.apis.mediators.fetch import index as mediator_fetch
from app.apis.mediators.add_or_update import index as mediator_add_or_update
from app.apis.parties.fetch import index as party_fetch
from app.apis.parties.add_or_update import index as party_add_or_update
from app.apis.cases.fetch import index as case_fetch
from app.apis.cases.add_or_update import index as case_add_or_update
from app.apis.conversations.converse import index as handle_conversation
from app.apis.stage_conversations.stage_conversation import index as stage_conversation
from app.apis.stage_conversations.show_conversations import index as show_conversation
from app.apis.stage_conversations.staged_file_upload import index as staged_file_upload
from app.apis.stage_conversations.notify_file_upload_completion import index as notify_file_upload_completion


urlpatterns = [

    #path(r'ask/', index, name="URL to prompty AI"),
    
    #Mediators APIS
    path(r'mediator/fetch/all', mediator_fetch_all, name="URL to fetch all Moderators"),
    path(r'mediator/fetch/<str:mediator_id>', mediator_fetch, name="URL to fetch a Moderator"),
    path(r'mediator/add', mediator_add_or_update, name="URL to add a Moderator"),
    path(r'mediator/update/<str:mediator_id>', mediator_add_or_update, name="URL to update a Moderator"),
     
    #Cases APIS
    path(r'cases/fetch/<str:case_id>', case_fetch, name="URL to fetch a Case info"),
    path(r'cases/add', case_add_or_update, name="URL to add a new Case"),
    path(r'cases/update/<str:case_id>', case_add_or_update, name="URL to update an existing Case"),
    
    #Parties APIS
    path(r'cases/<str:case_id>/parties/fetch', party_fetch, name="URL to fetch a Party info"),
    path(r'cases/<str:case_id>/parties/fetch/<str:party_id>', party_fetch, name="URL to fetch a Party info"),
    path(r'cases/<str:case_id>/parties/add', party_add_or_update, name="URL to add a new party to a case"),
    path(r'cases/<str:case_id>/parties/update/<str:party_id>', party_add_or_update, name="URL to update a party on a case"),
   
    #Conversations
    path(r'cases/<str:case_id>/parties/<str:party_id>/conversation', handle_conversation, name="URL to make a conversation with the AI"),




    path(r'stage/conversation/<str:conversation_id>', stage_conversation, name="URL to stage a conversation with the AI"),
    path(r'stage/conversation/', stage_conversation, name="URL to stage a conversation with the AI"),
    path(r'stage/conversation/show/<str:conversation_id>', show_conversation, name="URL to show the conversation hostory"),
    path(r'stage/conversation/fileupload/<str:conversation_id>', staged_file_upload, name="URL to upload file"),
    path(r'stage/conversation/fileupload/notifycompletion/<str:conversation_id>', notify_file_upload_completion, name="URL to notify file upload completion"),
]