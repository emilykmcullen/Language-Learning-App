import pdb
from models.translated_phrase import TranslatedPhrase
from models.first_language_phrase import FirstLanguagePhrase
from models.language import Language
from models.tag import Tag
from models.tag_translated_phrase import tagTranslatedPhrase

import repositories.translated_phrase_repository as translated_phrase_repository
import repositories.first_language_phrase_repository as first_language_phrase_repository
import repositories.language_repository as language_repository
import repositories.tag_repository as tag_repository
import repositories.tag_translated_phrase_repository as tag_translated_phrase_repository


translated_phrase_repository.delete_all()
first_language_phrase_repository.delete_all()
language_repository.delete_all()
tag_repository.delete_all()


tag_1 = Tag("poetic")
tag_repository.save(tag_1)

tag_2 = Tag("greetings")
tag_repository.save(tag_2)

language_1 = Language("italian")
language_repository.save(language_1)

language_2 = Language("spanish")
language_repository.save(language_2)

first_language_phrase_1 = FirstLanguagePhrase("dreamy sigh", "medium")
first_language_phrase_repository.save(first_language_phrase_1)

first_language_phrase_2 = FirstLanguagePhrase("a thimbleful", "medium")
first_language_phrase_repository.save(first_language_phrase_2)

first_language_phrase_3 = FirstLanguagePhrase("hello", "easy")
first_language_phrase_repository.save(first_language_phrase_3)

translated_phrase_1= TranslatedPhrase("sospiro trasognante", language_1, first_language_phrase_1, mastered=False)
translated_phrase_repository.save(translated_phrase_1)

translated_phrase_2= TranslatedPhrase("un goccino", language_1, first_language_phrase_2, mastered=False)
translated_phrase_repository.save(translated_phrase_2)

translated_phrase_3= TranslatedPhrase("ciao", language_1, first_language_phrase_3, mastered=False)
translated_phrase_repository.save(translated_phrase_3)

translated_phrase_4= TranslatedPhrase("hola", language_2, first_language_phrase_3, mastered=False)
translated_phrase_repository.save(translated_phrase_4)

tag_translated_phrase_1 = tagTranslatedPhrase(translated_phrase_1, tag_1)
tag_translated_phrase_repository.save(tag_translated_phrase_1)

tag_translated_phrase_2 = tagTranslatedPhrase(translated_phrase_3, tag_2)
tag_translated_phrase_repository.save(tag_translated_phrase_2)

tag_translated_phrase_3 = tagTranslatedPhrase(translated_phrase_4, tag_2)
tag_translated_phrase_repository.save(tag_translated_phrase_3)




pdb.set_trace()

