print("this is test!!!!!!!")

import logging, sys

#logging.basicConfig(stream= sys.stdout,level=logging.info)
logging.basicConfig(
    level=logging.INFO,  
    format="[%(asctime)s] [%(levelname)s] %(message)s", 
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger()
log.addHandler(logging.FileHandler("test.log", "w"))
log.info("This is logging info!!!!!!")