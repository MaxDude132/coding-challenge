from django.test import TestCase

from .models import NinjaWordOption, NinjaName, NinjaWord

# Create your tests here.
class TestNinjaWordOption(TestCase):
    def setUp(self):
        NinjaWordOption.objects.create(word='NinjaWord_Adjective', first_letter='n', word_type='Adjective', adjective_type=5)
        NinjaWordOption.objects.create(word='NinjaWord_Noun', first_letter='n', word_type='Noun')

    def test_adjective_type(self):
        adjective = NinjaWordOption.objects.get(word='NinjaWord_Adjective')
        self.assertEqual(adjective.get_adjective_type(), 5)
        self.assertEqual(adjective.get_adjective_type_display(), 'Color')
        
    def test_word_type(self):
        noun = NinjaWordOption.objects.get(word='NinjaWord_Noun')
        self.assertEqual(noun.word_type, 'Noun')
        self.assertEqual(noun.get_adjective_type(), None)

    def test_first_letter(self):
        noun = NinjaWordOption.objects.get(word='NinjaWord_Noun')
        self.assertEqual(noun.first_letter, 'n')


class TestNinjaName(TestCase):
    def setUp(self):
        self.ninja_name = NinjaName.objects.create(initial_words='test test')
        ninja_word_option = NinjaWordOption.objects.create(word='Crappy', first_letter='n', word_type='Noun')
        NinjaWord.objects.create(ninja_name=self.ninja_name, initial_word='test', is_tech_word=True, is_in_dictionary=True, ninja_word_option=ninja_word_option)

    def test_ninja_name_creation(self):
        name = NinjaWord.objects.get(initial_word='test')
        self.assertEqual(name.get_word(), 'Crappy')
        self.assertEqual(name.ninja_name, self.ninja_name)