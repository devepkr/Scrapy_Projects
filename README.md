# Scrapy_Projects


# Create and Activate a Virtual Environment
# Create the virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (macOS/Linux)
source venv/bin/activate

# Install Scrapy
pip install --upgrade pip
pip install scrapy


# Initialize the Scrapy Project
how to create scrape projects
scrapy startproject myproject

Navigate into the Project and Generate a Spider
 You can start your first spider with:
     cd quotes_projects
     scrapy genspider quotes_spider https://quotes.toscrape.com/

