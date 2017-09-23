$('#msg').keypress(function (e) {
  if (e.which == 13) {
    getdata()
    add_out()
    return false;
  }
});

function add_out() {
  $('.messages').append(
    '<p class="out">' + $('#msg').val() + '</p>'
  );
  $('#msg').val('');
}

function add_in(val) {
  $('.messages').append(
    '<p class="in">' + String(val) + '</p>'
  );
}

function getdata() {

  g = '/handler/mock?num=' + $('#num').val() + '&text=' + $('#msg').val()

  console.log(g);

  fe = fetch(g)

  fe.then(x => {
      x.text().then(x => {
        add_in(x);
      })
    })
}
