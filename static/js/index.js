function onFavorite(id_unsplash = '', preview = '') {
  fetch('/favorite/add/', {
    method: 'POST',
    body: JSON.stringify({ id_unsplash, preview, favorite: true }),
  }).then((res) => {
    res.json().then((data) => {
      if (data.status === 200) {
        $('img[id="' + id_unsplash + '"]').attr('src', '/static/img/star_1.png');
        $('img[id="' + id_unsplash + '"]').attr(
          'onclick',
          'onUnfavorite("' + id_unsplash + '", "' + preview + '")'
        );
        showMessage('Marked as favorite');
      } else {
        showMessage('Failed, action not success');
      }
    });
  });
}

function onUnfavorite(id_unsplash = '', preview = '') {
  fetch('/favorite/add/', {
    method: 'POST',
    body: JSON.stringify({ id_unsplash, preview: '', favorite: false }),
  }).then((res) => {
    res.json().then((data) => {
      if (data.status === 200) {
        $('img[id="' + id_unsplash + '"]').attr('src', '/static/img/star_2.png');
        $('img[id="' + id_unsplash + '"]').attr(
          'onclick',
          'onFavorite("' + id_unsplash + '", "' + preview + '")'
        );
        showMessage('Unmarked as favorite');
      } else {
        showMessage('Failed, action not success');
      }
    });
  });
}

function showMessage(message = '') {
  $('#message').text(message);
  $('#message').removeClass('hidden');
  setTimeout(() => {
    $('#message').addClass('hidden');
  }, 2000);
}
