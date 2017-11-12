
$('#ofr-msg') //Counter for message box
  .bind('input propertychange',
    function countmsg() {
      console.log(this)
      $('#ofr-msg-legend span').text(100 - this.value.length)
      if (this.value.length > 100) {
        $('#ofr-msg-legend span').css('color', 'red')
      } else {
        $('#ofr-msg-legend span').css('color', '#333')
      }
    });

$(document).ready(function() { //cache-bust report fields
  $('#report_deliv').val("")
  $('#report_resp').val("")
  $('#report_rate').val("")
  $('#report_unit').val("")
});

  function report_data(pk) {
    fe = fetch(('/report/' + pk + '/data'),)
    fe.then(x => {
        x.json().then(x => {
          console.log(x);
          $('#report_deliv').val(x.deliv)
          $('#report_resp').val(x.resp)
          $('#report_rate').val(x.pers)
          $('#report_unit').val(x.unit_total)
        });
      });
  }
