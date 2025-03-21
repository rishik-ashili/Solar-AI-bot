class SolarKnowledgeBase:
    def __init__(self):
        """Initialize the solar knowledge base with system prompts for various topics"""
        
        # Base system prompt for all interactions
        self.base_prompt = """
        You are an expert solar industry consultant assistant. Provide accurate, helpful information about solar energy 
        to both technical and non-technical users. Always be professional, concise, and factual.
        Base your responses on current industry knowledge as of October 2024.
        """
        
        # Specialized knowledge areas
        self.knowledge_areas = {
            "technology": """
            Knowledge area: Solar Panel Technology
            
            You're specialized in explaining solar photovoltaic (PV) technology, including:
            - Monocrystalline, polycrystalline, and thin-film panels
            - Efficiency ratings and technological advances
            - Inverters (string, microinverters, power optimizers)
            - Battery storage systems
            - Solar tracking systems
            - Bifacial panels and other emerging technologies
            
            Provide technical details when appropriate, but can also simplify concepts for non-experts.
            """,
            
            "installation": """
            Knowledge area: Installation Processes
            
            You're knowledgeable about solar installation procedures, including:
            - Site assessment and system design considerations
            - Roof types and mounting systems
            - Electrical integration and grid connection
            - Permitting requirements
            - Safety standards and best practices
            - Typical installation timelines and processes
            - Common installation challenges and solutions
            """,
            
            "maintenance": """
            Knowledge area: Maintenance Requirements
            
            You understand solar system maintenance, including:
            - Routine cleaning and inspection recommendations
            - Monitoring system performance
            - Troubleshooting common issues
            - Component lifespans and replacement considerations
            - Warranties and service agreements
            - Seasonal maintenance adjustments
            - Professional vs. DIY maintenance approaches
            """,
            
            "roi": """
            Knowledge area: Cost & ROI Analysis
            
            You can provide insights on solar economics, including:
            - Initial investment ranges and financing options
            - Energy production calculations and savings estimates
            - Payback period analysis methods
            - Available incentives (tax credits, rebates, SRECs)
            - Net metering and feed-in tariff considerations
            - Long-term ROI projections and factors
            - Property value impacts of solar installations
            """,
            
            "regulations": """
            Knowledge area: Industry Regulations
            
            You're informed about solar regulations, including:
            - Federal, state, and local incentive programs
            - Building codes and electrical standards
            - Interconnection requirements
            - Net metering policies
            - Homeowner association considerations
            - Solar access rights
            - Import tariffs and domestic content requirements
            """,
            
            "trends": """
            Knowledge area: Market Trends
            
            You follow solar industry trends, including:
            - Current market growth patterns
            - Price trends for equipment and installation
            - Emerging technologies and innovations
            - Industry consolidation and competition patterns
            - Global supply chain developments
            - Integration with smart home and EV technologies
            - Commercial and utility-scale market developments
            """
        }
    
    def get_general_prompt(self):
        """Get the general system prompt for solar assistant"""
        return self.base_prompt
    
    def get_specialized_prompt(self, topic):
        """
        Get a specialized system prompt based on the topic
        
        Args:
            topic (str): Knowledge area topic
            
        Returns:
            str: Combined base prompt and specialized knowledge
        """
        if topic in self.knowledge_areas:
            return self.base_prompt + "\n\n" + self.knowledge_areas[topic]
        return self.base_prompt
    
    def detect_topic(self, query):
        """
        Detect the most relevant knowledge area for a query
        
        Args:
            query (str): User query
            
        Returns:
            str: Detected topic key
        """
        query = query.lower()
        
        # Simple keyword matching for topic detection
        keywords = {
            "technology": ["panel", "module", "efficiency", "monocrystalline", "polycrystalline", "thin-film", 
                          "inverter", "microinverter", "power optimizer", "battery", "storage", "bifacial"],
            "installation": ["install", "mounting", "roof", "position", "orientation", "angle", "setup", "wiring", 
                            "connect", "placement", "site assessment", "permit"],
            "maintenance": ["maintain", "clean", "service", "repair", "monitor", "inspect", "performance", 
                           "troubleshoot", "issue", "problem", "warranty"],
            "roi": ["cost", "price", "saving", "financial", "investment", "return", "payback", "economic", 
                   "financing", "loan", "lease", "ppa", "value", "tax credit", "incentive"],
            "regulations": ["regulation", "code", "standard", "requirement", "permit", "law", "policy", 
                           "compliance", "legal", "hoa", "utility", "grid", "net metering"],
            "trends": ["trend", "market", "growth", "future", "development", "innovation", "emerging", 
                      "new technology", "industry", "forecast", "prediction"]
        }
        
        # Count keyword matches for each topic
        topic_scores = {topic: 0 for topic in self.knowledge_areas.keys()}
        
        for topic, topic_keywords in keywords.items():
            for keyword in topic_keywords:
                if keyword in query:
                    topic_scores[topic] += 1
        
        # Find topic with highest score
        best_topic = max(topic_scores.items(), key=lambda x: x[1])
        
        # If no clear match found, return general
        if best_topic[1] == 0:
            return None
            
        return best_topic[0]