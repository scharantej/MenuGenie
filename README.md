## Design for Flask Application: Sales Partners' Service Selection Tool

**HTML Files**

1. `index.html`:
   - Purpose: Serves as the landing page for the application.
   - Content: Contains a form with fields for the sales partner to input their requirements. These fields may include the industry they work in, the size of their company, their budget, etc.
   - Submit button: Redirects the user to the `/results` route.

2. `results.html`:
   - Purpose: Displays the list of services that match the sales partner's requirements.
   - Content: Contains a table with columns for the service name, description, and price. It also includes a button for each service that, when clicked, takes the sales partner to a page where they can request the service.

**Routes**

1. `/`:
   - Purpose: Handles the GET request for the landing page (`index.html`).
   - Function: Renders the `index.html` file.

2. `/results`:
   - Purpose: Handles the POST request from the form on the landing page.
   - Function:
     - Receives the form data containing the sales partner's requirements.
     - Queries a database or performs calculations to determine the list of services that match the requirements.
     - Renders the `results.html` file, passing the list of services as data.

3. `/request-service/<service_id>`:
   - Purpose: Handles the GET request for the page where the sales partner can request a service.
   - Function:
     - Receives the `service_id` from the URL.
     - Queries the database to retrieve the details of the service with the given ID.
     - Renders a page with the service details and a form for the sales partner to submit their contact information.

4. `/submit-request`:
   - Purpose: Handles the POST request from the form on the service request page.
   - Function:
     - Receives the form data containing the sales partner's contact information.
     - Saves the request in a database or forwards it to the appropriate specialist.
     - Displays a confirmation message to the sales partner.