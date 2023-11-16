//  reload cheyyathirikkan

$(document).on("submit", "form.ajax", function (e) {
  e.preventDefault();

  var thiss = $(this);

  var url = thiss.attr("action");
  var method = thiss.attr("method");

  jQuery.ajax({
    type: method,
    url: url,
    //  json type matrame sweegarikku
    dataType: "json",
    data: new FormData(this),
    contentType: false,
    cache: false,
    processData: false,
    success: function (data) {
      var title = data["title"];
      var message = data["message"];
      var status = data["status"];

    //   Custom - alert message
      Swal.fire({
        icon: status,
        title: title,
        text: message,
      });

    //   form filed clear cheyyan
      if (status == "success") {
        thiss.trigger("reset");
      }
    },
    error: function (data) {
      console.log(data);
    },
  });
});
