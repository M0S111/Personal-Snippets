class Resturant():
    def __init__(self, rest_name, cuisine):
        self.rest_name = rest_name
        self.cuisine = cuisine
        self.num_served = 0

    def biz_t(self):
        print('\n' + self.rest_name.title() + " is now open.")

    def desp(self):
        print('\n' + self.rest_name.title() + " is a/n " +
              self.cuisine.title() + " restaurant.")

    def num_cust(self):
        print('\n' + self.rest_name.title() + " has served " +
              str(self.num_served) + " customers today.")

    def inc_num(self, amount):
        self.num_served += amount


class Icecream_std(Resturant):

    def __init__(self, rest_name, cuisine):
        super().__init__(rest_name, cuisine)
        self.flav_list = ['Cherry', 'Cheesecake', 'Melon', 'Sorbet']

    def sayflavs(self):
        print("\nAvailable flavors are:", self.flav_list)


BR = Icecream_std('Baskin Robbins', 'Ice cream parlor')

BR.biz_t()

BR.desp()


BR.sayflavs()


rest_it = Resturant("guiliano'/s", "italian")

rest_it.biz_t()

rest_it.desp()

rest_it.num_served = 78

rest_it.inc_num(5)

rest_it.num_cust()

rest_c = Resturant('silver dragon', 'chinese')

rest_c.biz_t()

rest_c.desp()

rest_c.num_served = 44

rest_c.inc_num(19)

rest_c.num_cust()
