from audioop import maxpp
from django.db import models


# Create your models here
class NinjaWordOption(models.Model):
    NOUN = 'N'
    ADJECTIVE = 'A'
    WORD_TYPES = [
        ('N', 'Noun'),
        ('A', 'Adjective')
    ]
    ADJECTIVE_TYPES = [
        (1, 'Opinion'),
        (2, 'Size'),
        (3, 'Shape'),
        (4, 'Age'),
        (5, 'Color'),
        (6, 'Origin'),
        (7, 'Material'),
        (8, 'Purpose')
    ]

    word = models.CharField(max_length=50)
    first_letter = models.CharField(max_length=1)
    word_type = models.CharField(max_length=1, choices=WORD_TYPES)
    adjective_type = models.IntegerField(choices=ADJECTIVE_TYPES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.word}: {self.get_word_type_display()}"

    def get_adjective_type(self):
        return self.adjective_type


class NinjaName(models.Model):
    initial_words = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


class NinjaWord(models.Model):
    ninja_name = models.ForeignKey(NinjaName, on_delete=models.CASCADE)
    initial_word = models.CharField(max_length=50)
    is_tech_word = models.BooleanField(default=False)
    is_in_dictionary = models.BooleanField(default=False)
    ninja_word_option = models.ForeignKey(NinjaWordOption, on_delete=models.CASCADE, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_word(self):
        return self.ninja_word_option.word

    def __str__(self):
        return f"{self.ninja_word_option.word}: {self.ninja_word_option.get_word_type_display()}"
