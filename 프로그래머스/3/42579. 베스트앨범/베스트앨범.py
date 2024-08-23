from collections import defaultdict

def solution(genres, plays):
    genre_play_count = defaultdict(int) 
    songs_by_genre = defaultdict(list)  
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_play_count[genre] += play  
        songs_by_genre[genre].append((play, i))  
    
    sorted_genres = sorted(genre_play_count.keys(), key=lambda g: genre_play_count[g], reverse=True)
    
    answer = []
    
    for genre in sorted_genres:
        sorted_songs = sorted(songs_by_genre[genre], key=lambda x: (-x[0], x[1]))
        answer.extend([song[1] for song in sorted_songs[:2]])
    
    return answer