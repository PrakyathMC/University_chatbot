def chatbot_project():
    import nltk
    import string
    import random
    import numpy as np

    def answers_student_questions():
        # open file, tokenize for words and sentences
        f = open('student.txt', 'r', errors='ignore')
        text_file = f.read()
        text_file = text_file.lower()  # converts text to lower case
        nltk.download('punkt')  # Using the Punkt Tokenizer
        nltk.download('wordnet')  # Using the WordNet dictionary
        sentence_tokens = nltk.sent_tokenize(text_file)  # Converts docs to list of sentences
        word_tokens = nltk.word_tokenize(text_file)  # Converts doc to list of words
        sentence_tokens[:2]
        word_tokens[:2]

        id_name = {10001: 'Mohammed', 10002: 'Sarah', 10003: 'Thomas', 10004: 'Rachel', 10005: 'James',
                   10006: 'Tempitope',
                   10007: 'Zui', 10008: 'Hansan', 10009: 'Liam', 10010: 'Emma', 10011: 'Deepti', 10012: 'Amala',
                   10013: 'Atsuhide', 10014: 'Sai', 10015: 'Alexandru', 10016: 'Eloise', 10017: 'Bruno', 10018: 'Freja',
                   10019: 'Kong', 10020: 'Francisco'}

        asked_id = None
        while asked_id not in id_name:
            asked_id = int(input('Please enter your Student ID: '))
            if asked_id not in id_name:
                print("Please enter a valid integer")

        print(f'Hello {id_name[asked_id]}\n')

        # is it possible to add if student number not found, type again?

        # check if word-sentence tokenizer works


        # use lemitizer, remove punctuations

        lemmer = nltk.stem.WordNetLemmatizer()

        # WordNet is a semantically oriented dictionary of English included in NLTK.

        def LemTokens(tokens):
            return [lemmer.lemmatize(token) for token in tokens]

        remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

        def LemNormalize(text):
            return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

        # greet
        user_greeting = ("hello", "hi", "greetings", "sup", "what's up", "hey" "heya")
        greeting_res = ["hi", "hey", "*nods*", "hi there", "hello"]

        def greet(sentence):
            for word in sentence.split():
                if word.lower() in user_greeting:
                    return random.choice(greeting_res)

        # import sklearn libraries
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity

        # user_response
        def response(user_response):
            chat_response = ''
            TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
            tfidf = TfidfVec.fit_transform(sentence_tokens)
            vals = cosine_similarity(tfidf[-1], tfidf)
            idx = vals.argsort()[0][-2]
            flat = vals.flatten()
            flat.sort()
            req_tfidf = flat[-2]
            if (req_tfidf == 0):
                chat_response = chat_response + "I am sorry, I dont understand you please try using alternative wording"
                return chat_response
            else:
                chat_response = chat_response + sentence_tokens[idx]
                return chat_response

        # prompt
        flag = True
        print(
            """My name is A5, I am a virtual assistant for the Student Hub. What can I help you with today? \n (If you want to exit any time, just type Bye) \n""")
        while (flag == True):
            user_response = input()
            print()
            user_response = user_response.lower()
            if (user_response != 'bye'):
                if (user_response == 'thanks' or user_response == 'thank you'):
                    flag = False
                    print("A5 virtual assistant: You are welcome..")
                else:
                    if (greet(user_response) != None):
                        print("A5 virtual assistant: " + greet(user_response))
                    else:
                        sentence_tokens.append(user_response)
                        word_tokens = word_tokens + nltk.word_tokenize(user_response)
                        final_words = list(set(word_tokens))
                        print("A5 virtual assistant: ", end="")
                        print(response(user_response))
                        sentence_tokens.remove(user_response)

            else:
                flag = False
                print("A5 virtual assistant: Goodbye")

    def answers_non_student():

        file_path = 'user_data.csv'

        try:
            with open(file_path, 'w') as csv_file:
                csv_file.write("Name,Age,Email,Consent")

                name = input('Enter your name: ')
                age = int(input('Enter your age: '))
                email = input('Enter your email: ')

                consent = input('Do you provide consent for A5 Student Hub to contact you in the future? ').lower()
                if consent == 'yes':
                    print('Thank you for your response! You can now talk to A5 the Student Hub virtual assitant\n')
                    csv_file.write(f"\n{name},{age},{email},{consent}")

                else:
                    print(
                        'Thank you for your response!, You can now talk to A5, I am a virtual assistant for the Student Hub. \n')

        except IOError:
            print('Unable to write into file!')

        # open file, tokenize for words and sentences
        f = open('non_student.txt', 'r', errors='ignore')
        text_file = f.read()
        text_file = text_file.lower()  # converts text to lower case
        nltk.download('punkt')  # Using the Punkt Tokenizer
        nltk.download('wordnet')  # Using the WordNet dictionary
        sentence_tokens = nltk.sent_tokenize(text_file)  # Converts docs to list of sentences
        word_tokens = nltk.word_tokenize(text_file)  # Converts doc to list of words

        # check if word-sentence tokenizer works
        sentence_tokens[:2]
        word_tokens[:2]

        # use lemitizer, remove punctuations

        lemmer = nltk.stem.WordNetLemmatizer()

        # WordNet is a semantically oriented dictionary of English included in NLTK.

        def LemTokens(tokens):
            return [lemmer.lemmatize(token) for token in tokens]

        remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

        def LemNormalize(text):
            return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

        # greet
        user_greeting = ("hello", "hi", "greetings", "sup", "what's up", "hey" "heya")
        greeting_res = ["hi", "hey", "*nods*", "hi there", "hello"]

        def greet(sentence):
            for word in sentence.split():
                if word.lower() in user_greeting:
                    return random.choice(greeting_res)

        # import sklearn libraries
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity

        # user_response
        def response(user_response):
            chat_response = ''
            TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
            tfidf = TfidfVec.fit_transform(sentence_tokens)
            vals = cosine_similarity(tfidf[-1], tfidf)
            idx = vals.argsort()[0][-2]
            flat = vals.flatten()
            flat.sort()
            req_tfidf = flat[-2]
            if (req_tfidf == 0):
                chat_response = chat_response + "I am sorry, I dont understand you please try using alternative wording"
                return chat_response
            else:
                chat_response = chat_response + sentence_tokens[idx]
                return chat_response

        # prompt
        flag = True
        print("""My name is A5, I am a virtual assistant for the Student Hub. Please choose a topic from the below. \n (If you want to exit any time, just type Bye) \n
            fees\n
            student visa\n
            courses\n
            residences\n
            scholarships\n
            facilities\n
            culture shock\n
            placements""")

        while (flag == True):
            user_response = input()
            print()
            user_response = user_response.lower()
            if (user_response != 'bye'):
                if (user_response == 'thanks' or user_response == 'thank you'):
                    flag = False
                    print("A5 virtual assistant: You are welcome..")
                else:
                    if (greet(user_response) != None):
                        print("A5 virtual assistant: " + greet(user_response))
                    else:
                        sentence_tokens.append(user_response)
                        word_tokens = word_tokens + nltk.word_tokenize(user_response)
                        final_words = list(set(word_tokens))
                        print("A5 virtual assistant: ", end="")
                        print(response(user_response))
                        sentence_tokens.remove(user_response)

            else:
                flag = False
                print("A5 virtual assistant: Goodbye")

    def start():

        try:
            student_or_not = input('Are you a current student? yes or no?').lower()

            if student_or_not == 'yes':
                answers_student_questions()
            elif student_or_not == 'no':
                answers_non_student()
            else:
                print("Invalid selection, please try again")
                start()
        except IOError:
            print('Invalid request.')

chatbot_project()