import lyricsgenius
from profanity_check import predict, predict_prob


genius = lyricsgenius.Genius("YOUR-GENIUS-ACCESS-KEY-HERE")
song_name = "Alive" #Alive, Alive, UCLA, UCLA
artist_name = "Alvie" #Alvie, Alive, RL Grimesss, RL Grimes
song = genius.search_song(song_name, artist_name)
# print(song.artist)
# print(song.title)
# print(song.lyrics)
sentence = song.lyrics
sentence = sentence.replace("[Chorus]", "")
sentence = sentence.replace("[Verse 1]", "")
sentence = sentence.replace("[Verse 2]", "")
sentence = sentence.replace("[Bridge]", "")
sentence = sentence.replace("[Pre-Chorus]", "")

genius = lyricsgenius.Genius("YOUR-GENIUS-ACCESS-KEY-HERE")
song_name = "Running Out of Love" #Alive, Alive, UCLA, UCLA
artist_name = "Yung Bleu" #Alvie, Alive, RL Grimesss, RL Grimes
song = genius.search_song(song_name, artist_name)
sentence = song.lyrics
predict([sentence])
print(predict([sentence]))
# return [predict(sentence), song.title, artist.title]

# print(song.title)
# print(song.artist)


import billboardNYE
# chart = billboardNYE.ChartData('hot-100')
# print(chart.title)
# print(billboardNYE.charts())

# print(billboardYE.ChartData("ye2002", date="2017-12-31", fextch=True, timeout=25))
# print(billboard.YearEnd)



# print(billboardNYE.YearEnd('hot-100-songs', date='2006'))




# chart = billboardYE.YearEnd('hot-100-songs', date='2006')

# print(billboardYE.YearEnd('hot-100-songs'))


# chart = billboard.ChartData('hot-100')
# while chart.previousDate:
#     doSomething(chart)
#     chart = billboard.ChartData('hot-100', 2017)

# import analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# from textblob import TextBlob
analyzer = SentimentIntensityAnalyzer()
# sentence_p = "THis is a very positive sentence"
# sentence_n = "THis is a very negative sentence. THis is a very positive sentence"
# testimonial = TextBlob(sentence_n)
# print(testimonial.sentiment)
# print(testimonial.sentiment.polarity)
vs = analyzer.polarity_scores(sentence)
# print("Vader \n\n\n\n\n")
# # print("{:-<65} \n{}".format(sentence_n, str(vs)))
# from nltk.tokenize import sent_tokenize
# # sentence = "As the most quoted English writer Shakespeare has more than his share of famous quotes.  Some Shakespare famous quotes are known for their beauty, some for their everyday truths and some for their wisdom. We often talk about Shakespeare’s quotes as things the wise Bard is saying to us but, we should remember that some of his wisest words are spoken by his biggest fools. For example, both ‘neither a borrower nor a lender be,’ and ‘to thine own self be true’ are from the foolish, garrulous and quite disreputable Polonius in Hamlet."

# sentences = sent_tokenize(sentence)
# for sentence in sentences:
#     vs = analyzer.polarity_scores(sentence)
#     print("{:-<65} {}".format(sentence, str(vs)))