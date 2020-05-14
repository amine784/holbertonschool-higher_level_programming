const URL = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(URL, function (data) {
  data.results.forEach(index => {
    $('UL#list_movies').append('<li>' + index.title + '</li>');
  });
});
