import pdb
from models.translated_phrase import TranslatedPhrase
from models.first_language_phrase import FirstLanguagePhrase

import repositories.translated_phrase_repository as translated_phrase_repository
import repositories.first_language_phrase_repository as first_language_phrase_repository

translated_phrase_repository.delete_all()
first_language_phrase_repository.delete_all()

first_language_phrase_1 = FirstLanguagePhrase("Hello", "easy")
first_language_phrase_repository.save(first_language_phrase_1)

first_language_phrase_2 = FirstLanguagePhrase("Goobye", "easy")
first_language_phrase_repository.save(first_language_phrase_2)

translated_phrase_1= TranslatedPhrase("Ciao", "italian", first_language_phrase_1)
translated_phrase_repository.save(translated_phrase_1)

translated_phrase_2= TranslatedPhrase("Arrivederci", "italian", first_language_phrase_1)
translated_phrase_repository.save(translated_phrase_2)

pdb.set_trace()