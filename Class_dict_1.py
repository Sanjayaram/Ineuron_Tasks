import logging

logging.basicConfig(filename="dict1.log", level=logging.DEBUG, format='%(asctime)s, %(levelname)s,%(message)s')

#creating class for dictonary input

class Dict:
    logging.info("entering into dictionary class")

    def __init__(self, d):
        self.d = d

    def extract_all_items(self):
        """extracting all the elements from the dictionary"""
        logging.info("entering into function extract_all_items")

        self.l = []
        try:
            if type(d)!=dict:
                raise Exception("input is not a dictionary")
            else :
                for i, j in (self.d).items():
                    (self.l).append(i)
                    if type(j) == list:
                        (self.l).extend(j)
                    if type(j) == dict:
                        for m, k in j.items():
                            (self.l).extend(m)
                            if type(k) == list:
                                (self.l).extend(k)
                logging.info(self.l)
        except Exception as e:
            logging.error("error is %s",e)
        else:
            logging.info("executed successfully")

    def add_int(self):
        """creating function for adding integers in dictionary"""
        logging.info("entering into function add integers")

        try:
            count=0
            l=(self.d).items()

            if type(d)!=dict:
                raise Exception()
            else:
                for i,j in l:
                    if type (i)==int:
                        count=count+i
                    if type(j)==list:
                        for a in j:
                            if type(a)==int:
                                count=count+a
                    if type(j)==dict:
                        for b,c in j.items():
                            if type(b)==int:
                                count=count+b
                            if type(c)==list:
                                for f in c:
                                    if type(f)==int:
                                        count=count+f
        except Exception as e:
            logging.error("error is %s",e)
        else:
            logging.info("add integer executed successfully and the count = %s",count)


d = {'1': [1, 2, 3], '2': {'3': [3, 3, 3], 'a': ['an', 'ku', 'r']}}
j=6556

obj1=Dict(j)
obj1.extract_all_items()
obj1.add_int()



