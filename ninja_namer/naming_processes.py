from operator import is_
from . import models

from .dictionary_processes import DictionaryRequests

class MainNamingProcess:
    DICTIONARY_REQUESTS = DictionaryRequests()
    def __init__(self, initial_words):
        self._initial_words = initial_words
        self._initial_words_separated = [word.strip() for word in self._initial_words.split(',') if word.strip()]
        
        self._words = self._get_words(len(self._initial_words_separated) - 1)

        self._ninja_name = self._enter_words_in_database()

    def get_full_name(self):
        query = models.NinjaWord.objects.filter(ninja_name=self._ninja_name)
        
        names = []

        for ninja_word in query:
            names.append(ninja_word.get_word())

        return " ".join(names).title()

    def _get_words(self, adjectives_amount):
        words = []

        adjective_types_to_exclude = []
        words_to_exclude = []

        for _ in range(adjectives_amount):
            adjective = self._get_random_adjective(adjective_types_to_exclude, words_to_exclude)
            words.append(adjective)
            adjective_types_to_exclude.append(adjective.adjective_type)
            words_to_exclude.append(adjective.word)

        words.append(self._get_random_noun(words_to_exclude))

        return words

    def _enter_words_in_database(self):
        ninja_name = models.NinjaName(initial_words=self._initial_words)
        ninja_name.save()

        self._words.sort(key=self._new_words_sort_key)

        for i, old_word in enumerate(self._initial_words_separated):
            new_word = self._words[i]
            self._enter_word_in_database(old_word, new_word, ninja_name)

        return ninja_name

    def _new_words_sort_key(self, word):
        return word.get_adjective_type() or 10

    def _enter_word_in_database(self, initial_word, word, ninja_name):
        is_in_dictionary = self.DICTIONARY_REQUESTS.set_word(word)
        is_tech_word = self.DICTIONARY_REQUESTS.check_is_tech_word() if is_in_dictionary else False

        ninja_word = models.NinjaWord(  
            ninja_name=ninja_name, 
            initial_word=initial_word, 
            is_in_dictionary=is_in_dictionary, 
            is_tech_word=is_tech_word,
            ninja_word_option=word
        )
        ninja_word.save()

    def _get_random_adjective(self, adjective_types_to_exclude, words_to_exclude):
        return models.NinjaWordOption.objects\
                    .filter(word_type=models.NinjaWordOption.ADJECTIVE)\
                    .exclude(adjective_type__contains=adjective_types_to_exclude)\
                    .exclude(word__contains=words_to_exclude)\
                    .order_by('?')[0]

    def _get_random_noun(self, words_to_exclude):
        return models.NinjaWordOption.objects\
                    .filter(word_type=models.NinjaWordOption.NOUN)\
                    .exclude(word__contains=words_to_exclude)\
                    .order_by('?')[0]