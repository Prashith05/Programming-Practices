'''
WAP USING CLASS AND OBJECT
--> TAKE THE TRAIN DETAILS ,HAVING THE DETAILS LIKE TRAIN NUMBER ,TRAIN NAME,STARTING FROM END,
   DAYS OF RUN ,PRICE OF SLEEPER,GENERAL AND A/C 
-->EACH TRAIN DETAILS SHOULD BE IN THE FORM OF DICTIONARY AND ALL THE TRAIN DETAILS SHOULD BE IN
   THE FORM OF LIST AS FOLLOWS
   create a methods like 
-->get_train_name() use the train_no parameter
-->get_trains_in_day() ----it should accept day name as a parameter and 
   it should display all the train names which is running on that day
-->get_total_fare() ---- it should accept two parameters 
                        1.train_no
                        2.dict{
                         'general': 120
                         'sleeper' : 20
                         'AC ' : 30
                         }total_seat    
'''

train_list = [
   {
      'train_no':84314,
      'train_name':"mysore express",
      'start':"mysore express",
      'end ': "bangalore",
      'days_of_run ':['SUN','MON','TUE','THU','SAT'],
      'general':60,
      'sleeper':120,
      'AC' : 200
   },
   {
    
}
]
class TRAINS:
   def get_train_name(self,train_no):
      print(train_list)
   def get_trains_in_day(self,day):
      pass
   def total_fare(self,train_no):
      pass

t1 = TRAINS()
t1.get_train_name(45123)
    

