import json
import logging

from django.http import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from translations.models import BusinessText
from translations.utils import Languages
from words.models import WordZH, WordPL, to_word_model


logger = logging.getLogger(__name__)


def words_translations(request, source_language):
    """
    Manage words translations. Allow selecting words to edit.
    If exist display available translations.
    :param request: HTTP request
    :param source_language: language to translate words from
    :return: HTTP response
    """
    if request.is_ajax():
        source_word_model = to_word_model(source_language)
        if 'translations' in request.POST:
            delete_translations(request.POST['word_to_translate'], source_word_model)
            add_translations(request.POST['word_to_translate'],
                             source_word_model,
                             json.loads(request.POST['translations']))
            return JsonResponse({})
        elif 'word_to_search' in request.POST:
            matching_words = source_word_model.objects.filter(word__startswith=request.POST['word_to_search'])[:5].values_list('word', flat=True)
            return JsonResponse({'matching_words': list(matching_words)})
        elif 'word_to_translate' in request.POST:
            translations = get_translations_if_word_exists(request.POST['word_to_translate'], source_word_model)
            return JsonResponse({'translations': translations})
        else:
            return HttpResponseBadRequest('Unrecognized request', content_type='application/javascript')
    return render(request, 'translations/words_translations.html', {'source_language': source_language})


def get_translations_if_word_exists(word_to_search, word_model):
    try:
        if word_model == WordZH:
            return list(WordZH.objects.get(word=word_to_search).wordpl_set.values('word'))
        elif word_model == WordPL:
            return list(WordPL.objects.get(word=word_to_search).wordzh_set.values('word', 'pinyin'))
        else:
            logger.error("Unknown word model: " + word_model)
            return list()
    except ObjectDoesNotExist:
        return list()


def delete_translations(word_to_translate, source_word_model):
    for word_to_translate in source_word_model.objects.filter(word=word_to_translate):
        word_to_translate.get_translations().clear()


def add_translations(word_to_translate, source_word_model, translations):
    if source_word_model == WordPL:
        word_to_translate = WordPL.objects.get_or_create(word=word_to_translate)[0]
        for translation in translations:
            new_word_zh = WordZH.objects.get_or_create(word=translation['word'], pinyin=translation['pinyin'])[0]
            word_to_translate.add(new_word_zh)
    else:
        word_to_translate = WordZH.objects.get_or_create(word=word_to_translate)[0]  # TODO: user should specify pinyin of source word?
        for translation in translations:
            new_word_pl = WordPL.objects.get_or_create(word=translation['word'])[0]
            word_to_translate.wordzh_set.add(new_word_pl)


def texts_translations(request, source_language):
    """
    Manage texts translations. Allow selecting texts to edit.
    If exist display available translations.
    :param request: HTTP request
    :param source_language: language to translate texts from
    :return: HTTP response
    """
    return render(request, 'translations/texts_translations.html', {'source_language': source_language})


def texts_translations_service(request):
    """
    Same as texts_translations but handles operations in payload.
    :param request: HTTP request
    :return: HTTP response
    """
    source_language = request.POST['source_language']
    text_to_translate = request.POST['text_to_translate']
    operation = request.POST['operation']
    if operation == 'set_translations':
        return set_text_translations(text_to_translate, source_language,
                                     translations=json.loads(request.POST['translations']))
    elif operation == 'get_matches':
        return get_text_matches(text_to_translate, source_language)
    elif operation == 'get_translations':
        return get_text_translations(text_to_translate, source_language)
    else:
        return HttpResponseBadRequest('Unrecognized request', content_type='application/javascript')


def set_text_translations(source_text, source_language, translations):
    """
    Set translations of the source text in source language to the specified translations
    :param source_text: text to translate
    :param source_language: language of text to translate
    :param translations: translations of the text to translate
    :return:
    """
    business_text_to_translate, _ = BusinessText.objects.get_or_create(text=source_text, language=source_language)
    business_text_to_translate.translations.clear()
    for translation in translations:
        translation_language = Languages.chinese if source_language==Languages.polish else Languages.polish
        business_translation, _ = BusinessText.objects.get_or_create(text=translation, language=translation_language)
        business_text_to_translate.translations.add(business_translation)
    return JsonResponse({})


def get_text_matches(source_text, source_language):
    """
    Get texts that start with the specified source text in specified language
    :param source_text: text that matches should start with
    :param source_language: languages of the matches
    :return:
    """
    matching_business_texts = BusinessText.objects.filter(text__startswith=source_text, language=source_language)
    matching_texts = matching_business_texts[:5].values_list('text', flat=True)
    return JsonResponse({'matches': list(matching_texts)})


def get_text_translations(source_text, source_language):
    """
    Get translations of the specified text in specified language
    :param source_text: text to translate
    :param source_language: language of the text to translate
    :return:
    """
    business_text_to_translate = BusinessText.objects.get(text=source_text, language=source_language)
    translations = list(business_text_to_translate.translations.values('text'))
    return JsonResponse({'translations': translations})



