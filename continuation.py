class InlineTranslation:
    def __init__(self, to_translate, input_from, translated, correct_translation):
        self.to_translate = to_translate
        self.input_from = input_from
        self.translated = translated
        self.correct_translation = correct_translation
        self.line_edit = None

def update_state(state, line_edit):
    if not line_edit:
        return

    for key, translation in state.items():
        if translation.line_edit is line_edit:
            user_input = line_edit.text()
            translation.input_from = user_input
            if user_input.lower() == translation.correct_translation.lower():
                translation.translated = True
                line_edit.setStyleSheet("background-color: lightgreen")
            else:
                translation.translated = False
                line_edit.setStyleSheet("background-color: lightcoral")
            break
