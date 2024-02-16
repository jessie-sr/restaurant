# Restaurant Information System

The Restaurant Information System is a web application that allows users to interact with a database of restaurants to view, add, filter, and manage restaurant information.

## Features

The application implements the following user stories:

- **View All Restaurants**: Users can view a list of all available restaurants.
- **View Restaurant Details**: Users can retrieve detailed information about a specific restaurant.
- **Add New Restaurant**: Users can add a new restaurant to the system.
- **Update Restaurant**: Users can update the details of an existing restaurant.
- **Delete Restaurant**: Users can remove a restaurant from the list.
- **Filter Restaurants**: Users can filter restaurants based on location or cuisine.
- **Secure API**: The application ensures secure user interactions with the API.
- **Pagination**: The list of restaurants is paginated to display a maximum of 10 restaurants per page.

## Technologies Used

- **Programming Languages**: Python, JSON, HTML, CSS
- **Framework**: Django
- **Database**: PostgreSQL
- **Python Libraries**: django, sqlalchemy, json, ...

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)
- PostgreSQL

### Installation

1. Clone the repository:
```bash
git clone https://github.com/jessie-sr/restaurant.git
```

2. Navigate to the project directory:
```bash
cd restaurant
```

3. Install required Python libraries:
```bash
pip install -r requirements.txt
```

4. Start the development server:
```bash
python3 manage.py runserver
```

5. Open a web browser and navigate to 'http://127.0.0.1:8000/api/restaurants/' to start using the application.
