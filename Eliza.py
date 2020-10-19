"""
Shane Driskell
Create Eliza: A Primitive Chat Bot
"""

import random


# SETUP OF LISTS/DICTS FOR KEYWORDS AND RESPONSES
goodbye_list = ["goodbye", "bye", "farewell", "later", "adios"]

keywords = ["can you", "can i", "you are", "youre", "i dont", "i feel", "why dont you", "why cant i",
            "are you", "i cant", "i am", "im ", "you ", "i want", "what", "how", "who", "where", "when",
            "why", "name", "cause", "sorry", "dream", "hello", "hi ", "maybe", "no", "your", "always",
            "think", "alike", "yes", "friend", "computer"]

special_chars = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

conjugate_dict = {"are":"am", "am":"are", "were":"was", "was":"were", "you":"i", "i":"you", "your":"my",
                  "my":"your", "ive":"you've", "youve":"ive", "im":"you're", "youre":"I'm", "me":"you"}

response_dict = {
        -1: ["What does that suggest to you?", "I see.", "I'm not sure I understand you fully.",
             "Come, come, elucidate your thoughts.", "Can you elaborate on that?",
             "That is quite interesting."],
        0: ["Don't you believe that I can *", "Perhaps you would like me to be able to *",
            "You want me to be able to *"],
        1: ["Perhaps you don't want to *", "Do you want to be able to *"],
        2: ["What makes you think I am *", "Does it please you to believe I am *",
            "Perhaps you would like to be *", "Do you sometimes wish you were *"],
        3: ["What makes you think I am *", "Does it please you to believe I am *",
            "Perhaps you would like to be *", "Do you sometimes wish you were *"],
        4: ["Don't you really *", "Why don't you *", "Do you wish to be able to *",
            "Does that trouble you?"],
        5: ["Tell me more about such feelings.", "Do you often feel *", "Do you enjoy feeling *"],
        6: ["Do you really believe I don't *", "Perhaps in good time I will *", "Do you want me to *"],
        7: ["Do you think you should be able to *", "Why can't you *"],
        8: ["Why are you interested in whether or not I am *", "Would you prefer if I were not *",
            "Perhaps in your fantasies I am *"],
        9: ["How do you know you can't *", "Have you tried?", "Perhaps you can now *"],
        10: ["Did you come to me because you are *", "How long have you been *",
             "Do you believe it is normal to be *", "Do you enjoy being *"],
        11: ["Did you come to me because you are *", "How long have you been *",
             "Do you believe it is normal to be *", "Do you enjoy being *"],
        12: ["We were discussing you, not me.", "Oh, I *", "You're not really talking about me, are you?"],
        13: ["What would it mean to you if you got *", "Why do you want *", "Suppose you got *",
             "What if you never got *", "I sometimes also want *"],
        14: ["Why do you ask?", "Does that question interest you?",
             "What answer would please you the most?", "What do you think?",
             "Are such questions on your mind often?", "What is it that you really want to know?",
             "Have you asked anyone else?", "Have you asked such questions before?",
             "What else comes to your mind when you ask that?"],
        15: ["Why do you ask?", "Does that question interest you?",
             "What answer would please you the most?", "What do you think?",
             "Are such questions on your mind often?", "What is it that you really want to know?",
             "Have you asked anyone else?", "Have you asked such questions before?",
             "What else comes to your mind when you ask that?"],
        16: ["Why do you ask?", "Does that question interest you?", "What answer would please you the most?",
             "What do you think?", "Are such questions on your mind often?",
             "What is it that you really want to know?", "Have you asked anyone else?",
             "Have you asked such questions before?", "What else comes to your mind when you ask that?"],
        17: ["Why do you ask?", "Does that question interest you?", "What answer would please you the most?",
             "What do you think?", "Are such questions on your mind often?",
             "What is it that you really want to know?", "Have you asked anyone else?",
             "Have you asked such questions before?", "What else comes to your mind when you ask that?"],
        18: ["Why do you ask?", "Does that question interest you?", "What answer would please you the most?",
             "What do you think?", "Are such questions on your mind often?",
             "What is it that you really want to know?", "Have you asked anyone else?",
             "Have you asked such questions before?", "What else comes to your mind when you ask that?"],
        19: ["Why do you ask?", "Does that question interest you?", "What answer would please you the most?",
             "What do you think?", "Are such questions on your mind often?",
             "What is it that you really want to know?", "Have you asked anyone else?",
             "Have you asked such questions before?", "What else comes to your mind when you ask that?"],
        20:	["Names don't interest me.", "I don't care about names.  Please go on."],
        21: ["Is that the real reason?", "Don't any other reasons come to mind?",
             "Does that reason explain anything else?", "What other reasons might there be?"],
        22:	["Please don't apologize!" ,"Apologies are not necessary."],
        23: ["What does that dream suggest to you?", "Do you dream often?",
             "What persons appear in your dreams?", "Are you disturbed by your dreams?"],
        24: ["How do you do.  Please state your problem."],
        25: ["How do you do.  Please state your problem."],
        26: [ "You don't seem quite certain.", "Why the uncertain tone?", "Can't you be more positive?",
              "You aren't sure?", "Don't you know?"],
        27: ["Are you saying no just to be negative?", "You are being a bit negative.", "Why not?",
             "Are you sure?", "Why no?"],
        28:	["Why are you concerned about my *" ,"What about your own *"],
        29:	["Can you think of a specific example?" ,"When?" ,"What are you thinking of?" ,"Really, always?"],
        30: ["Do you really think so?" ,"But you are not sure you *" ,"Do you doubt *"],
        31: ["In what way?", "What resemblence do you see?", "What does the similarity suggest to you?",
             "What other connections do you see?", "Could there really be some connection?", "How?"],
        32:	["You seem quite positive.", "Are you sure?", "I see.", "I understand."],
        33: ["Why do you bring up the topic of friends?", "Do your friends worry you?",
             "Do your friends pick on you?", "Are you sure you have any friends?",
             "Do you impose on your friends?", "Perhaps your love for your friends worries you."],
        34: ["Do computers worry you?", "Are you frightened by machines?", "Why do you mention computers?",
             "What do you think machines have to do with your problem?",
             "Don't you think computers can help people?", "What is it about machines that worries you?"]
    }


