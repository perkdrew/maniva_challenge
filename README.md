# Maniva Digital Code Challenge

A project involving both a website redesign on the frontend and a structure of user data on the backend.

Tech Stack:
* Python
  * Django
  * Scikit-Learn
  * Libra
* Bootstrap 
  * HTML
  * CSS
  * JS
  * PHP
* VSCode
* Jupyter
* MongoDB 
  * Djongo 
  * Pymongo
  * Compass

* Frontend: 
The initial logic was to work through the frontend construction of the landing page by navigating a quick bootstrap template that I could properly modify given the requirements of the task. I adjusted it to better reflect the existing website. 

* Backend: 
I began to adjoin the contact form from the template with the user input from the frontend. I set up an initial web application for the frontend and backend known as "maniva_webapp". The user input (which was presented in a contact form) was sent to MongoDB on the backend. I replaced the traditional SQLite in Django because of the opportunity to learn something new whilst also utilizing a NoSQL database that doesn't need constant migration updates in Django but is also 100x faster in larger productions. It will also not be trapped by problematic joins in the future. As far as some of the backend features, I was able to manage smtp emails that were automatically sent as each contact form was submitted. However, web push notifications in Django proved more difficult as they relied on more dependencies then I was prepared for. I would've liked to add a category for locations as metadata from converted IP addresses too. Afterwards, I performed some basic data analytics with user data from MongoDB with Scikit-Learn to note the probabilities of message lengths and the common unique terms that were coming up in all the messages. These discoveries would be supplementary to a CRM that aims to make the most of user data and business insights. Given my background in data science and NLP, I was eager to use it in some capacity and I'm sure the value of AI can be further involved in CRMs in the future. Currently, I have a basic CRM that can manage data relevant to the website such as customers/clients, services, and orders.