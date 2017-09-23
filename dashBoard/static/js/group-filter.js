var group = new Set()

function group_toin() { //Add values to input element
  $('#groupField').val(
    JSON.stringify(
    Array.from(group)
    )
  );
//convert to set, then back to array, then to json, to remove duplicates
console.log($('#groupField').val())
}

$('#group-toggle').click(function() {
  if (this.text === 'Hide') {
    $('.group-selector-item').hide();
    this.text = 'Show';
  } else {
    $('.group-selector-item').show();
    this.text = 'Hide';
  }
});

$('.group-filter input') //When filter attributes changes
  .bind('input propertychange', function() {

    $('.group-selector-item').toArray().forEach(function(item) {

      let exitem = group_extract_data(item);
      let filter = group_get_filter();
      let comp = group_filter_compare(exitem, filter);

      if (comp == false) {
        $(item).addClass('hidden');
      } else {
        $(item).removeClass('hidden');
      }
    });
  });

function group_extract_data(item) { //get data from html node data- attributes
  item = $(item);
  return {
    "name": item.data('name'),
    "district": item.data('district'),
    "region": item.data('region'),
    "contact": item.data('contact'),
  };
}

function group_get_filter() { //get filter data from the filter header
  return {
    "name": $('#group-Name').val(),
    "district": $('#group-District').val(),
    "region": $('#group-Region').val(),
    "contact": $('#group-Contact').val(),
  };
}

function group_filter_compare(item, filter) { //compare the filter and the item and return a boolean

  let name = search(filter.name, item.name) || filter.name === ""
  let district = search(filter.district, item.district) || filter.district === ""
  let region = search(filter.region, item.region) || filter.region === ""
  let contact = search(filter.contact, item.contact) || filter.contact === ""

  if (name && district && region && contact) {
    return true;
  } else {
    return false;
  }
}

$(document).ready(function() { //reset checkboxes to fight browser form caching
  $(':checked')
    .toArray()
    .forEach(function(item) {
      $(item).prop('checked', false);
    });
});

$('.group-selector-check').click(function() { //Add/remove item to users array when checkbox is clicked
  if (this.checked) {
    group.add($(this).data('pk'));
  } else {
    group.delete($(this).data('pk'));
  }
  group_toin();
});

$('#group-checkall').click(function() { //Check all visable elements adn add to users
  $('.group-selector-item')
    .toArray()
    .forEach(function(item) {
      if ($(item).hasClass('hidden') == false) {
        if ($('#group-checkall').prop('checked')) {
          group.add($(item).data('pk'));
          $(item).find('.group-selector-check').prop('checked', true);
        } else {
          group.delete($(item).data('pk'));
          $(item).find('.group-selector-check').prop('checked', false);
        }
      }
    });
  group_toin();
});
