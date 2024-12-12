#Question 1
"""class PasswordValidator:
    def __init__(self, password):
        self.password = password

    def validate(self):
        if self.password[0].isupper():
                upp=0
                low=0
                dig=0
                spe=0
                spa=0
                for i in self.password:
                    if i.isupper():
                        upp+=1
                    elif i.islower():
                        low+=1
                    elif i.isdigit():
                        dig+=1
                    elif i.isspace():
                        spa+=1
                    else:
                        spe+=1
                if len(self.password)>8 and upp>=1 and low>=1 and dig>=1 and spe>=1:
                    print("Valid password")
                else:
                    print("Invalid password")
        else:
                print("First letter should be capital")
                
user_password = input("Enter your password: ")
validator = PasswordValidator(user_password)
validator.validate()"""

#Question 2
class TextProcessor:
    def __init__(self, text):
        self.text = text

    def split_into_sentences(self):
        return self.text.split('. ')

    def process_sentences(self):
        sentences = self.split_into_sentences()
        for sentence in sentences:
            sentence = sentence.strip()
            if sentence:
                word_count = len(sentence.split())
                print(f"Sentence: \"{sentence}\", Word Count: {word_count}")


text_input = "Hello! How are you? I am fine. Let's learn NLP."
processor = TextProcessor(text_input)


print("Processed Sentence Data:")
processor.process_sentences()


