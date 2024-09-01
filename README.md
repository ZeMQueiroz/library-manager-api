# Library Manager API

The Library Manager API is a Django-based RESTful API designed to help you manage and organize various media types, such as books and anime (more in the future). This API allows you to create, read, update, and delete media items, categorize them, and fetch additional information from external APIs like Google Books and Jikan. It also supports creating custom lists and provides recommendations based on predefined criteria.

## Features

- **Media Item Management:** Handle various media types like books and anime with CRUD (Create, Read, Update, Delete) operations.
- **Custom Lists:** Create and manage custom lists, such as "Favorites," "Seasonal Anime," "Books by Author X," etc.
- **External API Integration:** Automatically fetch detailed information about books from Google Books API and anime from Jikan API.
- **Recommendations:** ---- In Progress ---- Get personalized media recommendations based on categories or predefined logic.
- **Filtering, Searching, and Sorting:** Easily filter, search, and sort media items by attributes such as title, description, status, and more.

## Technologies Used

- **Backend:** Django, Django REST Framework
- **Database:** SQLite (default, can be replaced with other databases like PostgreSQL or MySQL)
- **External APIs:**
  - [Google Books API](https://developers.google.com/books)
  - [Jikan API](https://jikan.moe/)

## Installation

Follow these steps to set up and run the Library Manager API on your local machine.

### Prerequisites

- Python 3.8 or higher
- Virtual environment tool (optional but recommended)
- Git

### Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ZeMQueiroz/library-manager-api.git
   cd library-manager-api

   ```

2. **Set Up Virtual Environment:**

   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`

3. **Install Dependencies:**

   pip install -r requirements.txt

4. **Set Up Virtual Environment:**

   • Create a .env file in the root of your project to store environment-specific settings, such as API keys for Google Books and other sensitive information.
   • Example .env file:
   SECRET_KEY=your-django-secret-key
   DEBUG=True
   GOOGLE_BOOKS_API_KEY=your-google-books-api-key

5. **Run Migrations:**

   python manage.py makemigrations
   python manage.py migrate

6. **Run the Server:**

   python manage.py runserver

7. **Access the API:**

   • Visit http://127.0.0.1:8000/api/ in your browser or API client.

## API Endpoints

### Media Items

- **GET `/api/items/`** - List all media items.
- **POST `/api/items/`** - Create a new media item.
- **GET `/api/items/{id}/`** - Retrieve details of a specific media item.
- **PUT `/api/items/{id}/`** - Update a specific media item.
- **DELETE `/api/items/{id}/`** - Delete a specific media item.

### Categories

- **GET `/api/categories/`** - List all categories.
- **POST `/api/categories/`** - Create a new category.

### Custom Lists

- **GET `/api/lists/`** - List all custom lists.
- **POST `/api/lists/`** - Create a new custom list.
- **GET `/api/lists/{id}/`** - Retrieve details of a specific list.
- **PUT `/api/lists/{id}/`** - Update a specific custom list.
- **DELETE `/api/lists/{id}/`** - Delete a specific custom list.

### Recommendations

- **GET `/api/recommendations/`** - Get recommendations for media items.

## Usage

1. **Create Media Items:** Use the `/api/items/` endpoint to add books or anime to your collection. The API will automatically fetch additional details from external sources.
2. **Manage Lists:** Organize your media items into custom lists for easy access and management.
3. **Explore Recommendations:** Use the recommendations endpoint to discover new media items based on your existing collection.
