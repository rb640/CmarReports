import os
import uuid
import logging
import zipfile
import appsettings
#log = logging.getLogger(__name__)

def get_logs_list():
    '''
    Returns list of all present log files.
    '''    
    result = []    
    for file in os.listdir(appsettings.LOG_DIR):
        result.append(file)
        
    #log.debug('Found log files: %s', str(result))
    return result

def create_log_archive():
    '''
    Create log file archive.
    Returns archive file name or None if creation failed.
    '''
    archive_filename = os.path.join(os.getcwd(), appsettings.TEMP_DIR, str(uuid.uuid4()))
    
    zip_file = zipfile.ZipFile(archive_filename, 'w')
    for log_file in get_logs_list():
        zip_file.write(os.path.join(appsettings.LOG_DIR, log_file), arcname=log_file)        
    zip_file.close()
    return archive_filename
print create_log_archive()