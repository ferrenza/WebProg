
# Django API Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Endpoints](#endpoints)
   - [GET /api/course](#get-apicourse)
   - [POST /api/course](#post-apicourse)
   - [PUT /api/course/update/:id](#put-apicourseupdateid)
   - [DELETE /api/course/delete/:id](#delete-apicoursedeleteid)
3. [Example Responses](#example-responses)

## Introduction

This API allows you to manage courses. The available operations are creating, reading, updating, and deleting courses.

## Endpoints

### GET /api/course

#### Description
Retrieve a list of all courses.

#### Request
- Method: GET
- URL: `/api/course`

#### Response
- Status: 200 OK
- Body:
  ```json
  [
      {
          "course_id": "06877a80-e728-486f-a5be-f25857022179",
          "course_name": "Data Science 101",
          "course_created_by": "ferrenza",
          "course_created_date": "2024-07-03T02:52:20.996Z",
          "course_updated_by": null,
          "course_updated_date": "2024-07-03T02:52:20.996Z"
      },
      {
          "course_id": "88ac727d-6f21-42e7-a040-6166d1b525a1",
          "course_name": "Matematika Minat",
          "course_created_by": "ferrenza",
          "course_created_date": "2024-07-07T13:35:40.753Z",
          "course_updated_by": null,
          "course_updated_date": "2024-07-07T13:35:40.753Z"
      }
  ]
  ```

### POST /api/course

#### Description
Create a new course.

#### Request
- Method: POST
- URL: `/api/course`
- Headers: `Content-Type: application/json`
- Body:
  ```json
  {
      "course_name": "Matematika Minat",
      "course_created_by": "ferrenza"
  }
  ```

#### Response
- Status: 201 Created
- Body:
  ```json
  {
      "message": "Course created",
      "course_id": "88ac727d-6f21-42e7-a040-6166d1b525a1"
  }
  ```

### PUT /api/course/update/:id

#### Description
Update an existing course.

#### Request
- Method: PUT
- URL: `/api/course/update/:id`
- Headers: `Content-Type: application/json`
- Body:
  ```json
  {
      "course_name": "Matematika Minat Updated",
      "course_updated_by": "admin"
  }
  ```

#### Response
- Status: 200 OK
- Body:
  ```json
  {
      "message": "Course updated"
  }
  ```

#### Error Responses
- Status: 400 Bad Request
  ```json
  {
      "message": "Invalid course ID"
  }
  ```
- Status: 404 Not Found
  ```json
  {
      "message": "Course not found"
  }
  ```

### DELETE /api/course/delete/:id

#### Description
Delete a course.

#### Request
- Method: DELETE
- URL: `/api/course/delete/:id`

#### Response
- Status: 200 OK
- Body:
  ```json
  {
      "message": "Course deleted"
  }
  ```

#### Error Responses
- Status: 400 Bad Request
  ```json
  {
      "message": "Invalid course ID"
  }
  ```
- Status: 404 Not Found
  ```json
  {
      "message": "Course not found"
  }
  ```

## Example Responses

### GET /api/course
```json
[
    {
        "course_id": "06877a80-e728-486f-a5be-f25857022179",
        "course_name": "Data Science 101",
        "course_created_by": "ferrenza",
        "course_created_date": "2024-07-03T02:52:20.996Z",
        "course_updated_by": null,
        "course_updated_date": "2024-07-03T02:52:20.996Z"
    },
    {
        "course_id": "88ac727d-6f21-42e7-a040-6166d1b525a1",
        "course_name": "Matematika Minat",
        "course_created_by": "ferrenza",
        "course_created_date": "2024-07-07T13:35:40.753Z",
        "course_updated_by": null,
        "course_updated_date": "2024-07-07T13:35:40.753Z"
    }
]
```

### POST /api/course
```json
{
    "message": "Course created",
    "course_id": "88ac727d-6f21-42e7-a040-6166d1b525a1"
}
```

### PUT /api/course/update/:id
```json
{
    "message": "Course updated"
}
```

### DELETE /api/course/delete/:id
```json
{
    "message": "Course deleted"
}
```

#### Error Response Examples
##### Invalid Course ID
```json
{
    "message": "Invalid course ID"
}
```

##### Course Not Found
```json
{
    "message": "Course not found"
}
```
