# streampy
A wrapper for the Streamable API

## Requirements
1. Python 3.6
2. Requests module  
```pip3 install requests```

## Authentication

Streamable allows both authenticated and unauthenticated (anonymous) uploads. If you wish to authenticate, simply enter your credentials into  
```
USER = ''
PASS = ''
```
## Usage

### Create an instance
```s = Streamable()```  

### Upload a video
```s.upload(file='', title='')```  
:params:  
```file``` = the local video file  
```title``` = optional title for the video  

### Upload a video via import  
```s.import_vid(url='', title='')```  
:params:  
```url``` = location of video (youtube link, webm, etc)  
```title``` = optional title for the video  

### Retrieve user
```s.get_user(user='')```  
:params:  
```user``` = user to retrieve

### Retrieve self
```s.get_me()```  
(Requires authentication)  
Returns a User object representing the currently authenticated user

## More Reading  
https://streamable.com/documentation