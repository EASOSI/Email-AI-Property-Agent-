"""Main entry point for the Email AI Property Agent"""

import logging
import sys
from typing import List, Dict, Any
from src.agents.email_agent import EmailAgent
from src.utils.config import EnvConfig

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def validate_configuration() -> bool:
    """Validate that all required configuration is present"""
    required = [
        EnvConfig.OPENAI_API_KEY,
        EnvConfig.SENDER_EMAIL,
        EnvConfig.GOOGLE_MAPS_API_KEY
    ]
    
    if not all(required):
        logger.error("Missing required configuration. Please check .env file.")
        return False
    
    return True


def main():
    """Main application entry point"""
    
    # Validate configuration
    if not validate_configuration():
        logger.error("Configuration validation failed")
        sys.exit(1)
    
    # Initialize agent
    try:
        agent = EmailAgent(config_path="config.yaml")
        logger.info("Email Agent initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize agent: {str(e)}")
        sys.exit(1)
    
    # Example: Process a property
    property_data = {
        'address': '123 Main St, Austin, TX 78701',
        'latitude': 30.2672,
        'longitude': -97.7431,
        'property_type': 'commercial',
        'square_feet': 15000,
        'description': 'Vacant commercial property in downtown Austin',
        'documents': []  # Add document paths here
    }
    
    # Example clients
    clients = [
        {
            'name': 'John Smith',
            'email': 'john@example.com',
            'latitude': 30.2700,
            'longitude': -97.7400,
            'company': 'Smith Properties'
        },
        {
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'latitude': 30.2650,
            'longitude': -97.7450,
            'company': 'Doe Realty'
        }
    ]
    
    # Process property
    logger.info("Processing property...")
    results = agent.process_property(
        property_data=property_data,
        clients=clients,
        verify_documents=False,
        send_emails=False  # Set to True to actually send emails
    )
    
    logger.info(f"Processing complete: {results}")


if __name__ == "__main__":
    main()
