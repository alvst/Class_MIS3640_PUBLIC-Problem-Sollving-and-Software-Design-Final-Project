from profanity_check import predict, predict_prob
import lyricsgenius

def search(song, artist, word): 
    genius = lyricsgenius.Genius("YOUR-GENIUS-ACCESS-KEY-HERE")
    song_name = song #Alive, Alive, UCLA, UCLA
    artist_name = artist #Alvie, Alive, RL Grimesss, RL Grimes
    song = genius.search_song(song_name, artist_name)
    sentence = song.lyrics
    def count_occurences(s,word): #https://stackoverflow.com/questions/8272358/how-do-i-calculate-the-number-of-times-a-word-occurs-in-a-sentence
        count = 0
        for i in range(len(s)): 
            if s[i:i+len(word)] == word:
                count += 1    
        return count

    return count_occurences(sentence,word)


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
    

print(explicit("Running out of love", "Yung Bleu"))