BuzzlogixTextAnalysisAPILib
=================
This API SDK was automatically generated by APIMATIC BETA v2.0

Due to the UniRest package dependency this SDK only works under Python 2.7
It will not work using Python 3.x

How To Configure:
=================
The generated code might need to be configured with your API credentials. To do that,
open the file "Configuration.py" and edit its contents.

How To Build: 
=============
The generated code uses Python libraries named UniRest and Jsonpickle. 

PIP is a popular tool for managing python packages[1].
To resolve these packages:
1) From terminal/cmd navigate to the root directory
2) Invoke 'pip install -r requirements.txt'

Note: You will need internet access to resolve these dependencies.

How To Use:
===========
The following shows how to make invoke the ObjectivityController controller.
It is also shown in [2].

    1. Create a "ObjectivityControllerTest.py" file in the root directory.
    2. Add the following import statement 
        'from BuzzlogixTextAnalysisAPILib.Controllers.ObjectivityController import *'
    3. Create a new instance using 'controller = ObjectivityController()'
    4. Invoke an endpoint with the appropriate parameters, for example
        'response = controller.create_return_objectivity(<required parameters if any>)'
    5. "response" will now be an object of type Void.

[1] PIP - https://pip.pypa.io

[2] from BuzzlogixTextAnalysisAPILib.Controllers.ObjectivityController import *

	controller = ObjectivityController()
    response = controller.create_return_objectivity()

    print response
