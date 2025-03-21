# Solar Industry AI Assistant

An intelligent assistant providing accurate, helpful information about solar energy to both technical and non-technical users.

## Features

- 💬 Interactive chat interface
- 🔋 Comprehensive solar industry knowledge
- 👩‍🔧 Technical and non-technical response modes
- 🧠 Context-aware conversations
- 🌐 Topic detection for specialized responses

## Knowledge Areas

- Solar Panel Technology
- Installation Processes
- Maintenance Requirements
- Cost & ROI Analysis
- Industry Regulations
- Market Trends

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Groq API key

### Installation

1. Clone this repository:
   git clone <repository-url>
cd solar-assistant

2. Install required packages:
   pip install -r requirements.txt

3. Create a `.env` file with your API key:
   GROQ_API_KEY=your_groq_api_key_here

### Running Locally

Start the Streamlit application:
streamlit run app.py


The application will be available at http://localhost:8501

## Deployment

This application can be deployed to Streamlit Cloud:

1. Push your code to a GitHub repository
2. Connect to Streamlit Cloud (https://streamlit.io/cloud)
3. Select your repository and branch
4. Add your secrets (GROQ_API_KEY)
5. Deploy

## Usage Examples

See the `examples` directory for sample conversations and use cases.

## Implementation Details

- **AI Integration**: Using Groq API with LLaMA3 model for fast, high-quality responses
- **Context Management**: Maintains conversation history for contextual responses
- **Knowledge Base**: Specialized prompts for different solar industry topics
- **Topic Detection**: Automatically identifies query topics for specialized knowledge

## Future Improvements

- Add more sophisticated topic detection using embeddings
- Implement a vector database for storing and retrieving specific solar knowledge
- Add support for file uploads (e.g., electricity bills for cost analysis)
- Enhance visualization capabilities for ROI calculations
- Add multilingual support for international users

## Error Handling

The application includes error handling for:
- API communication issues
- Invalid user inputs
- Context management edge cases

## License

[MIT License](LICENSE)
