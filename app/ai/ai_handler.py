class AIHandler():

    @staticmethod
    def talk(conversation_id, user_message, full_json_conversation_history):
        pass
    
    @staticmethod
    def stage_talk(conversation_id, user_message, full_json_conversation_history):
        #Put the API code here
        if(user_message == None):
            return "Hello, welcome to MediatorAI, how can i asist you today?"
        else:
            return "AI Response  : "+str(user_message)
    
    