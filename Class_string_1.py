import logging
logging.basicConfig(filename="str1.log",level=logging.DEBUG,format="%(levelname)s, %(asctime)s, %(message)s")

#creating class for string with logging try and exception handling.

class class_string:
    logging.info("entering into class_string")

    def vowels(self,s):
        """extracting vowels"""
        self.s=s
        logging.info("entering into function vowels")
        try:
            l1=[]
            for i in range(len(s)):
                if s[i].lower() in "aeiou":
                    l1.append(i)
            logging.info(l1)

        except Exception as e:
            logging.info(e)
        else:
            logging.info("class_string executed successfully")

    def remove_space(self,s1):
        """function to remove space in a string"""
        self.s1=s1
        logging.info("entering to function remove_space in a string")
        try:
            a=s1.replace(" ","")
            logging.info(a)
        except Exception as e:
            logging.info("remove_space faced an issue with error %s",e)
        else:
            logging.info("executed successfully")

    def length_string(self,l):
        """function for length of the string"""
        self.l=l
        logging.info("entering into the function length_string")
        try:
            count=0
            for i in l:
                count=count+1
            logging.info(count)

        except Exception as e:
            logging.error(e)
        else:
            logging.info("executed successfully")

s="santo"
st="remove space "
integer=5683

obj1=class_string()
obj1.vowels(s)
obj1.remove_space(st)
obj1.length_string(integer)


