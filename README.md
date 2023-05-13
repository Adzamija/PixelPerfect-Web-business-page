# PixelPerfect-Web-business-page
## Efficiently designed and developed website for a web development company using the Django Framework, incorporating all necessary features and functionalities to fully meet the client's business needs.

## Website specifications
1. index(): This view renders the main/index.html template and displays a list of all Blog objects in the database. It takes a GET request as input and returns a response containing the rendered HTML template.
2. about(): This view renders the main/about.html template. It takes a GET request as input and returns a response containing the rendered HTML template.
3. contact(): This view handles both GET and POST requests. If a GET request is received, it renders the main/contact.html template. If a POST request is received, it retrieves the subject, from_email, phone, and message from the request.POST object, validates the data, and sends an email to the email address adzamija@icloud.com using the send_mail() function from Django's built-in email library. If the email is sent successfully, it returns a response containing the main/contact.html template with a success message. If there is an error with the email header, it returns a response containing the main/contact.html template with an error message.
4. pricing(): This view renders the main/pricing.html template. It takes a GET request as input and returns a response containing the rendered HTML template.
5. faq(): This view renders the main/faq.html template. It takes a GET request as input and returns a response containing the rendered HTML template.
6. blog_home(): This view renders the main/blog-home.html template. It takes a GET request as input and returns a response containing the rendered HTML template.
7. blog_post(): This view handles both GET and POST requests. If a GET request is received, it retrieves the blog object with the primary key specified in the URL, as well as all comments associated with that blog post, and renders the main/blog-post.html template with these objects passed as context. If a POST request is received, it retrieves the comment from the request.POST object, creates a new Comments object associated with the specified blog post, and saves it to the database. It then retrieves the blog object and all comments associated with that blog post, and renders the main/blog-post.html template with these objects passed as context.
8. portfolio(): This view retrieves all Portfolio objects from the database and renders the main/portfolio.html template with these objects passed as context. It takes a GET request as input and returns a response containing the rendered HTML template.
portfolio_item(): This view retrieves the Portfolio object with the primary key specified in the URL and renders the main/portfolio-item.html template with this object passed as context. It takes a GET request as input and returns a response containing the rendered HTML template.
9. privacy(): This view renders the main/privacyandterms.html template. It takes a GET request as input and returns a response containing the rendered HTML template.

## How To Use App
### To use this code, you also need to have the following installed on your machine:

1. Python
2. Django

## Tehnical specifications
The website's backend was developed using Python 3 and Django, with HTML, Jinja, and CSS used to create the website's frontend. The website's design includes elements from Bootstrap 5, as well as custom CSS styles.

The main goal of the website was to create a business page for a company, with sections for displaying blog posts, providing information about the company, showcasing the company's past work, and providing pricing information.

Looking towards the future, the website could be further improved by incorporating payment methods for the pricing page. This would allow potential customers to make payments directly through the website, making it easier for them to purchase the company's services.

## Contact
Any information, bugs or questions can be sent on the e-mail adress: adzamija@icloud.com
