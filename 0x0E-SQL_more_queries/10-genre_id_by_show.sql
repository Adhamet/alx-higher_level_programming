-- Lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked.
SELECT show.`title`, genre.`genre_id`
    FROM `tv_shows` AS show
        INNER JOIN `tv_shows_genre` AS genre
        ON show.`id` = genre.`id`
ORDER BY show.`title`, genre.`genre_id`;
