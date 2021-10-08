# APIs
- url: http://127.0.0.1:8000 

---
## Libraries


---
## Authenication
1. Login
- url/auth/login
```
{"username":"tonylee","password":"admin1"}
```
---
## Course
1. Get Courses List
- url/course/
- Get
```
```
2. Create Courses
- url/course/
- Post
```
{
   "name":"Course 1",
   "userId":"61603a6a4de4c5355e1be49c",
   "description":"um.",
   "modules":[
      {
         "name":"Module 1",
         "description":"quiofficia deserunt mollit anim id est laborum.",
         "videoLink":"https://cfg-team1.s3.ap-southeast-1.amazonaws.com/video1.mp4",
         "views":5,
         "questions":[
            
         ],
         "transcript":"",
         "translation":[
            
         ],
         "rating":3,
         "comments":[
            {
               "username":"Lam Zi Hao",
               "text":"This is a great course, will recommend to friends"
            },
            {
               "username":"Kim Ji Hoo",
               "text":"Learned alot form this course"
            }
         ]
      }
   ]
}

```

3. Update Courses
- url/course/{id}
- Put
```
{
   "_id":{
      "$oid":"6160360a1242e82e1db3c88a"
   },
   "name":"Course 1",
   "userId":"61603a6a4de4c5355e1be49c",
   "description":"um.",
   "modules":[
      {
         "name":"Module 1",
         "description":"quiofficia deserunt mollit anim id est laborum.",
         "videoLink":"https://cfg-team1.s3.ap-southeast-1.amazonaws.com/video1.mp4",
         "views":5,
         "questions":[
            
         ],
         "transcript":"",
         "translation":[
            
         ],
         "rating":3,
         "comments":[
            {
               "username":"Lam Zi Hao",
               "text":"This is a great course, will recommend to friends"
            },
            {
               "username":"Kim Ji Hoo",
               "text":"Learned alot form this course"
            }
         ]
      }
   ]
}

```

4. Delete Courses
- url/course/{id}
- Delete

---
## User
1. Get Users List
- url/user/
- Get


2. Create Courses
- url/user/
- Post
```
{
   "username":"Jane Doe",
   "password":"trainer2",
   "role":"trainer",
   "courseHistory":[
      
   ],
   "rating":95
}
```

3. Update Courses
- url/user/{id}
- Put
```
{
   "username":"Jane Doe",
   "password":"trainer2",
   "role":"trainer",
   "courseHistory":[
      
   ],
   "rating":95
}
```

4. Delete Courses
- url/user/{id}
- Delete

---