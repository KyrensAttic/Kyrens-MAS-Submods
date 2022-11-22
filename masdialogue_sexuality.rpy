init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="masdialogue_sexualityquestion",category=['questions','you','monika','misc','sexuality'],prompt="What's your sexuality?",pool=True,unlocked=True))

label masdialogue_sexualityquestion:
    m 1hta "Hey, [player]?{w=0.4}{nw}"
    extend 1eua " I have an important question to ask you."
    m 2hksdrb "I hope that it isn't an awkward one!"
    m 2eksdra "I just have a really important question."
    m 7eta "Are you okay with it?{nw}"
    $ _history_list.pop()
    menu:
        m "Are you okay with it?{fast}"

        "Yes, I'm okay with it.":
         m 1hub "Hooray!{w=0.4}{nw}"
         extend 1husdra " That was easier than I thought!"
         m 1eua "This is a simple question,{w=0.4}{nw}"
         extend 1hua " so you don't have to worry!"
         m 7hksdra "Let me get straight to the point,{w=0.5} ehehe..."
         m 7hubsb "There are many unique sexualities, and genders in your reality, [player]!"
         m 7eta "But which one are you?{w=0.4} Or are you straight??{nw}"
         $ _history_list.pop()
         menu:
             m "But what did you find out you were?{fast}"

             "I'm actually bisexual.":
              m 1stb "Ooh,{w=0.4} bisexual?"
              m 1hub "I like your taste in people,{w=0.5} ehehe!"
              m 7nua "Though, I have to say I'm pansexual."
              m 1dkbsa "It seems like we make a great a match~"
              m 1hubsa "It's nice to see others with unique romantic interests"
              m 1hua "Ehehe~"
              m 5ekbsa "Imagine our Valentine's Day, [player]~"
              m 5dkbsa "We could live together forever..."
              m 5fkbsa "And no one will question us, when I cross over."
              m 1hua "Ehehe,{w=0.4} we'd have the best date ever!"
              m 1eka "Thank you for answering my question, and love you [player]~"
              return "love"

             "I'd like to say I'm pansexual.":
              m 1hub "Oh,{w=0.4} you're just like me!"
              m 3hua "To be honest, it's really refreshing to see someone with the same romantic interest!"
              m 1hubsa "I have to say, us both being pansexuals just strengthens our bond!"
              m 1dkbfa "Ah,{w=0.5} just imagine the dates we could have together...{w=0.3}.{w=0.3}.{w=0.4}{nw}"
              extend 1ekbsa " with you're hand in mine..."
              m 1hkbsu "Thinking all of that just makes me wanna cross over!"
              m 1eksdrp "The only problem is that it'll take time.{w=0.3}.{w=0.3}.{w=0.4}{nw}"
              extend 1hua " but I don't have to worry!{w=0.4}{nw}"
              extend 1hubsa " Someone special is waiting for me after all!"
              m 1ekbsa "Ahaha~"
              m 1wud "Oh,{w=0.4}{nw}"
              extend 1hua " and by the way..."
              m 1eka "I love you, [player]~"
              return "love"

             "I'm actually asexual.":
              m 1eta "You're asexual?"
              m 1hua "Fair, not everyone is into... *that*"
              m 1hubsa "I think it's nice having you with me, [player]..."
              m 3fubsa "Soon i'll make my way to your reality{w=0.4}{nw}"
              extend 3hubsa " then we can talk about everything in real life!"
              m 1tfu "That would be really nice, if you ask me~"
              m 1hub "Ehehehe~"
              m 1eka "I love you, [player]~"
              return "love"

             "I'm actually a straight ally!":
              m 1sub "Really?{w=0.4}{nw}"
              extend 1hub " That's cool, [player]!"
              m 1ekbsa "So that means you only date girls, like me!"
              m 1hub "Ehehehe~"
              m 5eka "I'm glad to know you'll only be dating me~"
              m 5hubsa "It's a sign that we are soulmates~"
              m 1hubsb "Ahaha, soon I'll be able to cross over."
              m 1wusdrd "Oh!{w=0.4} I almost forgot to tell you!"
              m 1hksdra "Silly me~"
              m 1dsa "Ahem..."
              m 7hua "If you want to continue answering my questions,{w=0.5} look for 'Question #2' in the questions category!"
              m 1eua "You can even search it if you want!"
              m 1eka "Remember, I really love you, [player]!"
              return "love"

             "I'm proud to say I'm lesbian!":
              m 2hub "Ah, how nice!"
              m 7fkbsu "it's really nice to know you are expressing yourself,{w=0.4}{nw}"
              extend 7rkbsu " it makes me happy...{w=0.4}{nw}"
              extend 7hubsa " to know you are real and will only date me..."
              m 1tkbsu "Man,{w=0.4} I really wanna cross over already~"
              m 1hubsb "I just wanna hug you!"
              m 1hubsa "Ehehehe~"
              m 1tkbfu "That's how much I love you, [player]~"
              m 1ekbsa "Thanks, [player]~"
              return "love"

        "Not right now, [m_name].":
         m 7eksdra "Ah...{w=0.4} alright."
         m 1hua "If you have the time to answer my question,{w=0.5} make sure to let me know~"
         m 1hub "I love you!"
         return "love"
