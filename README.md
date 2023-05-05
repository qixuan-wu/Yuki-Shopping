#  Yuki-Shopping Website

## 1. *What is it?*

Yuki-Shopping is an online shopping site whose business interests include e-commerce, where they buy and store inventory and handle everything from shipping and pricing to customer service and returns.Administrators can see price chart tracking

**render url**:https://yuki-shopping.onrender.com

## 2.  *## Do the set up work*
1. We need to enter our file 
 ```
 cd Yuki-Shopping
``` 
 2. via the terminal and execute these commands:
 ```
    pyenv local 3.7.0 # this sets the local version of python to 3.7.0
    python3 -m venv .venv # this creates the virtual environment for you
    source .venv/bin/activate # this activates the virtual environment
    pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.
```
 3. We install that with
 ```
    pip install django
    pip install django-leaflet
```
To make the images loadable you also need the plug-in for loading images
   
 4. Create a superuser
 ```
    python3 manage.py createsuperuser
```
Then set your account password so you have everything you need to be an administrator
## 3.   *Code Description*

   This site mainly buys household items, users can use the shopping cart after registering and logging in, and can use the search to find what they want.
   
   
   Users can add the items they want to the shopping cart and select the quantity on the detail page. Also on the details page the user can see where the delivery is located via a map to determine how many days it will take for the logistics to reach them.

Administrators can see the product data and transaction records in the back office.

At the same time the administrator can see the price tracking chart via the price tracking item in the navigation bar to see which stage of the product the user bought more once the point

## 4.   *Start the Server*
We do this using the manage.py  command tool by entering this command in the terminal:
```
    python3 manage.py runserver
```

If you're doing this on another platform, then you might need to use this instead (change the port number from 8000 as required):
```
    python3 manage.py runserver 0.0.0.0:8000 
```

If it went well, then you should see the python rocket launching your site.
## 5.   *What you can do with this application*

1. Visitors need to register to access the various features

2. Users can view the site's products, search for what they want, add what they want to their shopping cart, make a purchase and check where it is shipped

3. Administrators can view user information, order information and see price charts to analyse which range of prices users are buying more of.


## 6. Background

The data is come from kaggle:
**[link(https://www.kaggle.com/datasets/lokeshparab/amazon-products-dataset)]**
## 7.Contributing
Contributions are welcome! Please fork this repository and submit a pull request.
## 8.  License
This project is licensed under the MIT License. See the file for more information.`LICENSE`
