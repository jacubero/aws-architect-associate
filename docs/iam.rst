AWS Identity and Access Management (IAM)
########################################

Account users and IAM
*********************

A **user** is a permanent named operator. It could be a human or it could be a machine. Their credentials are permanent and they stay with that named user until there is a forced rotation, whether it's a name and password, whether it's an access key, secret key combination ,etc. This is my *authentication method* for named users in the system.

A **group** is a collection of users. Groups can have many users, users can belong to many groups.

A **role** is an operation (human or machine) and its credentials are temporary. It is the authentication method for the user.

Permissions happens in a separate object known as the **policy document**. A policy specifies resources and the operations that can be perform on these resources. It is a JSON document and attaches either a permanent named user or to a group of users, or to a role. I lists the specific API or wuilcard group of APIs that are white-listed.

Identities in AWS exist in these forms:

* **IAM users**: Users created within the account.

* **Roles**: Temporary identities used by EC2 instances, Lambdas, and external users.

* **Federation**: Users with Active Directoty identities or other corporate credentials have role assigned in IAM.

* **Web Identity Federation**: Users with web identities from Amazon.com or other Open ID provier have role assigned using Security Token System (STS).

`Secure Access to AWS Services Using AWS Identity and Access Management (IAM) Roles <https://www.youtube.com/watch?v=wY7FOFaPNuE&feature=emb_logo>`_ 

`How to Enable Multi-Factor Authentication (MFA) for Your AWS User Account <https://www.youtube.com/watch?v=A3AObXBJ4Lw&feature=emb_logo>`_

Organizing my users
*******************

Federating users
****************

Multiple accounts
*****************

`AWS re:Invent 2018: [REPEAT 1] Become an IAM Policy Master in 60 Minutes or Less (SEC316-R1) <https://www.youtube.com/watch?time_continue=2&v=YQsK4MtsELU&feature=emb_logo>`_