/* Ma's finest spagetti code, good luck! */
var inter = new Set()

function inter_toin(){ //Add values to input element
$('#interField').val(
  JSON.stringify(
  Array.from(inter)
  )
);
//convert to set, then back to array, then to json, to remove duplicates
console.log($('#interField').val())
}

$('#inter-toggle').click(function() {
  if(this.text === 'Hide'){
    $('.inter-selector-item').hide();
    this.text = 'Show';
  }else{
    $('.inter-selector-item').show();
    this.text = 'Hide';
  }
});

$('.inter-filter input') //When filter attributes changes
  .bind('input propertychange', function() {

    $('.inter-selector-item').toArray().forEach(function(item) {

      let exitem = inter_extract_data(item);
      let filter = inter_get_filter();
      let comp = inter_filter_compare(exitem, filter);

      if (comp == false) {
        $(item).addClass('hidden');
      } else {
        $(item).removeClass('hidden');
      }
    });
  });

function inter_extract_data(item) { //get data from html node data- attributes
  item = $(item);
  return {
    "name": item.data('name'),
    "members": item.data('members'),
  };
}

function inter_get_filter() { //get filter data from the filter header
  return {
    "name": $('#inter-Name').val(),
    "members": $('#inter-Members').val(),
  };
}

function inter_filter_compare(item, filter) { //compare the filter and the item and return a boolean

  let name = search(filter.name, item.name) || filter.name === ""
  let members = search(filter.members, item.members) || filter.members === ""

  if (name && members) {
    return true;
  } else {
    return false;
  }
}

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

$(document).ready(function() { //reset checkboxes to fight browser form caching
  $(':checked')
    .toArray()
    .forEach(function(item) {
      $(item).prop('checked', false);
    });
});

$('.inter-selector-check').click(function() { //Add/remove item to users array when checkbox is clicked
  if (this.checked) {
    inter.add($(this).data('pk'));
  } else {
    inter.delete($(this).data('pk'));
  }
  inter_toin();
});

$('#inter-checkall').click(function() { //Check all visable elements adn add to users
  console.log('checkall');
  $('.inter-selector-item')
    .toArray()
    .forEach(function(item) {
      if ($(item).hasClass('hidden') == false) {
        if ($('#inter-checkall').prop('checked')) {
          inter.add($(item).data('pk'));
          $(item).find('.inter-selector-check').prop('checked', true);
        } else {
          inter.delete($(item).data('pk'));
          $(item).find('.inter-selector-check').prop('checked', false);
        }
      }
    });
    inter_toin();
});


$(document).ready(function reversecheckup() {

let liststr = String($('#interField').data('val'))
.replace('[','')
.replace(']','')
.replace(' ','')
.split(",");

let listint = liststr.map(x => {return parseInt(x)});

console.log(listint);

listint.forEach(x => {
$("#inter_" + x).prop('checked', true);
inter.add(x);
inter_toin();
});
});
