-- Lists all shows and genres linked to the show from the
-- Records are ordered by ascending show title and genre name.
SELECT show.`title`, genre.`name`
  FROM `tv_shows` AS show
       LEFT JOIN `tv_show_genres` AS show_genre
       ON show.`id` = show_genre.`show_id`

       LEFT JOIN `tv_genres` AS genre
       ON show_genre.`genre_id` = genre.`id`
 ORDER BY show.`title`, genre.`name`;
