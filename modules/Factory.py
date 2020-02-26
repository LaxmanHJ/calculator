import modules.Main2 as Main2
import modules.Main as Main

class custobject(object):
    def factory(typeof):
        if typeof== 'cat1':
            return Main.main1()

        if typeof == 'cat2':
            return Main2.main2()
    factory = staticmethod(factory)

obj=custobject.factory("cat2")
obj.calc()