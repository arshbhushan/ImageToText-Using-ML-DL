from deep_translator import GoogleTranslator
import deep_translator
def translate_text(input_text, target_language='hi'):
    print(deep_translator.__version__)
    def translate_chunk(chunk):
        """Wrapper for Google Translate with character limit workaround."""
        translate = GoogleTranslator(source='auto', target=target_language).translate
        translated_text = ''
        source_text_chunk = ''
        for sentence in chunk.split('. '):
            if len(sentence.encode('utf-8')) + len(source_text_chunk.encode('utf-8')) < 5000:
                source_text_chunk += '. ' + sentence
            else:
                translated_text += ' ' + translate(source_text_chunk)
                if len(sentence.encode('utf-8')) < 5000:
                    source_text_chunk = sentence
                else:
                    message = '<<Omitted Word longer than 5000 bytes>>'
                    translated_text += ' ' + translate(message)
                    source_text_chunk = ''
        if translate(source_text_chunk) is not None:
            translated_text += ' ' + translate(source_text_chunk)
        return translated_text

    try:
        # Translate the input text
        translated_text = translate_chunk(input_text)

        # Return the translated text
        return translated_text
    except Exception as e:
        return str(e)

# Example usage:
# input_text = "This is a sample text. It can be longer and contain multiple sentences."
# translated_text = translate_text(input_text)
