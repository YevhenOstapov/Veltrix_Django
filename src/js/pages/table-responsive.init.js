/*
  Name: Veltrix - Admin & Dashboard  
Author: Themesbrand
Website: https://themesbrand.com/
Contact:  andzukor@gmail.com
File: Table responsive Init Js File
*/

$(function() {
    $(".table-responsive").responsiveTable({
        addDisplayAllBtn: "btn btn-secondary"
    });

    $(".btn-toolbar [data-toggle=dropdown]").attr("data-bs-toggle", "dropdown");
});
