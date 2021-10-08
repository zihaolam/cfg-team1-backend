# APIs
- url: http://127.0.0.1:8000 

---
## Authenication
1. Login
- url/auth/login
- Post
- Request:
```
{"username":"tonylee","password":"admin1"}
```
- Response: {"status":<Success/Failed>}

---

## User
1. Get Users List
- url/user/
- Get
- Request: None
- Response: <Array_of_User>

2. Get User by ID
- url/user/{id}
- Get
- Request: None
- Response: 
```
{
   "_id":{
      "$oid":"61603a854de4c5355e1be49e"
   },
   "username":"Ben Wong",
   "role":"trainer",
   "courseHistory":[
   ],
   "rating":80
}
```

3. Create Users
- url/user/create
- Post
- Request: 
```
{
    "username":"zihao_ftw"
    "password":"zihao_ftw123"
    "role":"trainer"
}
```
- Response:
```
{
    "_id":{
      "$oid":"61603a854de4c5355e1be49e"
   },
   "username":"Jane Doe",
   "role":"trainer",
   "courseHistory":[],
   "rating":50
}
```

4. Update Users
- url/user/{id}
- Put
- Request:
```
{
   "username":"zihao (immortal)",
}
```
- Response:
```
{
   "_id":{
      "$oid":"61603a854de4c5355e1be49e"
   },
   "username":"zihao (immortal)",
   "role":"trainer",
   "courseHistory":[
   ],
   "rating":90
}
```

5. Delete Users
- url/user/{id}
- Delete
- Request: None
- Response: <Success/Failed>

---

## Course
1. Get Courses List
- url/course/
- Get
- Request: None
- Response:
  
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

2. Create Courses
- url/course/
- Post
- Request:
```

```
- Response:
```


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