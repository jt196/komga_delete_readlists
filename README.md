## Delete Empty Read Lists inside Komga

**The Problem**

After deleting a bunch of comics from your Komga installation, you may find that in the libraries view and when you want to add a comic to a readlist, all of the previous Readlists are there, even when they're empty. 

**The Solution**

This script uses the Komga Swagger api to remove any empty readlists. 

**Dependencies**

- Python
- the Python requests library.

**Before you run this**

Enter the URL, user and pass at the prompts. Confirm you want to delete with y/n.

Beware, running delete requests through an API can seriously damage your collection if you don't know what you're doing! 