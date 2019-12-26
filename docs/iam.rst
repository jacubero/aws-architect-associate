AWS Identity and Access Management (IAM)
########################################

`AWS re:Invent 2018: [REPEAT 1] Become an IAM Policy Master in 60 Minutes or Less (SEC316-R1) <https://www.youtube.com/watch?v=YQsK4MtsELU&feature=emb_logo>`_

Account users and IAM
*********************

A **user** is a permanent named operator. It could be a human or it could be a machine. Their credentials are permanent and they stay with that named user until there is a forced rotation, whether it's a name and password, whether it's an access key, secret key combination ,etc. This is my *authentication method* for named users in the system.

A **group** is a collection of users. Groups can have many users, users can belong to many groups.

A **role** is an operation (human or machine) and its credentials are temporary. It is the authentication method for the user.

Permissions happens in a separate object known as the **policy document**. It is a JSON document and attaches either a permanent named user or to a group of users, or to a role. I lists the specific API or wuilcard group of APIs that are white-listed.

Organizing my users
*******************

Federating users
****************

Multiple accounts
*****************
