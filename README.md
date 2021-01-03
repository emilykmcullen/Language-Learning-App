Language practice app

MVP:
-The app should allow the user to practise sentences and words in their target language
-The user should be able to add sentences in English, choose their target language from a drop-down list, write their target language sentence and choose the difficulty level from a drop-down list
-The user should be able to edit and delete sentences
-Once created the user should be able to see only the English version of their sentence/ word
-When they click on the sentence/ word they should be able to input their target language translation
-They should receive feedback on whether they were correct or incorrect
-The user should be able to ‘show’ the answer if they are unable to get it correct

POSSIBLE EXTENSIONS:
-The user could be able to sort the sentences by ‘tags’
-The user could be able to move sentences/words from an ‘in practice’ section to a ‘mastered’ 
  section once they are confident with the sentence and don’t want to practice it anymore
-The user could be able to generate a random one of their sentences to practise rather than selecting it themselves

TO RUN THE APP:

1. psql -d lingua_snaps -f db/lingua_snaps.sql
2. python3 console.py (this will populate the db with the info in console.py, you can then enter q to quit)
3. python3 -m flask run (now you can go to localhost:5000)
4. if you want to check the db use psql -d lingua_snaps