"use strict";

jQuery(document).on('click', '.cwg_popup_submit', function () {
    jQuery.blockUI({message: null});
    var current = jQuery(this);
    var product_id = current.attr('data-product_id');
    var variation_id = current.attr('data-variation_id');
    var security = current.attr('data-security');
    var data = {
        action: 'cwg_trigger_popup_ajax',
        product_id: product_id,
        variation_id: variation_id,
        security: security
    };
    jQuery.ajax({
        type: "post",
        url: cwginstock.default_ajax_url,
        data: data,
        success: function (msg) {
            jQuery.unblockUI();
            Swal.fire({
                html: msg,
                showCloseButton: true,
                showConfirmButton: false,
                willOpen: function () {
                    if ('1' == cwginstock.enable_recaptcha) {
                        jQuery('.g-recaptcha').before('<div id="cwg-google-recaptcha"></div>');
                        jQuery('.g-recaptcha').remove();
                    }
                },
                didOpen: function () {
                    jQuery(document).trigger('cwginstock_popup_open_callback');
                },
                willClose: function () {
                    jQuery(document).trigger('cwginstock_popup_close_callback');
                },
            });

        },
        error: function (request, status, error) {
            jQuery.unblockUI();
        }
    });
    return false;
});

jQuery(document).on('cwginstock_popup_open_callback', function () {
    instock_notifier.onloadcallback();
});

jQuery(document).on('cwginstock_popup_close_callback', function () {
    instock_notifier.resetcallback();
});

