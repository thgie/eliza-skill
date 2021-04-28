from mycroft import MycroftSkill, intent_file_handler


class Eliza(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('eliza.intent')
    def handle_eliza(self, message):
        self.speak_dialog('eliza')


def create_skill():
    return Eliza()

