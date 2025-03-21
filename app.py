import streamlit as st
import time
from ai_integration import GroqIntegration
from context_manager import ContextManager
from knowledge_base import SolarKnowledgeBase

# Page configuration
st.set_page_config(
    page_title="Solar Industry AI Assistant",
    page_icon="☀️",
    layout="wide"
)

# Initialize session state variables
if "conversation" not in st.session_state:
    st.session_state.conversation = ContextManager()
if "messages" not in st.session_state:
    st.session_state.messages = []
if "ai_integration" not in st.session_state:
    st.session_state.ai_integration = GroqIntegration()
if "knowledge_base" not in st.session_state:
    st.session_state.knowledge_base = SolarKnowledgeBase()
if "expert_mode" not in st.session_state:
    st.session_state.expert_mode = False

# Header
st.title("☀️ Solar Industry AI Assistant")
st.markdown("""
This AI assistant specializes in solar industry consulting, providing accurate information 
about solar energy technology, installation, maintenance, costs, regulations, and market trends.
""")

# Sidebar with filters and settings
with st.sidebar:
    st.header("Knowledge Areas")
    st.markdown("""
    Our assistant can help with:
    - 🔋 Solar Panel Technology
    - 🛠️ Installation Processes
    - 🔧 Maintenance Requirements
    - 💰 Cost & ROI Analysis
    - 📑 Industry Regulations
    - 📈 Market Trends
    """)
    
    # Expert mode toggle with callback
    def toggle_expert_mode():
        st.session_state.expert_mode = not st.session_state.expert_mode
        
    expert_mode = st.toggle("Expert Mode", value=st.session_state.expert_mode, 
                           help="Toggle for more technical, detailed responses",
                           on_change=toggle_expert_mode)
    
    # Clear conversation button
    if st.button("Clear Conversation"):
        st.session_state.conversation.clear_context()
        st.session_state.messages = []
        st.rerun()  # Use st.rerun() instead of experimental_rerun()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to process user input and generate response
def process_query(user_query):
    # Add user message to the conversation
    st.session_state.conversation.add_message("user", user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_query)
    
    # Detect topic
    topic = st.session_state.knowledge_base.detect_topic(user_query)
    
    # Get appropriate system prompt
    if topic:
        system_prompt = st.session_state.knowledge_base.get_specialized_prompt(topic)
    else:
        system_prompt = st.session_state.knowledge_base.get_general_prompt()
    
    # Add expert mode modifier if enabled
    if st.session_state.expert_mode:
        system_prompt += "\n\nProvide detailed, technical responses suitable for industry professionals."
    else:
        system_prompt += "\n\nProvide clear, accessible responses suitable for non-technical users."
    
    # Get conversation context
    context = st.session_state.conversation.get_context_for_prompt()
    
    # Display assistant "thinking" spinner
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")
        
        # Get AI response
        response = st.session_state.ai_integration.get_response(context, system_prompt)
        
        # Update displayed message
        message_placeholder.markdown(response)
    
    # Add assistant message to conversation
    st.session_state.conversation.add_message("assistant", response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Chat input
user_query = st.chat_input("Ask me about solar energy...")
if user_query:
    process_query(user_query)