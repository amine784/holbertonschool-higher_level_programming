-- cript that lists all shows contained in
-- hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title,tv_show_genres.genre_id FROM tv_shows,tv_shows_genres WHERE tv_show_genres.genres.show_id=tv_shows_id ORDER BY  tv_shows.title,tv_show_genres.genre_id;
