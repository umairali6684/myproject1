frappe.ui.report.on("My Report", "onload", function(report) {
    // Get the current filters for the report
    var filters = report.get_values();
    
    // Set the company filter to be empty, to display data for all companies
    filters.company = "";
    
    // Refresh the report with the updated filters
    report.set_filters(filters);
    report.refresh();
});

/*In this example, we are using the frappe.ui.report.on function to define a callback 
for when the report loads. Inside the callback, we get the current filters for the 
report using report.get_values(). We then update the company filter to be an empty string, which means no
filter will be applied to limit the data to a specific company. Finally,
 we set the updated filters on the report using report.set_filters and refresh the report using report.refresh().
This client script can be attached to any report in ERPNext by adding it to the
 "Custom Script" field in the report settings. Make sure to replace "My Report" with the name of the report you want to modify.*/
