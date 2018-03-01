$(document).ready(function() {
	$("#dt").datepicker({ 
	  autoclose: true, 
	  todayHighlight: true,
	  dateFormat: 'yy-mm-dd'
	});
	$('#request_list').DataTable();
} );

ko.validation.init({
    registerExtenders: true,
    messagesOnModified: true,
    insertMessages: true,
    parseInputAttributes: true,
    errorClass: 'errorStyle',
    messageTemplate: null
}, true);

(function () {
	var featureModel = function(){
		var self = this;
		var client_list;
		var product_list;
		var request_list;
		
		$.ajax({
			type: 'GET',
			url: 'api/client_list/',
			contentType: "application/javascript",
			dataType: "json",
			async:false,
			success: function (data) {
				client_list = data;
			},
			error: function (jq, st, error) {
			}
		});
		
		$.ajax({
			type: 'GET',
			url: 'api/product_list/',
			contentType: "application/javascript",
			dataType: "json",
			async:false,
			success: function (data) {
				product_list = data;
			},
			error: function (jq, st, error) {
			}
		});
		
		$.ajax({
				type: 'GET',
				url: 'api/new_request/',
				contentType: "application/javascript",
				dataType: "json",
				async:false,
				cache:false,
				success: function (data) {
					request_list = data;
				},
				error: function (jq, st, error) {
				}
			});
			
		self.validateNow = ko.observable(false);
		self.client = ko.observableArray(client_list);
        self.c_id = ko.observable().extend({required: true});
		self.product = ko.observableArray(product_list);
        self.p_id = ko.observable().extend({required: true});
		self.title = ko.observable().extend({required: true});
		self.description = ko.observable().extend({required: true});
		self.req_priority = ko.observable().extend({required: true});
		self.t_date = ko.observable().extend({
							required: true, 
							validation: {
								validator: function (val) {
									val = val.replace(/-/g,'/')
									return new Date(val) > new Date();
								},
								message: "Date should be greater than today's date",
							}
						});
		self.errors = ko.validation.group(self);
		self.request_list = ko.observableArray(request_list);
		
		self.submit = function () {
            self.validateNow(true);
            if (self.errors().length === 0) {
				var req_json = ko.toJSON({
					  "title": self.title,
					  "description": self.description,
					  "c_id": self.c_id,
					  "p_id": self.p_id,
					  "t_date": self.t_date,
					  "req_priority": self.req_priority
					});
				$.ajax({
					url: 'api/new_request/',
					type: 'POST',
					dataType: 'json',
					data: req_json,
					contentType: 'application/json; charset=utf-8',
					success: function (data) {
						$("#modal-dialog .close").click();
						location.reload();
					},
					error: function (jq, st, error){
						$("#modal-dialog .close").click();
						location.reload();
					}
				});
            }
            else
            {
                self.errors.showAllMessages();
                return;
            }
             
        }
	}
    ko.applyBindings(new featureModel());
})();	