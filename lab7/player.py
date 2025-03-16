import pygame
import os

SONG_END = pygame.USEREVENT + 1
paused = False

pygame.init()
screen = pygame.display.set_mode((900, 300))
done = False
clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.Font(None, 36)
text_color = (0, 0, 0)

_songs = ['01 - Sir Baudelaire.mp3', '02 - Corso.mp3', '03 - Lemonhead.mp3', 
'04 - Wusyaname.mp3', '05 - Lumberjack.mp3', '06 - Hot Wind Blows.mp3', '07 - Massa.mp3', '08 - Runitup.mp3', 
'09 - Manifesto.mp3', '10 - Sweet - I Thought You Wanted To Dance.mp3', '11 - Momma Talk.mp3', 
'12 - Rise!.mp3', '13 - Blessed.mp3', '14 - Juggernaut.mp3', '15 - Wilshire.mp3', '16 - Safari.mp3']

_currently_playing_song = _songs[0]

def draw_text(text):
    screen.fill((255, 255, 255))
    rendered_text = font.render(text, True, text_color)
    text_rect = rendered_text.get_rect(center=(900/2, 300/2))
    screen.blit(rendered_text, text_rect)
    pygame.display.flip()

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
    _currently_playing_song = _songs[0]
    draw_text(f"Now playing: {_currently_playing_song}")
    print(_songs)

def play_previous_song():
    global _songs
    _songs = [_songs[-1]] + _songs[:-1]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
    _currently_playing_song = _songs[0]
    draw_text(f"Now playing: {_currently_playing_song}")
    print(_songs)



def stop_music():
    pygame.mixer.music.stop()
    draw_text("Music stopped")

pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load(_currently_playing_song)
pygame.mixer.music.play()
draw_text(f"Now playing: {_currently_playing_song}")

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if paused:
                        pygame.mixer.music.unpause()
                        draw_text(f"Now playing: {_songs[0]}")
                    else:
                        pygame.mixer.music.pause()
                        draw_text("Pause")
                    paused = not paused

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    play_next_song()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    play_previous_song()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    stop_music()

                if event.type == SONG_END:
                    play_next_song()

        pygame.display.flip()
        clock.tick(60)

pygame.quit()