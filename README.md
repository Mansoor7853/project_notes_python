# Getting Started with Note API

## Prerequisites

1. **Install Postman:**
   - Make sure you have [Postman](https://www.postman.com/downloads/) installed on your machine.

2. **API Base URL:**
   - Obtain the base URL for the Note API.

## Authentication
Use Basic Auth after signUp using this URL:
- URL: `{{BASE_URL}}/signup/`
For checking login in into the account.


## Test API Endpoints

### 1. Create New Note

- **Request:**
  - Method: POST
  - URL: `{{BASE_URL}}/notes/create/`
  - Headers:
    - Content-Type: application/json
    - Authorization: Bearer {{ACCESS_TOKEN}}
  - Body:
    ```json
    {
      "content": "This is a new note."
    }
    ```

- **Response:**
  - Status: 201 Created
  - Body:
    ```json
    {
      "message": "Note created successfully."
    }
    ```

### 2. Get Note

- **Request:**
  - Method: GET
  - URL: `{{BASE_URL}}/notes/{note_id}/`
  - Headers:
    - Content-Type: application/json
    - Authorization: Bearer {{ACCESS_TOKEN}}

- **Response:**
  - Status: 200 OK
  - Body:
    ```json
    {
      "id": 1,
      "content": "This is a new note.",
      "owner": "your_username"
    }
    ```

### 3. Share Note

- **Request:**
  - Method: POST
  - URL: `{{BASE_URL}}/notes/share/`
  - Headers:
    - Content-Type: application/json
    - Authorization: Bearer {{ACCESS_TOKEN}}
  - Body:
    ```json
    {
      "note_id": 1,
      "shared_users": ["other_user_id"]
    }
    ```

- **Response:**
  - Status: 200 OK
  - Body:
    ```json
    {
      "message": "Note shared successfully."
    }
    ```

### 4. Update Note

- **Request:**
  - Method: PUT
  - URL: `{{BASE_URL}}/notes/{note_id}/update/`
  - Headers:
    - Content-Type: application/json
    - Authorization: Bearer {{ACCESS_TOKEN}}
  - Body:
    ```json
    {
      "content": "This note has been updated."
    }
    ```

- **Response:**
  - Status: 200 OK
  - Body:
    ```json
    {
      "message": "Note updated successfully."
    }
    ```

### 5. Get Note Version History

- **Request:**
  - Method: GET
  - URL: `{{BASE_URL}}/notes/version-history/{note_id}/`
  - Headers:
    - Content-Type: application/json
    - Authorization: Bearer {{ACCESS_TOKEN}}

- **Response:**
  - Status: 200 OK
  - Body:
    ```json
    {
      "version_history": [
        {
          "timestamp": "2024-02-19T12:00:00Z",
          "user": "user1",
          "changes": "Added a new line."
        },
        {
          "timestamp": "2024-02-20T14:30:00Z",
          "user": "user2",
          "changes": "Modified content."
        }
      ]
    }
    ```

---

Note:
The code can be optimized to create more user-friendly code, but given the time it was not possible.
All the requirements are met as per the document provided.
