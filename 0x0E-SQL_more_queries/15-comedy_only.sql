-- Lists all Comedy shows in the database hbtn_0d_tvshows
SELECT show.`title`
    FROM `tv_shows` as show
        INNER JOIN `tv_show_genres` as show_genres
        ON show.`id` = show_genre.`show_id`

        INNER JOIN `tv_genres` as genres
        ON show.`id` = genres.`genre_id`
        WHERE genres.`name` = "Comedy"
ORDER BY show.`title`;
