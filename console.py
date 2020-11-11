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

tag_3 = Tag("food")
tag_repository.save(tag_3)

language_1 = Language("italian")
language_repository.save(language_1)

language_2 = Language("spanish")
language_repository.save(language_2)

language_3 = Language("german")
language_repository.save(language_3)

first_language_phrase_1 = FirstLanguagePhrase("I looked out of the window and did a dreamy sigh", "medium")
first_language_phrase_repository.save(first_language_phrase_1)

first_language_phrase_2 = FirstLanguagePhrase("a drop of milk", "medium")
first_language_phrase_repository.save(first_language_phrase_2)

first_language_phrase_3 = FirstLanguagePhrase("hello", "easy")
first_language_phrase_repository.save(first_language_phrase_3)

first_language_phrase_4 = FirstLanguagePhrase("my secret dream", "medium")
first_language_phrase_repository.save(first_language_phrase_4)

first_language_phrase_5 = FirstLanguagePhrase("I allowed myself a pleasant read", "difficult")
first_language_phrase_repository.save(first_language_phrase_5)

first_language_phrase_6 = FirstLanguagePhrase("what a struggle", "easy")
first_language_phrase_repository.save(first_language_phrase_6)

first_language_phrase_7 = FirstLanguagePhrase("I like breakfast", "easy")
first_language_phrase_repository.save(first_language_phrase_7)

translated_phrase_1= TranslatedPhrase("ho guardato dalla finestra e ho fatto un sospiro sognante", language_1, first_language_phrase_1, mastered=False)
translated_phrase_repository.save(translated_phrase_1)

translated_phrase_2= TranslatedPhrase("una goccia di latte", language_1, first_language_phrase_2, mastered=False)
translated_phrase_repository.save(translated_phrase_2)

translated_phrase_3= TranslatedPhrase("ciao", language_1, first_language_phrase_3, mastered=True)
translated_phrase_repository.save(translated_phrase_3)

translated_phrase_4= TranslatedPhrase("hola", language_2, first_language_phrase_3, mastered=False)
translated_phrase_repository.save(translated_phrase_4)

translated_phrase_5 = TranslatedPhrase("il mio sogno nel cassetto", language_1, first_language_phrase_4, mastered=True)
translated_phrase_repository.save(translated_phrase_5)

translated_phrase_6 = TranslatedPhrase("mi sono concessa una piacevole lettura", language_1, first_language_phrase_5, mastered=False)
translated_phrase_repository.save(translated_phrase_6)

translated_phrase_7 = TranslatedPhrase("che fatica", language_1, first_language_phrase_6, mastered=False)
translated_phrase_repository.save(translated_phrase_7)

translated_phrase_8 = TranslatedPhrase("Ich frühstücke gern", language_3, first_language_phrase_7, mastered=False)

tag_translated_phrase_1 = tagTranslatedPhrase(translated_phrase_1, tag_1)
tag_translated_phrase_repository.save(tag_translated_phrase_1)

tag_translated_phrase_2 = tagTranslatedPhrase(translated_phrase_5, tag_1)
tag_translated_phrase_repository.save(tag_translated_phrase_2)

tag_translated_phrase_3 = tagTranslatedPhrase(translated_phrase_2, tag_3 )
tag_translated_phrase_repository.save(tag_translated_phrase_3)

tag_translated_phrase_4 = tagTranslatedPhrase(translated_phrase_8, tag_3)


pdb.set_trace()

