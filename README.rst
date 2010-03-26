Extragen
========

Extract from live database and generate code to populate a new database through
SQLAlchemy API.

Goal
----

Python/SQLAlchemy code generation to populate a test database used for tests
setup.

The test database must hold copy of data of actual database, based on the
SQLAlchemy mapper definitions.

Use case
--------

The developer writes a SQLAlchemy query.

He can then pass an instance of the result set to the tool.

The result set is designated by its python dotted name.

Query without parameters
++++++++++++++++++++++++

::

        db = getDb('sanitel')
        Bovine = db.getMapper('BOVINE')
        AdultBovine = db.query(Bovine)
        AdultBovine = AdultBovine.filter(Bovine.age > 2)
        adultBovines = AdultBovine.all()

::

        foundation -r bovines.adultBovines

It outputs a python module in the current directory. 

::

        from Bovines import Bovine

        def setup(session):
                bovine1 = Bovine()
                bovine1.name = 'Marguerite'
                bovine1.age = 3
                session.save(bovine)
                bovine2 = Bovine()
                bovine2.name = 'Antoinette'
                bovine1.age = 4
                session.save(bovine2)
                session.flush()

::

        class TestAdultBovines(TestCase):
                def setUp(self):
                        db = getDb('sanitel')
                        setup_adultBovines.setup(db.session)

                def testOlder(self):
                        from bovines import adultBovines
                        for bovine in adultBovines:
                                self.failIf(bovine.age <= 2)


Query with parameters
+++++++++++++++++++++

::

        db = getDb('sanitel')
        Bovine = db.getMapper('BOVINE')
        def bovinesOlderThan(age):
                BovineOlderThan = db.query(Bovine)
                BovineOlderThan = AdultBovine.filter(Bovine.age > age)
                return BovineOlderThan.all()

::

        foundation -r bovines.bovinesOlderThan --age=2


TODO
====
Expand documentation for memoize
generator
