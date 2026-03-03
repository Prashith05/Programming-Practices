'''
    WAP using classes and objects
    * take the train details having the details like train number, train name, starting from, end, days, price of sleeper, general and 
       A/C
    * each train details should be in the form of dictionary and all the train details should be in the form of list
      as follows:
      train_details = 
        {
            'train_no' :84314,
            'train_name' : 'Mysore Express',
            'start' : 'Mysore',
            'end' : 'Bangalore',
            'days_of_run' : ['Sun' , 'Mon', Tue', 'Wed', 'Thu', 'Sat'],
            'general' : 60,
            'sleeper' : 120,
            'AC' : 200
        },
        {
            'train_no' : 12345,
            'train_name' : 'Chennai Express',
            'start' : 'Bangalore',
            'end' : 'Chennai',
            'days_of_run' : ['Mon', 'Wed', 'Fri'],
            'general' : 200,
            'sleeper' : 350,
            'AC' : 850
        }

        * Create methods like
            - get_train_name(train_no) -
                give train_no as parameter and if not available print msg
            - get_trains_in_day() -
                it should accept day name as a parameter and it should display all the train names which is running on that day
            - get_total_fare() - 
                it should accept 2 parameters 
                    1. train_no
                    2. dict of total seats = {
                                                'general' : 120,
                                                'sleeper' :20,
                                                'AC' : 30
                    }
                if i/p = 84314
                120 * 60 = 7200
                20 * 120 = 2400
                30 * 200 = 6000
                ---------------
                          15600

'''

class Train:

    def get_train_name(self, train_no):
        pass

    def get_trains_in_day(self, day):
        pass

    def total_fare(self, train_no):
        pass

train_details = {
        {
            'train_no' : 84314,
            'train_name' : 'Mysore Express',
            'start' : 'Mysore',
            'end' : 'Bangalore',
            'days_of_run' : ['Sun' , 'Mon', 'Tue', 'Wed', 'Thu', 'Sat'],
            'general' : 60,
            'sleeper' : 120,
            'AC' : 200
        },
        {
            'train_no' : 12345,
            'train_name' : 'Chennai Express',
            'start' : 'Bangalore',
            'end' : 'Chennai',
            'days_of_run' : ['Mon', 'Wed', 'Fri'],
            'general' : 200,
            'sleeper' : 350,
            'AC' : 850
        }
}

t = Train()
t.get_train_name(84314)