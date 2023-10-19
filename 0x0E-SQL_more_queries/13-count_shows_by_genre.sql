-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT g.name as `genre`, COUNT(*) AS 'number_of_shows' FROM `tv_genres` as g
INNER JOIN `tv_show_genres` as show_genres ON g.id = show_genres.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;