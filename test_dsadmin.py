from dsadmin import Entry
from nose import SkipTest
from nose.tools import raises


class TestEntry(object):
    
    def test_init_empty(self):
        e = Entry('')
        assert not e.dn

    def test_init_str(self):
        e = Entry('o=pippo')
        assert e.dn == 'o=pippo'
        
    @raises(ValueError)
    def test_init_badstr(self):
        e = Entry('no equal sign here')
        
            
    def test_init_tuple(self):
        t = ( 'o=pippo', {
                'o': ['pippo'],
                'objectclass': ['organization', 'top']
                }
            )
        e = Entry(t)
        assert e.dn == 'o=pippo'

