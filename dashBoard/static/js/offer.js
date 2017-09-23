
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
