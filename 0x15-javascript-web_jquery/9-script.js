const URL = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.get(URL, function (data) { $('DIV#hello').text(data.hello); });
