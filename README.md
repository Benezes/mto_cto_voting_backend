# Voting System

This is a Django-based voting system that allows authenticated users to create posts and vote on them.

## Features

- User registration and JWT-based authentication
- Create, retrieve, update, and delete posts
- Upvote/downvote posts

## Setup

1.  Clone the repository
2.  Install dependencies: `pip install -r requirements.txt`
3.  Run migrations: `python manage.py migrate`
4.  Start the development server: `python manage.py runserver`

## API Endpoints

### Authentication

-   **POST /api/token/**: Obtain JWT token pair.
    -   Payload: `{ "username": "your_username", "password": "your_password" }`
    -   Returns: `{ "refresh": "...", "access": "..." }`
-   **POST /api/token/refresh/**: Refresh JWT token.
    -   Payload: `{ "refresh": "your_refresh_token" }`
    -   Returns: `{ "access": "..." }`

### Users

-   **POST /api/users/**: Register a new user.
    -   Payload: `{ "username": "new_username", "password": "new_password" }`
    -   Returns: `{ "id": 1, "username": "new_username" }`

### Posts

-   **GET /api/posts/**: List all posts.
    -   Returns: `[{ "id": 1, "title": "Post Title", "content": "Post content", "author": "author_username", "created_at": "...", "votes": 0 }]`
-   **POST /api/posts/**: Create a new post. (Authentication required)
    -   Payload: `{ "title": "Post Title", "content": "Post content" }`
    -   Returns: `{ "id": 1, "title": "Post Title", "content": "Post content", "author": "author_username", "created_at": "...", "votes": 0 }`
-   **GET /api/posts/<id>/**: Retrieve a specific post.
    -   Returns: `{ "id": 1, "title": "Post Title", "content": "Post content", "author": "author_username", "created_at": "...", "votes": 0 }`
-   **PUT /api/posts/<id>/**: Update a specific post. (Authentication required, must be owner)
    -   Payload: `{ "title": "Updated Title", "content": "Updated content" }`
    -   Returns: `{ "id": 1, "title": "Updated Title", "content": "Updated content", "author": "author_username", "created_at": "...", "votes": 0 }`
-   **DELETE /api/posts/<id>/**: Delete a specific post. (Authentication required, must be owner)
    -   Returns: `204 No Content`

### Votes

-   **POST /api/posts/<id>/vote/**: Upvote or downvote a post. (Authentication required)
    -   Payload: `{ "value": 1 }` for upvote, or `{ "value": -1 }` for downvote.
    -   Returns: `200 OK` (vote created/updated) or `204 No Content` (vote deleted).
