# -python-django-video-calling-application
 DISCRPTION :
 
 Video calling has become increasingly popular as a way to stay connected with friends, 
family, and colleagues, and video calling applications have been developed to make it easier than ever
to make video calls. This project aims to develop a video calling application using the Django 
framework. The application will provide users with the ability to initiate video calls without creating 
an account. It will also feature real-time video and audio streaming, encryption for secure calls, and
high-definition video quality. The application will be developed using the latest web technologies 
available, such as HTML, CSS, JavaScript, and Bootstrap, as well as using the Django framework. 
Additionally, third-party Agora APIs will be integrated for authentication and other features. The 
application will be tested for performance and usability, and will be optimized for mobile devices. 

  EXISTING METHOD :
  
  The existing system for video calling application using Django is to create a web application 
using the Django framework and the Django REST Framework. The web application should use web 
sockets to allow users to make video calls to each other. This involves configuring server and setting 
up the client-side code. This app is inspired by many social media applications like Google Meet 
which help in connecting with people via Video Chat. The control options were hugely inspired from 
Google meet, Zoom meet. The minor flaws that were felt in the above mentioned apps where kept in 
mind, so that they can be removed, tuned or addressed. 

IMPLEMENTATION :

1. Setting Up Agora SDK: The first step is to set up the Agora SDK for your video call 
application. This involves registering and creating an Agora account, downloading the Agora SDK 
and integrating it into your application. 
2. Setup Video Session: After you have installed the Agora SDK, you can setup a video 
session. This can be done by creating an Agora Video Client instance and configuring the video 
settings, such as video resolution, bit rate, and frame rate. 
 3. Join Video Call: After the video session has been setup, you can join the video call by 
calling the join() method. This will require the user to enter a channel name and a user ID. 
4. Display Video Streams: Once the user has joined the video call, you can display the video 
streams from all the participants using the Agora SDK’s method. 
5. Implement Call-Related Features: To implement call-related features, such as mute/unmute 
audio, mute/unmute video and leave the call, you can use the methods available in the Agora SDK. 
 6. End Video Call: Finally, when the video call has ended, you can call the leave() method to 
leave the call and clean up the video session.

![image](https://github.com/ArunMuthukumarasamy/-python-django-video-calling-application/assets/123149917/6676b68c-5f74-47ec-941c-f5e60a5fc1d5)
