class ContextManager:
    def __init__(self, max_context_length=10):
        """
        Initialize the context manager
        
        Args:
            max_context_length (int): Maximum number of messages to keep in context
        """
        self.conversation_history = []
        self.max_context_length = max_context_length
        
    def add_message(self, role, content):
        """
        Add a message to the conversation history
        
        Args:
            role (str): 'user' or 'assistant'
            content (str): Message content
        """
        self.conversation_history.append({"role": role, "content": content})
        
        # Trim history if it exceeds max length
        if len(self.conversation_history) > self.max_context_length:
            # Remove oldest messages but keep the system prompt if it exists
            if self.conversation_history[0]["role"] == "system":
                self.conversation_history = [self.conversation_history[0]] + self.conversation_history[-(self.max_context_length-1):]
            else:
                self.conversation_history = self.conversation_history[-self.max_context_length:]
    
    def get_conversation_context(self):
        """
        Get the current conversation context
        
        Returns:
            list: List of message dictionaries
        """
        return self.conversation_history
    
    def clear_context(self):
        """Clear the conversation history"""
        self.conversation_history = []
        
    def get_context_for_prompt(self):
        """
        Format the conversation history for the AI prompt
        
        Returns:
            list: List of message dictionaries
        """
        return self.conversation_history