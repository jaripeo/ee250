# Lab 3

## Team Members
- team member 1
- team member 2

## Lab Question Answers

Question 1: Why are RESTful APIs scalable?

RESTful APIs are scalable becuase they are stateless which means that each request from a client to the server must contain all the information needed to understand and process the request. This would allow the servers to handle requests independently, making it easy to add ore remove servers to handle more or fewer requests which can also be called horizontal scaling. 

Question 2: According to the definition of "resources" provided in the AWS article above, What are the resources the mail server is providing to clients?

Based on the AWS definition, the resources the mail server is providing to clients include:
- Email messages(the content of sent and received emails)
- Mailboxes or folders (such as inbox, sent)
- Metadata about emails (such as sender, recipient, subject, and timestamps)

Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?

One common REST Method not used in our mail server is PUT as the server contains POST (to create new mail), GET (to retrieve mail) and DELETE (to delete mail). We can extend our mail server to using PUT by adding a route that allows clients to update an existing email like editing the subject or body or marking an email as read or unread. 

Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve? Make sure to cite any online resources you use to answer this question!

API keys are used for many RESTful APIs to provide authentication, project identification, and authorization. They help ensure that only approved applications can access the API, protect against misuse, and allow API providers to monitor and control usage. API keys also help track how the API is being used and by whom.

Source: https://cloud.google.com/endpoints/docs/openapi/when-why-api-key