import os
import uuid
import logging
import zipfile
import appsettings
#log = logging.getLogger(__name__)

result = []    
for file in os.listdir(appsettings.LOG_DIR):
	result.append(os.path.abspath(file))
    
print result
