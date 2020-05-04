from flask import Flask, render_template, request
from songs_analysis import analyze, explicit, searcher
import lyricsgenius
import billboardNYE

# import mbta_helper

app = Flask(__name__)

@app.route("/", methods=["GET"])
def start():
    return render_template("index.html")

@app.route("/songs/", methods=["GET", "POST"])
def songs():
    if request.method == "GET":
        print("good")
    if request.method == "POST":
        checked = []
        boxes = ["Explicit", "SentimentAnalysis"]
        for box in boxes:
            if box in request.form:
                checked.append(box)
        word_to_check = request.form['word']
        to_check_song = []
        to_check_artist = []
        list1Name = request.form['list-1-name']
        list2Name = request.form['list-2-name']
        Artist_col_one_zero = request.form['artist-col-1-0']
        Song_col_one_zero = request.form['song-col-1-0']
        Artist_col_one_one = request.form['artist-col-1-0']
        Song_col_one_one = request.form['song-col-1-1']
        Artist_col_one_two = request.form['artist-col-1-2']
        Song_col_one_two = request.form['song-col-1-2']
        Artist_col_one_three = request.form['artist-col-1-3']
        Song_col_one_three = request.form['song-col-1-3']
        Artist_col_one_four = request.form['artist-col-1-4']
        Song_col_one_four = request.form['song-col-1-4']
        Artist_col_one_five = request.form['artist-col-1-5']
        Song_col_one_five = request.form['song-col-1-5']
        Artist_col_one_six = request.form['artist-col-1-6']
        Song_col_one_six = request.form['song-col-1-6']
        Artist_col_one_seven = request.form['artist-col-1-7']
        Song_col_one_seven = request.form['song-col-1-7']
        Artist_col_one_eight = request.form['artist-col-1-8']
        Song_col_one_eight = request.form['song-col-1-8']
        Artist_col_one_nine = request.form['artist-col-1-9']
        Song_col_one_nine = request.form['song-col-1-9']
        to_check_song.append(Song_col_one_zero)
        to_check_artist.append(Artist_col_one_zero)
        to_check_song.extend([Song_col_one_one, Song_col_one_two, Song_col_one_three, Song_col_one_four, Song_col_one_five, Song_col_one_six, Song_col_one_seven, Song_col_one_eight, Song_col_one_nine])
        to_check_artist.extend([Artist_col_one_one, Artist_col_one_two, Artist_col_one_three, Artist_col_one_four, Artist_col_one_five, Artist_col_one_six, Artist_col_one_seven, Artist_col_one_eight, Artist_col_one_nine])
        senti_result = []
        explicit_song= []
        word_occurences = []
        new_to_check_song = []
        new_to_check_artist = []
        print("lovely")
        for i in range(len(to_check_song)):
            if to_check_song[i] and to_check_artist[i] != "":
                song_name = to_check_song[i] #Alive, Alive, UCLA, UCLA
                artist_name = to_check_artist[i] #Alvie, Alive, RL Grimesss, RL Grimes
                genius = lyricsgenius.Genius("YOUR-GENIUS-ACCESS-KEY-HERE")
                # song_name = song #Alive, Alive, UCLA, UCLA
                # artist_name = artist #Alvie, Alive, RL Grimesss, RL Grimes
                song = genius.search_song(song_name, artist_name)
                new_to_check_song.append(song.title)
                new_to_check_artist.append(song.artist)
                print(new_to_check_song)
                # sentence = song.lyrics
        
        if "SentimentAnalysis" in checked:
            for i in range(len(new_to_check_song)):
                senti_result.append(analyze(song = new_to_check_song[i], artist = new_to_check_artist[i]))
        if "Explicit" in checked:
            for i in range(len(new_to_check_song)):
                explicit_song.append(explicit(song = new_to_check_song[i], artist = new_to_check_artist[i]))
        if word_to_check != "":
            for i in range(len(new_to_check_song)):
                word_occurences.append(searcher(song = new_to_check_song[i], artist= new_to_check_artist[i], word = word_to_check))
        # return render_template('songs-outcome.html', songs=new_to_check_song, artists = new_to_check_artist, sentiment_analysis = senti_result, explicit_songs = explicit_song, checked_word = word_occurences)
        

        to_check_song_two = []
        to_check_artist_two = []
        list1Name = request.form['list-1-name']
        list2Name = request.form['list-2-name']
        Artist_col_two_zero = request.form['artist-col-2-0']
        Song_col_two_zero = request.form['song-col-2-0']
        Artist_col_two_one = request.form['artist-col-2-1']
        Song_col_two_one = request.form['song-col-2-1']
        Artist_col_two_two = request.form['artist-col-2-2']
        Song_col_two_two = request.form['song-col-2-2']
        Artist_col_two_three = request.form['artist-col-2-3']
        Song_col_two_three = request.form['song-col-2-3']
        Artist_col_two_four = request.form['artist-col-2-4']
        Song_col_two_four = request.form['song-col-2-4']
        Artist_col_two_five = request.form['artist-col-2-5']
        Song_col_two_five = request.form['song-col-2-5']
        Artist_col_two_six = request.form['artist-col-2-6']
        Song_col_two_six = request.form['song-col-2-6']
        Artist_col_two_seven = request.form['artist-col-2-7']
        Song_col_two_seven = request.form['song-col-2-7']
        Artist_col_two_eight = request.form['artist-col-2-8']
        Song_col_two_eight = request.form['song-col-2-8']
        Artist_col_two_nine = request.form['artist-col-2-9']
        Song_col_two_nine = request.form['song-col-2-9']
        to_check_song_two.append(Song_col_two_zero)
        to_check_artist_two.append(Artist_col_two_zero)
        to_check_song_two.extend([Song_col_two_one, Song_col_two_two, Song_col_two_three, Song_col_two_four, Song_col_two_five, Song_col_two_six, Song_col_two_seven, Song_col_two_eight, Song_col_two_nine])
        to_check_artist_two.extend([Artist_col_two_one, Artist_col_two_two, Artist_col_two_three, Artist_col_two_four, Artist_col_two_five, Artist_col_two_six, Artist_col_two_seven, Artist_col_two_eight, Artist_col_two_nine])
        senti_result_two = []
        explicit_song_two = []
        word_occurences_two = []
        new_to_check_song_two = []
        new_to_check_artist_two = []
        # print("lovely")
        for i in range(len(to_check_song_two)):
            if to_check_song_two[i] and to_check_artist[i] != "":
                song_name = to_check_song_two[i] #Alive, Alive, UCLA, UCLA
                artist_name = to_check_artist_two[i] #Alvie, Alive, RL Grimesss, RL Grimes
                genius = lyricsgenius.Genius("YOUR-GENIUS-ACCESS-KEY-HERE")
                # song_name = song #Alive, Alive, UCLA, UCLA
                # artist_name = artist #Alvie, Alive, RL Grimesss, RL Grimes
                song = genius.search_song(song_name, artist_name)
                new_to_check_song_two.append(song.title)
                new_to_check_artist_two.append(song.artist)
                print(new_to_check_song_two)
        print(checked)
        if "SentimentAnalysis" in checked:
            for i in range(len(new_to_check_song_two)):
                senti_result_two.append(analyze(song = new_to_check_song_two[i], artist = new_to_check_artist_two[i]))
        if "Explicit" in checked:
            print("test")
            # for i in range(len(new_to_check_song_two)):
            #     explicit_song_two.append(explicit(song = new_to_check_song_two[i], artist = new_to_check_artist_two[i]))
            for i in range(len(new_to_check_song_two)):
                explicit_song_two.append(explicit(song = new_to_check_song_two[i], artist = new_to_check_artist_two[i]))
                print(explicit_song_two)
        if word_to_check != "":
            for i in range(len(new_to_check_song_two)):
                word_occurences_two.append(searcher(song = new_to_check_song_two[i], artist= new_to_check_artist_two[i], word = word_to_check))
        return render_template('songs-outcome.html', list1Name=list1Name, list2Name=list2Name, songs=new_to_check_song, artists = new_to_check_artist, sentiment_analysis = senti_result, explicit_songs = explicit_song, checked_word = word_occurences, songs_two=new_to_check_song_two, artists_two = new_to_check_artist_two, sentiment_analysis_two = senti_result_two, explicit_songs_two = explicit_song_two, checked_word_two = word_occurences_two)
        
    #     list1Name = request.form['list-1-name']
    # return render_template('songs-outcome.html', list1Name=list1Name)
        
    #     idfds = request.form['#1']
    #     if not idfds=="":
    #         find = request.form["songs"]
    #     checked = []
    #     boxes = ["RapidTransit", "ExpressBus-Downtown", "LocalBus"]
    #     for box in boxes:
    #         if box in request.form:
    #             checked.append(box)
    #     if request.method == 'POST':
    #         a = float(request.form['a'])
    #         b = float(request.form['b'])
    #         c = float(request.form['c'])
    #         root_1 = analyze()

            # if root_1:
            #     return render_template('calculator_result.html', a=a, b=b, c=c,
            #                         root_1=root_1, root_2=root_2)
            # else:
            #     return render_template('calculator_form.html', error=True)
    return render_template("song.html")

@app.route("/years/", methods=["GET", "POST"])
def years():
    if request.method == "GET":
        print("good")
    if request.method == "POST":
        year_num = request.form['year']
        results = billboardNYE.YearEnd('hot-100-songs', date=year_num)
        return render_template('years.html', results=results, year_num=year_num)
        # return render_template("years.html", results, year_num)

    return render_template("years.html")

@app.route("/writeup/", methods=["GET"])
def writeup():
    return render_template("writeup.html")

@app.route("/proposal/", methods=["GET"])
def propsal():
    return render_template("propsal.html")

