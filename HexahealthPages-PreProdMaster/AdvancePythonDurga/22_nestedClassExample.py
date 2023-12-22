class outer:
    class inner:
        def m1(self):
            pass


outer_obj=outer()
inner_obj=outer_obj.inner()
inner_obj.m1()

