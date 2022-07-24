import logging

logging.basicConfig(filename="list.log", level=logging.DEBUG, format=' %(asctime)s, %(levelname)s, %(message)s')

#creating class for list with logging try and exception handling.

class List:
    logging.info("getting into the list")
    def extract_list(self,l):
        """extract list from the collection"""
        self.l=l
        logging.info("we are into extract_list function")
        try:
            for i in self.l:
                if type(i)==list:
                    #print (i)
                    logging.info("result of extracted list %s", i)
        except Exception as e:
            logging.error("provided object is not a list %s",e)
        else:
            logging.info("list has been extracted successfully")

    def extract_dict(self,l):
        """extract dict from the collection"""
        self.l=l
        logging.info("we are into extract_dict function")
        try:
            for i in self.l:
                if type(i)==dict:
                    #print(i)
                    logging.info(i)
        except Exception as e:
            logging.error("provided object is not a list %s",e)
        else:
            logging.info("dict extracted successfully")

    def extract_ineuron(self,l):
        self.l=l
        """extract 'ineuron' from the collection"""
        logging.info("we are into extract_ineuron function")
        try:
            for i in self.l:
                if type(i)==list:
                    for j in i:
                        if j=="ineuron":
                            #print(j)
                            logging.info(j)

                elif type(i)==dict:
                    for k in i:
                        if i[k]=="ineuron":
                            #print(i[k])
                            logging.info(i[k])
        except Exception as e:
                logging.error("provided object is not a list %s",e)
        else:
            logging.info("extracted successfully")

    def flat_list(self,l):
        """extract all the elemnts into single list"""
        self.l=l
        logging.info("entering to flat_list function")
        try:
            l1=[]
            for i in self.l:
                if type(i)!=dict:
                    for j in i :
                        l1.append(j)
                elif type(i)==dict:
                    for k in i:
                        l1.append(k)
                        l1.append(i[k])
            logging.info("flat_list = %s",l1)
        except Exception as e:
            logging.error("provided object is not a list %s", e)
        else:
            logging.info("flat_list function executed successfully")


l = [[1,2,3,4], (2,3,4,5,6),(3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]),
     {'k1':"sudh", 'k2':"ineuron", 'k3':"kumar", 3:6,7:8}, ["ineuron", "data science"]]

object=List()
object.extract_list(l)
object.extract_dict(l)
object.extract_ineuron(l)
object.flat_list(l)



