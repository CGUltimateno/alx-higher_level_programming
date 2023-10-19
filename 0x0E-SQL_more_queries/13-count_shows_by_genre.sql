-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT genres.name, COUNT(*) AS 'number_of_shows' FROM `tv_genres` as genres
INNER JOIN `tv_show_genres` as show_genres ON genres.id = show_genres.genre_id
GROUP BY genres.name
ORDER BY number_of_shows DESC;