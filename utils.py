# utils.py (Revisi untuk mendukung page_token)
import os
import requests

def get_secret(key):
    """
    Retrieves a secret variable from the environment.
    """
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"Environment variable '{key}' not set.")
    return value

# --- FUNGSI get_blogger_posts YANG DIPERBARUI ---
def get_blogger_posts(blog_id, api_key, max_results=10, page_token=None): # <-- Tambahkan page_token=None di sini
    """
    Fetches a list of posts from a specified Blogger blog.
    """
    base_url = f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts"
    
    # Siapkan parameter untuk request
    params = {
        'key': api_key,
        'fetchBodies': True, # Pastikan konten postingan juga diambil
        'maxResults': max_results
    }
    
    # Jika ada page_token, tambahkan ke parameter
    if page_token:
        params['pageToken'] = page_token

    try:
        response = requests.get(base_url, params=params) # Gunakan params dictionary
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Blogger posts: {e}")
        return None
# --- AKHIR FUNGSI get_blogger_posts YANG DIPERBARUI ---
