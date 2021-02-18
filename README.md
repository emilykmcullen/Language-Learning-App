<h1> Lingua Snaps <h1>

<h2>Deployed App<h2>
<h5>[Lingua Snaps](https://lingua-snaps.herokuapp.com/)<h5>

<h2>Overview<h2>

<h5> When learning a language I always use a notebook to store new phrases and vocabularly, however I 
never return to this notebook to actually practise them! With Lingua Snaps I aimed to solve this issue
by making an app that allows the user to actively practise their phrases they have stored.<h5>

<h2> Main Features<h2>

* The user can create and store phrases in their target language and mother tongue language
* The user can edit and delete phrases
* The user can also create new tags and add languages to the system
* The user can practise their phrases and get feedback on whether they were correct or not
* The user can filter phrases by tags or language 


TO RUN THE APP:

1. psql -d lingua_snaps -f db/lingua_snaps.sql
2. python3 console.py (this will populate the db with the info in console.py, you can then enter q to quit)
3. python3 -m flask run (now you can go to localhost:5000)
4. if you want to check the db use psql -d lingua_snaps