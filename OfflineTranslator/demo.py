from argostranslate import translate

from argostranslate import package
package.install_from_path('translate-en_ru-1_7.argosmodel')


def get_argos_model(source, target):
    lang = f'{source} -> {target}'
    source_lang = [model for model in translate.get_installed_languages() if lang in map(repr, model.translations_from)]
    target_lang = [model for model in translate.get_installed_languages() if lang in map(repr, model.translations_to)]
    
    return source_lang[0].get_translation(target_lang[0])

argos_ru_en = get_argos_model('English', 'Russia')
res = argos_ru_en.translate('Hello world!')
print(res)

