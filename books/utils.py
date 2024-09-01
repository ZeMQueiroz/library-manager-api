import requests

def fetch_book_info(title):
    api_url = f'https://www.googleapis.com/books/v1/volumes?q={title}'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data:
            book_data = data['items'][0]['volumeInfo']
            return {
                'title': book_data.get('title', ''),
                'description': book_data.get('description', ''),
                'rating': None,  # Modify if you have a different rating field requirement
                'cover_url': book_data.get('imageLinks', {}).get('thumbnail', ''),
            }
    return None

def fetch_anime_info(title):
    api_url = f'https://api.jikan.moe/v4/anime?q={title}&limit=1'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if data['data']:
            anime_data = data['data'][0]
            return {
                'title': anime_data.get('title', ''),
                'description': anime_data.get('synopsis', ''),
                'progress': 0,  # Assuming progress starts at 0
                'rating': None,
                'notes': '',
                'cover_url': anime_data.get('images', {}).get('jpg', {}).get('image_url', ''),
            }
    return None