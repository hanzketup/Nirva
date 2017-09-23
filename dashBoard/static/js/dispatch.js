$('#ofr-msg') //Counter for message box
  .bind('input propertychange',
    function countmsg() {
      console.log(this)
      $('#ofr-msg-legend span').text(160 - this.value.length)
      if (this.value.length > 160) {
        $('#ofr-msg-legend span').css('color', 'red')
      } else {
        $('#ofr-msg-legend span').css('color', '#333')
      }
    });

    var users = new Set();

    $('.filter input') //When filter attributes changes
      .bind('input propertychange', function() {

        $('.selector-item').toArray().forEach(function(item) {

          let exitem = extract_data(item);
          let filter = get_filter();
          let comp = filter_compare(exitem, filter);

          if (comp == false) {
            $(item).addClass('hidden');
          } else {
            $(item).removeClass('hidden');
          }

        });
      });


    $('.selector-check').click(function() { //Add/remove item to users array when checkbox is clicked

      if (this.checked) {
        users.add($(this).data('pk'));
      } else {
        users.delete($(this).data('pk'));
      }
      console.log(users);
      update_counter();
    });

    $('#checkall').click(function() { //Check all visable elements adn add to users
      $('.selector-item')
        .toArray()
        .forEach(function(item) {
          if ($(item).hasClass('hidden') == false) {
            if ($('#checkall').prop('checked')) {
              users.add($(item).data('pk'));
              $(item).find('.selector-check').prop('checked', true);
            } else {
              users.delete($(item).data('pk'));
              $(item).find('.selector-check').prop('checked', false);
            }
          }
        });
      console.log(users);
      update_counter();
    });


    function search(filter, string) { //search for pattern in string and return boolean

      stringre = ('/' + string + '/g')
      sr = stringre.search(filter)

      if (sr > 0) {
        return true
      }
      if (sr === -1) {
        return false
      } else {
        return false
      }
    }

    function extract_data(item) { //get data from html node data- attributes
      item = $(item);
      return {
        "name": item.data('name'),
        "village": item.data('village'),
        "district": item.data('district'),
        "region": item.data('region'),
        "lang": item.data('lang'),
        "inter": item.data('interests'),
      };
    }

    function get_filter() { //get filter data from the filter header
      return {
        "name": $('#Name').val(),
        "village": $('#Village').val(),
        "district": $('#District').val(),
        "region": $('#Region').val(),
        "lang": $('#Language').val(),
        "inter": $('#Interests').val(),
      };
    }

    function filter_compare(item, filter) { //compare the filter and the item and return a boolean

      let name = search(filter.name, item.name) || filter.name === ""
      let village = search(filter.village, item.village) || filter.village === ""
      let district = search(filter.district, item.district) || filter.district === ""
      let region = search(filter.region, item.region) || filter.region === ""
      let lang = search(filter.lang, item.lang) || filter.lang === ""
      let inter = search(filter.inter, item.inter) || filter.inter === ""

      if (name && village && district && region && lang && inter) {
        return true;
      } else {
        return false;
      }
    }

    function update_counter() { //update 'users selected' counter
      $('#selected-counter').text(Array.from(users).length);
    }

    $(document).ready(function() { //reset checkboxes to fight browser form caching
      $(':checked')
        .toArray()
        .forEach(function(item) {
          $(item).prop('checked', false);
        });
    });

    $('#dispatch').click(function() {

          console.log('ech');
          save = fetch('', {
            method: 'POST',
            body: JSON.stringify({
              msg: $('#ofr-msg').val(),
              pk: Array.from(users),
            }),
            headers: {
              "X-CSRFToken": getCookie("csrftoken"),
              "Accept": "application/json",
              'Content-Type': 'application/json'
            },
            credentials: 'same-origin'
          });

          console.log(JSON.stringify({
            msg: $('#ofr-msg').val(),
            pk: Array.from(users),
          }));

          save.then(x => {
              x.text().then(x => {
                alert(x)
                console.log('y');
              })
            })
          });

        function getCookie(name) {
          var cookieValue = null;
          if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
              }
            }
          }
          return cookieValue;
        }