def preprocess(user_input):
    """Remove special characters from input"""
    preprocess_input = ""
    for char in user_input:
        if char not in special_chars:
            preprocess_input = preprocess_input + char
    return preprocess_input
    # https://pythonguides.com/remove-character-from-string-python/


def conjugate(user_input):
    """Conjugate from 1st to 2nd person or vice versa"""
    user_input = user_input.split()
    index_number = 0
    results_list = []

    for word in user_input:
        if conjugate_dict.get(word) != None:
            results_list.append(conjugate_dict.get(word))
        else:
            results_list.append(word)
    return " ".join(results_list)


def keyword(user_input):
    """Identify keyword and remove it and left-hand text from input"""
    for key in keywords:
        if key in user_input:
            keyword_index = keywords.index(key)
            start = user_input.find(key)
            end = start + len(key)
            results = str(keyword_index) + " " + user_input[end:]
            return results

    index_number = -1
    return str(index_number) + " " + " ".join(user_input)
    # Thanks to my friend snowk11235 @github for helping me with this


def get_reply(user_input):
    """Generate the response back to user."""
    keyword_index = user_input.split()[0]
    reply_list = []

    reply_list = response_dict.get(int(keyword_index))
    random_reply = random.randint(0, len(reply_list))
    reply = reply_list[random_reply]

    return reply


def build_reply():
    """Build a reply that takes get_reply results and provides a response to user"""
    pass


def eliza():
    """Run process to simulate a simple chat bot"""
    still_going = True
    print("Good day to you.")

    while still_going:
        # preprocessed_input = preprocess(input(">").lower())
        preprocessed_input = preprocess("I am sorry that you're wonderful to my eyes.".lower())

        for bye in goodbye_list:
            if bye == preprocessed_input:
                still_going = False

        keyword_input = keyword(preprocessed_input)
        conjugated_input = conjugate(keyword_input)
        reply = get_reply(conjugated_input)

        # REMOVE WHEN DONE TESTING
        still_going = False
    print("Goodbye, jerk-face.")


if __name__ == "__main__":
    eliza()
