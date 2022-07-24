import logging
logging.basicConfig(filename="tuple1.log", level=logging.DEBUG,format=' %(asctime)s, %(levelname)s, %(message)s')

#creating class for tuple

class class_tuple:
    logging.info("entering into class_tuple")

    def extract_tuple(self,t):
        """extracting tuple"""
        logging.info("entering into of function of extract tuple")
        self.t=t
        try:
            for i in t:
                if type(i)==tuple:
                    logging.info(i)
        except Exception as e:
            logging.error(e)
        else:
            logging.info("executed successfully")

t=("sant", "kumar", [1,2,3,4],(6,7,8),{"k1":5})

obj1=class_tuple()
obj1.extract_tuple(t)
