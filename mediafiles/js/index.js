function onFavorite(id_unsplash = '', preview = '') {
  console.log(id_unsplash, preview);
  fetch('/favorite/add/', {
    method: 'POST',
    body: JSON.stringify({ id_unsplash, preview, favorite: true }),
  }).then(
      $('img[id="' + id_unsplash + '"]').attr('src', '/static/img/star_1.png')
  );
}

function onUnfavorite(id_unsplash = '') {
    fetch('/favorite/add/', {
      method: 'POST',
      body: JSON.stringify({ id_unsplash, preview: '', favorite: false }),
    }).then(
        $('img[id="' + id_unsplash + '"]').attr('src', '/static/img/star_2.png')
    );
  }
