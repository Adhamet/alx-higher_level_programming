-- Lists all genres of the show Dexter.
SELECT tvG.`name`
    FROM `tv_genres` as tvG
        INNER JOIN `tv_show_genres`
        ON tvG.`id` = `tv_show_genres`.`id`

        INNER JOIN `tv_shows`
        ON tvG.`id` = `tv_shows`.`show_id`
        WHERE `tv_shows`.`title` = "Dexter"
ORDER BY tvG.`name`;
