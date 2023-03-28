/* JavaScript for Frontend pages */
jQuery(document).ready(function($) {
	try {
		// Invalidate cache of WooCommerce minicart when billing country changes.
		// This will ensure that the minicart is updated correctly
		var supports_html5_storage =('sessionStorage' in window && window['sessionStorage'] !== null);
		if(supports_html5_storage) {
			// The fragment name might be generated dynamically by WooCommerce, so
			// we have to retrieve it from the WC parameters
			// @since WC 3.1
			var fragment_name = 'wc_fragments';
			if((typeof wc_cart_fragments_params !== 'undefined') && wc_cart_fragments_params && wc_cart_fragments_params.fragment_name) {
				fragment_name = wc_cart_fragments_params.fragment_name;
			}

			$('.checkout').on('change', '#billing_country', function() {
				sessionStorage.removeItem(fragment_name, '');
			});

			$('.widget_wc_aelia_country_selector_widget').on('submit', 'form', function() {
				sessionStorage.removeItem(fragment_name, '');
			});
		}
	}
	catch(exception) {
		var error_msg = 'Aelia - Exception occurred while accessing window.sessionStorage. ' +
										'This could be caused by the browser disabling cookies. ' +
										'COOKIES MUST BE ENABLED for the site to work correctly. ' +
										'Exception details below.';
		console.log(error_msg);
		console.log(exception);
	}

	// Select2 Enhancement if it exists
	if($().select2) {
		$('.widget_wc_aelia_country_selector_widget').find('select').select2();
	}

	/* If we are not handling the State, hide the "Change country" button and
	 * submit the Widget form when the country changes. If we are handling the
	 * State, then the form has multiple selections, and we should allow the user
	 * to change all of them and declare when he is finished by clicking the
	 * "change location" button.
	 */
	if((typeof aelia_tdbc_params != 'undefined') && (aelia_tdbc_params.handle_customer_state != 1)) {
		$('.widget_wc_aelia_country_selector_widget')
			.find('.change_country')
			.hide()
			.end()
			.on('change', '.country_selector, input.tax_exempt', function(event) {
				var widget_form = $(this).closest('form');
				$(widget_form).submit();
				event.stopPropagation();
				return false;
		});
	}
	else {
		// wc_country_select_params is required to handle States/Counties
		/* The following code is inspired by the equivalent code found in WooCommerce's
		 * country-select.js
		 */
		if(typeof wc_country_select_params != 'undefined') {
			/* State/Country select boxes */
			var states_json = wc_country_select_params.countries.replace(/&quot;/g, '"');
			states = $.parseJSON(states_json);

			$('.widget_wc_aelia_country_selector_widget').find('.change_country').show();

			$('.widget_wc_aelia_country_selector_widget').on('change', 'select.country_selector', function() {
				var
					$widget = $(this).parents('.widget_wc_aelia_country_selector_widget').first(),
					country = $(this).val(),
					$statebox = $widget.find('select.state_selector'),
					$statebox_parent = $statebox.parents('.wrapper.state_selector').first(),
					input_name = $statebox.attr('name'),
					value = $statebox.val(),
					placeholder = $statebox.attr('placeholder');

				$statebox.find('option').remove();
				if(states[country] && !$.isEmptyObject(states[country])) {
					// There are States/Counties associated with the country
					var
						options = '',
						state = states[country];

					for(var index in state) {
						if(state.hasOwnProperty(index)) {
							$statebox.html()
							$statebox.append($('<option>', {
								value: index,
								text: state[index]
							}));
						}
					}
					$statebox_parent.show();
					$statebox.change();
				}
				else {
					// There aren't States/Counties. Hide the selector
					$statebox_parent.hide();
					$statebox.val('');
				}
				$('body').trigger('country_to_state_changed', [country, $widget]);
			});
			$('.widget_wc_aelia_country_selector_widget').find('select.country_selector').trigger('change');
		}
	}
});
