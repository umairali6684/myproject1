from frappe import _

def execute(filters=None):
    columns = [
        _("Company") + ":Link/Company:120",
        _("Sales Order") + ":Link/Sales Order:120",
        _("Customer") + ":Link/Customer:120",
        _("Item") + ":Link/Item:120",
        _("Qty") + ":Float:120"
    ]
    data = []

    # Get a list of all companies
    companies = frappe.get_all("Company", fields=["name"])
    
    # Loop through all companies and get data for each one
    for company in companies:
        company_data = []
        company_name = company["name"]
        
        # Query data for this company
        sales_orders = frappe.db.sql("""
            SELECT company, name, customer, item_code, qty
            FROM `tabSales Order Item`
            WHERE docstatus = 1 AND company = %s
        """, company_name, as_dict=True)

        # Build the data for this company
        for so in sales_orders:
            company_data.append([
                so.company,
                so.name,
                so.customer,
                so.item_code,
                so.qty
            ])

        # Add the data for this company to the overall data list
        data += company_data
    
    return columns, data


'''In this example, we define a function called execute that takes a filters argument (which we are not using in this case). 
The function returns two values: a list of column definitions and a list of data rows.

Inside the function, we first define the column definitions for our report. Then, 
we get a list of all companies using frappe.get_all("Company", fields=["name"]). We loop through each company 
and query data for that company using a SQL query. 
We build a list of data rows for each company, and then add those rows to the overall data list.

Finally, we return the column definitions and data list to be displayed in the report.

To use this server script report in ERPNext, create a new report and select "Script Report" as the report type. 
Then, copy and paste this code into the "Python Script" field. You can modify the column definitions 
and SQL query to fit the needs of your report.
'''
