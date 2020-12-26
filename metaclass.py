MainMeta = type("MainMeta", (), {'is_main': True})

Meta = type("Meta", (MainMeta,), {})


class TestClass(Meta):
    pass


test = TestClass()

print(test)
print(test.is_main)
