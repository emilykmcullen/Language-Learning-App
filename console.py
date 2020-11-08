import pdb
from models.translated_phrase import TranslatedPhrase
from models.first_language_phrase import FirstLanguagePhrase
from models.language import Language

import repositories.translated_phrase_repository as translated_phrase_repository
import repositories.first_language_phrase_repository as first_language_phrase_repository
import repositories.language_repository as language_repository


translated_phrase_repository.delete_all()
first_language_phrase_repository.delete_all()
language_repository.delete_all()

language_1 = Language("italian")
language_repository.save(language_1)

language_2 = Language("spanish")
language_repository.save(language_2)

first_language_phrase_1 = FirstLanguagePhrase("Hello", "easy")
first_language_phrase_repository.save(first_language_phrase_1)

first_language_phrase_2 = FirstLanguagePhrase("Goodbye", "easy")
first_language_phrase_repository.save(first_language_phrase_2)

translated_phrase_1= TranslatedPhrase("Ciao", language_1, first_language_phrase_1, mastered=False)
translated_phrase_repository.save(translated_phrase_1)

translated_phrase_2= TranslatedPhrase("Adios", language_2, first_language_phrase_2, mastered=False)
translated_phrase_repository.save(translated_phrase_2)



pdb.set_trace()

