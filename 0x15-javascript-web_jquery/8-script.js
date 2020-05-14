const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, (data) => {
  for (let x = 0; x < data.results.length; x++) {
    $('UL#list_movies').append('<li>' + data.results[x].title + '</li>');
  }
});
