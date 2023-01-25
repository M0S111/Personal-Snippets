class User():

    def __init__(self,name_f,name_l):
        self.name_f=name_f
        self.name_l=name_l
        self.logs=5

    def say_name(self):
        print("User logged in: "+self.name_f.title()+" "+self.name_l.title())

    def sho_logs(self):
        print("No. of logs: "+str(self.logs))

    def log_inc(self,ink):
        self.logs+=ink

    def log_reset(self):
        self.logs=0


her=User('Hermione','slater')

her.say_name()

her.log_inc(3)

her.sho_logs()

her.log_reset()

her.sho_logs()

her.log_inc(9)

her.sho_logs()
