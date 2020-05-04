import lyricsgenius
from nltk.tokenize import sent_tokenize
import billboardNYE
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from profanity_check import predict, predict_prob


def explicit(song, artist): 
    if song and artist != "":
        genius = lyricsgenius.Genius("YOUR-GENIUS-ACCESS-KEY-HERE")
        song_name = song #Alive, Alive, UCLA, UCLA
        artist_name = artist #Alvie, Alive, RL Grimesss, RL Grimes
        song = genius.search_song(song_name, artist_name)
        sentence = [song.lyrics]
        # predict([sentence])
        # print(predict([sentence]))
        return predict(sentence)[0]


def searcher(song, artist, word): 
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(word)
    if song and artist != "":
        genius = lyricsgenius.Genius("YOUR-GENIUS-ACCESS-KEY-HERE")
        song_name = song #Alive, Alive, UCLA, UCLA
        artist_name = artist #Alvie, Alive, RL Grimesss, RL Grimes
        song = genius.search_song(song_name, artist_name)
        sentence = song.lyrics
        sentence = sentence.replace("[Chorus]", "")
        sentence = sentence.replace("[Verse 1]", "")
        sentence = sentence.replace("[Verse 2]", "")
        sentence = sentence.replace("[Bridge]", "")
        sentence = sentence.replace("[Pre-Chorus]", "")
        sentence = sentence.replace("[Pre Chorus]", "")
        sentence = sentence.replace("[Outro]", "")
        print(word)
        # def count_occurences(s,word): #https://stackoverflow.com/questions/8272358/how-do-i-calculate-the-number-of-times-a-word-occurs-in-a-sentence
        # str = 'Hello World. Hello TutorialKart.'
        
        #substring
        # substr = 'Hello'
        
        #finding number of occurrences of substring in given string
        count = sentence.count(word)
        return count
    
    # print("Number of occurrences of substring :", count)
    # return count

    # return count_occurences(sentence,word)


def analyze(song, artist):
    # songs = dict()
    # songs["list1"] = []
    # songs["list1"].append([1,2,3])
    # songs["list1"].append([4,5,6])
    # songs["list2"] = []
    # songs["second"].append([7,8,9])

    # for key, value in d.items():
    if song and artist != "":
        genius = lyricsgenius.Genius("YOUR-GENIUS-ACCESS-KEY-HERE")
        song_name = song #Alive, Alive, UCLA, UCLA
        artist_name = artist #Alvie, Alive, RL Grimesss, RL Grimes
        song = genius.search_song(song_name, artist_name)
        sentence = song.lyrics
        sentence = sentence.replace("[Chorus]", "")
        sentence = sentence.replace("[Verse 1]", "")
        sentence = sentence.replace("[Verse 2]", "")
        sentence = sentence.replace("[Bridge]", "")
        sentence = sentence.replace("[Pre-Chorus]", "")
        sentence = sentence.replace("[Pre Chorus]", "")
        sentence = sentence.replace("[Outro]", "")

        analyzer = SentimentIntensityAnalyzer()

        vs = analyzer.polarity_scores(sentence)
        # print("Vader \n\n\n\n\n")

        sentences = sent_tokenize(sentence)
        for sentence in sentences:
            vs = analyzer.polarity_scores(sentence)
            # print("{:-<65} {}".format(sentence, str(vs)))
        return vs