-- Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT title, tv_genres.name FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY title ASC, tv_genres.name ASC;
