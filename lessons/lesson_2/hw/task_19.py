
is_permission_denied = False
is_stock_product = True
type_of_value = 'grid'
# type_of_value = 'table'
is_equities = True
is_admin = True

VIEW_DATA = 1
SUBMIT_DATA = 2
VIEW_PRODUCTS = 4
MANAGE_DATA = 8

if is_permission_denied:
    print("Permission is denied" if not is_stock_product else "Stock products are not available anymore")
elif not is_equities:
    match type_of_value:
        case 'grid':
            print("Grid representation of the data: ...")
        case 'table':
            print("Table representation of the data: ...")
        case _:
            print("Unsuported format of the data")
elif is_equities:
    print("Equities are supported only in grid table for now: ...")

permissioned_operations = 0
if is_admin:
    permissioned_operations = VIEW_DATA | SUBMIT_DATA | MANAGE_DATA | VIEW_PRODUCTS
else:
    permissioned_operations = VIEW_DATA | MANAGE_DATA

operation = input("Type operation you would like to proceed with: ").strip().lower()

match operation:
    case "view" if permissioned_operations & VIEW_DATA:
        print("View data: ...")
    case "submit" if permissioned_operations & SUBMIT_DATA:
        print("Submit data: ...")
    case "view_products" if permissioned_operations & VIEW_PRODUCTS:
        print("View products: ...")
    case "manage" if permissioned_operations & MANAGE_DATA:
        print("Manage Data: ...")
    case _:
        print("You don't have access")

