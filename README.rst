rdrama
======

**rdrama.net API Wrapper**

Lightweigt API wrapper, made for `rdrama.net <https://rdrama.net>`_. Allows access to API endpoints and returns a JSON result.

Installation
------------

.. code-block:: bash

   git clone https://github.com/IThinkImOKAY/rdrama && cd rdrama && pip3 install .

How to use
----------

Sending a get request:

.. code-block:: python

    import rdrama

    drama = rdrama.Drama(client_id='client_id',
                         client_secret='client_secret',
                         user_agent='user_agent',
                         access_token='access_token',
                         refresh_token='refresh_token')
    dramaqueen = drama.get('/api/v1/user/dramaqueen')
    print(dramaqueen)
    
Sending a post request:

.. code-block:: python

    import rdrama

    drama = rdrama.Drama(client_id='client_id',
                         client_secret='client_secret',
                         user_agent='user_agent',
                         access_token='access_token',
                         refresh_token='refresh_token')
    title = 'API TESTING'
    url = 'https://localhost:8000'
    parameters = {'board': 'general',
                  'title': title,
                  'url' : url}
    submit = drama.post('/api/v1/submit', data=parameters)
    print(submit)
