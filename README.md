# GM-Marketing-Requests
GM Marketing Requests will act as an inventory system and a website to submit requests for new materials

## Required
* sqlite3
* flask
* wtforms

## Functions
* Customer Experience Managers will have access to a webpage that allows them to submit requests for marketing materials.
  * If the Customer Experience Manager is requesting uniforms, they will be notified if the items they are requesting are not in inventory.
  * They will then be prompted to make a different selection or to contact the GM Marketing Department.
  * When their request is marked as complete, the individual who requested the items will recieve and email letting them know they are on their way.
* The GM Marketing Department will have access to a different section of the webpage that allows them to view all submitted requests.
  * On this view, they will be able to sort and mark items as complete. they will also have the ability to make edits to the requests
* In addition to the previous view, the GM Marketing Department will have access to a different view for inventory.
  * This view will allow them to enter new items into inventory, as well as view current inventory levels
