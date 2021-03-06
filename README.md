## **---------------POKEDEX--------------**

### **Project by Tor Cox & Yaseen Mohamed**

----

#### Table of Contents:


1. Description
2. Complexity
3. Video Demos
4. Presentation Link
5. REST API Specification
6. OO API 
7. User Interaction
----



**DESCRIPTION**

Our user-friendly and interactive pokedex can be used by clients in order to search through the
multitude of pokemon (over 800) and can be used to make your own pokedex by allowing the user to 
delete the whole index, create their own, or even update existing pokemon and make them unique.
Our biggest source for our data is a json file with a plethora of pokemon. Specifically it is a big list of dictionaries of the pokemon. Using this json file we were able to create our list and implement it into our REST API.

**COMPLEXITY**

Subjectively pretty high complexity, considering there are many moving parts with over 15 files, 1500+ lines of code, and each with their own functions and variables, as well as using various types of requests. For second year college students entering into their third year, and with a time constraint of about 4-5 days, this project seemed to challenge us but proved to be a great learning experience as well. From building our own backend REST API server, controllers with event handlers, object oriented library, unit tests, and then connecting it to our own front end UI, we would say this was our most challenging, yet exciting project to date.

**VIDEO DEMOS**

[Front End](https://youtu.be/9v0st2wKif0) walkthrough video

[Code]( https://youtu.be/KGjdX68acxI ) walkthrough video


**PRESENTATION LINK**

Google Presentation [Link](https://docs.google.com/presentation/d/1SMJPQVrhuJrQnuTn6PggtxTwEj3u8_uWXUhT5RFElXc/edit?usp=sharing)


**REST API SPECIFICATION**

[Here](https://imgur.com/a/DDryA05) is the Rest API Specification Table

**OBJECT ORIENTED API**

JSON format for Pokemon


| Key | Value |
| ------ | ------ |
| id   |  1  |
| name | Bulbasaur |
| type | Grass |
| base |       |
| HP   |  45   |
| Attack   |  49   |
| Defense   |  45   |
| Sp. Attack|  65   |
| Sp. Defense   |  65   |
| Speed   |  45   |


**USER INTERACTION**

Our Pokedex contained a couple pages for the user to interact with. First there is the main loading page. When first accessing the site the user will land on the search page where they can search for a specific pokemon by name, or get a list of all the pokemon. Then there is a modify page where a user can modify a pokemon's name, type, stats, and upload an image for them. Next we have an add pokemon page where the user has the same controls as modifying a pokemon. Finally there is a reset page and a delete page. Where the user has the option to reset a pokemon in the list to it's original values, or can delete a certain pokemon or all if they would like.
