# Institute-Management-System
 App-Institute Management System

We are having following entities.Created  RESTful web services for these.

Course: id (pk), name, duration, fees
Subject: id (pk), name, description
Batch: id (pk), start_time, end_time, start_date
Student: id (pk), name, dob, gender, address, phone, email
Teacher: id(pk), name, dob, gender, address, phone, email, experience

Course and Subject are having many to many relation
Course and Batch are having one to many relation
Student and Batch are having many to many relation
Teacher and Batch are having many to many relation
Teacher and Subject are having many to many relation to store the skills of teacher

For course  APIs:
1. Get all courses
   Endpoint: http://127.0.0.1:8000/course
   Method: GET
   return courses along with their associated subjects

2. Add Course
   Endpoint: http://127.0.0.1:8000/course
   Method: POST
   contain a request body which have attributes for a course and we also need to pass subject IDs in this request body to relate this course with subjects
   Return a proper JSON response that course is added

3. Get course by id
   Endpoint: http://127.0.0.1:8000/course/{id}
   Method: GET
   return a course along with its associated subjects for given course id in endpoint

4. Remove course
   Endpoint: http://127.0.0.1:8000/course/{id}
   Method: DELETE
   return a proper JSON response with a message that course is removed

5. Update course 
   Endpoint: http://127.0.0.1:8000/course/{id}
   Method: PUT
   contain a request body which have new values of attributes for a course to be updated

For subject APIs:

1. Add new Subject:
   Endpoint: http://127.0.0.1:8000/subject
   Method: POST
   contain a request body which have values of attributes for a subject to be added

2. Get all subjects:
   Endpoint: http://127.0.0.1:8000/subject
   Method: GET
   return all the subjects 

3. Get subject by id:
   Endpoint: http://127.0.0.1:8000/subject/{id}
   Method: GET
   return a subject for given subject id in endpoint

4. Remove subject:
   Endpoint: http://127.0.0.1:8000/subject/{id}
   Method: DELETE
   return a proper json response

5. Update subject:
   Endpoint: http://127.0.0.1:8000/subject/{id}
   Method: PUT
    contain request body which have new values of subject to be updated

For Batch  APIs:

1. Add a batch
   Endpoint: http://127.0.0.1:8000/batch
   Method: POST
   contain a request body which have values of attributes for a batch to be added and we also need to pass the course id of into the request body to relate this batch with a course

2. Get all batches
   Endpoint: http://127.0.0.1:8000/batch
   Method: GET
   return all the batches along with the data of associated course with it and course must contain its associated subjects

3. Get batch by id
   Endpoint: http://127.0.0.1:8000/batch/{id}
   Method: GET
   return all the batches along with the data of associated course with it and course must contain its associated subjects for the given subject id in endpoint

4. Remove batch:
   Endpoint: http://127.0.0.1:8000/batch/{id}
   Method: DELETE
   return a proper JSON response

5. Update batch:
   Endpoint: http://127.0.0.1:8000/batch/{id}
   Method: PUT
   contain request body which have new values of batch to be updated
